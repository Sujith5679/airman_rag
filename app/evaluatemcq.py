import json
import requests
from time import sleep

API_URL = "http://127.0.0.1:8000/ask"
JSON_FILE = r"C:\Users\sujit\Desktop\armiango\questions\mcqquestions.json"  

with open(JSON_FILE, "r") as f:
    data = json.load(f)

results = {
    "correct": [],
    "incorrect": [],
    "refused": [],
    "failed": [],
    "details": []
}

def detect_choice(answer, options):
    """Match answer to A/B/C/D using option text matching"""
    answer_lower = answer.lower()

    for key, text in options.items():
        if text.lower() in answer_lower:
            return key  
    for key, text in options.items():
        if key.lower() in answer_lower:   
            return key

    return None

for q in data["questions"]:
    q_id = q["id"]
    question = q["question"]
    options = q["options"]

    print(f"\n Question {q_id}: {question}")

    try:
        res = requests.post(f"{API_URL}?q={question}", timeout=120)
        raw_answer = res.json().get("answer", "").strip()

        choice = detect_choice(raw_answer, options)

        detail = {
            "id": q_id,
            "question": question,
            "model_answer": raw_answer,
            "matched_choice": choice
        }

        if raw_answer == "This information is not available in the provided document(s).":
            results["refused"].append(q_id)
            detail["status"] = "refused"

        elif choice is None:
            results["failed"].append(q_id)
            detail["status"] = "failed (no match)"

        else:
            results["correct"].append(q_id)
            detail["status"] = "answered (choice matched)"

        results["details"].append(detail)

    except Exception as e:
        results["failed"].append(q_id)
        results["details"].append({
            "id": q_id,
            "question": question,
            "model_answer": None,
            "status": "failed (timeout/error)",
            "error": str(e),
        })

    sleep(1)

# Summary Report
total = len(data["questions"])
accuracy = len(results["correct"]) / total

report = {
    "summary": {
        "total": total,
        "choice_matched": len(results["correct"]),
        "refused": len(results["refused"]),
        "failed": len(results["failed"]),
        "model_selection_accuracy_rate": round(accuracy, 2)
    },
    "details": results["details"]
}

with open("evaluation_sample_mcq_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("\n SAMPLE MCQ EVALUATION COMPLETE!")
print("Report saved to evaluation_sample_mcq_report.json")
