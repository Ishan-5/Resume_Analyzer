# AI Career Copilot 🚀

AI-powered Resume Analyzer and Career Assistant that evaluates resumes against job descriptions using NLP, semantic embeddings, ATS-style matching, and Large Language Models.

The system provides:

- ATS Match Score
- Resume Skill Extraction
- Missing Skill Identification
- Career Improvement Suggestions
- Personalized Learning Roadmap
- Interview Preparation Questions
- Project Recommendations

---

## Demo Features

### Resume Parsing
Extracts text directly from PDF resumes.

### Semantic Resume Matching
Uses transformer-based sentence embeddings to measure how closely a resume aligns with a target job description.

### Skill Gap Analysis
Identifies important skills present in the job description but missing from the candidate profile.

### AI Career Report
Generates a detailed report including:

- Resume strengths
- Weaknesses
- Career recommendations
- 30-day learning roadmap
- Interview questions
- Project suggestions

---

## Tech Stack

### Frontend
- Streamlit

### NLP & AI
- Hugging Face Transformers
- Sentence Transformers
- Groq LLM API
- NLP-based Skill Extraction

### Machine Learning
- Semantic Embeddings
- Cosine Similarity
- ATS Score Calculation

### Utilities
- PyPDF2
- Python
- dotenv

---

## System Architecture

PDF Resume
↓
Resume Text Extraction
↓
Skill Extraction
↓
Sentence Embeddings
↓
Resume Embedding
+
Job Description Embedding
↓
Cosine Similarity
↓
ATS Match Score
↓
Missing Skills Detection
↓
LLM Career Analysis
↓
Career Report

---

## Project Structure

AI_Career_Copilot/

├── app.py

├── utils/

│ ├── pdf_parser.py

│ ├── embeddings.py

│ ├── scorer.py

│ ├── skill_extractor.py

│ ├── prompts.py

│ └── llm.py

├── .env

├── requirements.txt

└── README.md

---

## Installation

Clone the repository

```bash
git clone <repo_url>
cd AI_Career_Copilot
