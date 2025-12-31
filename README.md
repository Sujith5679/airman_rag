# Aviation RAG System — Level 1 Submission
## **1. Project Summary**

This project is a Retrieval-Augmented Generation (RAG) based Question Answering System for aviation domain knowledge.
It uses aviation textbooks as the only source of truth and answers questions based strictly on the content of those documents.

If the answer is not present in the documents, the system refuses to answer instead of guessing.
This eliminates hallucination and ensures reliability.

---
## **2. Objective**

* To build an AI system that retrieves information from aviation PDFs.
* To answer questions using only that retrieved text.
* To prevent hallucinations (no invented information).
* To evaluate the system using 50 aviation questions.

---

## **3. How the System Works**

### Step 1: PDF Ingestion

A set of aviation textbooks (7 PDFs) are converted to text, split into chunks, and embedded into a vector database (FAISS) so that they can be searched efficiently.

### Step 2: Retrieval

When a question is asked, the system searches the vector database and retrieves the most relevant text passages.

### Step 3: Answer Generation

The retrieved text is passed to an LLM (LLaMA 2 via Ollama) which forms the answer.
The model is instructed to use **only** the retrieved text and nothing else.

### Step 4: Hallucination Control

If the information is not available in the documents, the system responds with:

This information is not available in the provided document(s).

This ensures that the model does not guess or fabricate answers.

---

## **4. Architecture Overview**

* FastAPI backend to handle user queries.
* Sentence Transformers for text embeddings.
* FAISS Vector Store for document search.
* LLaMA 2 (Ollama) as the language model.
* Strict refusal rules to avoid hallucination.

---

## **5. Models and Tools Used**

* Programming Language: Python
* LLM: LLaMA 2 (local inference with Ollama)
* Vector Store: FAISS
* Embeddings Model: SentenceTransformer
* API Framework: FastAPI
* PDF Parsing: PyPDF

---

## **6. Evaluation**

The system was tested with 50 aviation knowledge questions.

**Evaluation Results:**

* Total Questions: 50
* Grounded Answers (answered with support): 25
* Refused (correct refusal, no answer available): 14
* Failed (timeout or retrieval issue): 11
* Retrieval Hit Rate: 50%
* Faithfulness: 100%
* Hallucination Rate: **0%**

### Interpretation:

* The system answers correctly when relevant information is found.
* It safely refuses when unsure, instead of hallucinating.
* Areas to improve include retrieval accuracy and multi-passage understanding.

---

## **7. MCQ Evaluation**

A second evaluation was performed using aviation multiple-choice questions.

**MCQ Results:**

* Total MCQs: 50
* Answerable / Matched: 25
* Refused: 14
* Failed / Unmatched Response: 11
* Observed Bias: Model sometimes defaults to Option A when unsure.

**Reason for Bias:**
The model is not trained for MCQ answering format and often selects the first plausible option.
This will be addressed in Level 2.

---

## **8. Key Strengths**

* Zero hallucinations (safety by design)
* Traceable answers with citations
* Works offline with local LLM
* Domain-limited, controlled knowledge

---

## **9. Current Limitations**

* Retrieval accuracy is 50% and needs improvement.
* Model is not specifically trained for aviation exams.
* Multiple-choice question handling is basic.
* Slow responses due to local CPU inference.

---

## **10. Planned Improvements for Level 2**

* Hybrid search (BM25 + FAISS)
* Reranking using cross-encoders
* Better MCQ reasoning prompt
* Confidence scoring
* Improved chunking and contextual retrieval
* Optional chat UI using Streamlit

---

## **11. How to Run the System**

1. Start the FastAPI Server:
   uvicorn app.main:app --reload

2. Ask a question using:
   [http://127.0.0.1:8000/ask?q=Your](http://127.0.0.1:8000/ask?q=Your) Question Here

3. Evaluate performance:
   python app/evaluate.py

---

## **12. Submission Package Includes**

* Source code files
* Evaluation reports (JSON)
* Instructions (this document)
* Drive link to aviation documents (PDFs not submitted due to size)

---

## **13. Conclusion**

This Level 1 submission successfully demonstrates:

* A working RAG pipeline
* Domain-bounded responses
* No hallucinations
* Evaluation with real aviation questions

---

# ** End of Submission **
drive link to the dataset(PDFs) -> https://drive.google.com/drive/folders/19zsPPy_nxo570GQK0_Kydm_pJ2KWixd0?usp=sharing
---


