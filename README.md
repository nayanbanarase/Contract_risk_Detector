AI Contract Risk Detector
An AI-Powered Contract Analysis System Using FastAPI, React.js, SQLite, OCR, NLP, and Large Language Models

Abstract
The AI Contract Risk Detector is an intelligent web-based application developed to automate the analysis of legal contracts and identify potential risks. The system extracts text from PDF and scanned image contracts using PyPDF2 and Tesseract OCR, analyzes the content using Natural Language Processing (NLP) and rule-based risk detection, and generates AI-assisted summaries through Ollama (Phi-4/Llama 3). It identifies important clauses such as penalties, liabilities, termination conditions, deadlines, and hidden fees while assigning a risk score to the contract. The application is built using Python, FastAPI, React.js, SQLite, spaCy, and OCR technologies, providing a simple and efficient platform for contract analysis.

Keywords: Artificial Intelligence, Contract Analysis, FastAPI, React.js, OCR, NLP, SQLite, Ollama, Risk Detection.

1. Introduction
Legal contracts often contain complex language that makes it difficult for individuals and organizations to identify risky clauses. Manual contract review is time-consuming, expensive, and prone to human error.

The AI Contract Risk Detector is designed to simplify this process by automatically extracting text from contracts, identifying risky clauses, calculating a risk score, and generating an easy-to-understand summary. The project combines Artificial Intelligence, Natural Language Processing, and Optical Character Recognition to improve the efficiency and accuracy of contract analysis.

2. Literature Review
Several existing systems focus on contract management and legal document processing. Traditional methods rely on manual review by legal professionals, which is costly and time-intensive.

Recent advancements in Artificial Intelligence and Natural Language Processing have enabled automated analysis of legal documents. OCR technologies such as Tesseract allow extraction of text from scanned contracts, while language models assist in understanding document context. Frameworks like FastAPI simplify backend development, and React.js provides responsive user interfaces. This project integrates these technologies into a single application for intelligent contract analysis.

3. Methodology
The proposed system follows the following workflow:

User uploads a contract in PDF or image format.

Text is extracted using PyPDF2 or Tesseract OCR.

Extracted text is processed using spaCy for NLP tasks.

A rule-based engine detects risk-related keywords such as penalties, liabilities, indemnity, termination clauses, and hidden fees.

A numerical risk score is calculated.

The extracted information is stored in an SQLite database.

The contract is summarized using an Ollama Large Language Model (Phi-4/Llama 3).

Results are displayed on a React.js dashboard.

4. System Architecture
User
   │
   ▼
React.js Frontend
   │
   ▼
FastAPI Backend
   │
   ├───────────────┐
   ▼               ▼
PDF Reader      OCR Reader
(PyPDF2)      (Tesseract OCR)
   │               │
   └───────► Text Extraction
                   │
                   ▼
            NLP Processing (spaCy)
                   │
                   ▼
          Risk Detection Engine
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
   Risk Score         AI Summary (Ollama)
         │                   │
         └─────────┬─────────┘
                   ▼
             SQLite Database
                   │
                   ▼
            Dashboard Results
5. Implementation
Frontend
React.js

Axios

HTML

CSS

The frontend provides:

Contract upload interface

Risk analysis dashboard

AI-generated summary

Risk score display

Backend
Developed using FastAPI.

Responsibilities:

Receive uploaded contracts

Extract document text

Process risk detection

Generate AI summary

Store results in database

Database
SQLite stores:

Contract name

Upload date

Risk score

Analysis summary

OCR Module
Implemented using:

Tesseract OCR

Pillow

Used for extracting text from scanned contracts and images.

NLP & AI Module
Technologies:

spaCy

Ollama

Phi-4 / Llama 3

Functions:

Contract summarization

Risk explanation

Deadline extraction

Clause identification

Risk Detection
The rule-based engine identifies keywords including:

Penalty

Liability

Indemnity

Lawsuit

Termination

Additional Fee

Service Charge

Processing Fee

A predefined scoring mechanism generates an overall contract risk score.

6. Software Requirements
Python 3.10+

Node.js

React.js

FastAPI

SQLite

PyPDF2

pdfplumber

spaCy

Tesseract OCR

Pillow

Ollama

VS Code

7. Hardware Requirements
Minimum
Intel Core i3 Processor

4 GB RAM

10 GB Free Storage

Recommended
Intel Core i5/i7

8 GB RAM

SSD Storage

8. Features
PDF Contract Upload

OCR Support for Scanned Contracts

Automatic Text Extraction

AI-Based Contract Summary

Risk Clause Detection

Hidden Fee Detection

Deadline Identification

Risk Score Calculation

SQLite Database Storage

Interactive React Dashboard

9. Applications
Law Firms

Business Organizations

HR Departments

Procurement Teams

Financial Institutions

Insurance Companies

Government Offices

10. Advantages
Reduces manual effort

Faster contract analysis

Identifies risky clauses

Supports scanned documents

Generates AI-powered summaries

Easy-to-use interface

Free and open-source technologies

11. Limitations
Current risk detection mainly uses predefined rules.

Accuracy depends on document quality.

AI-generated summaries depend on the selected LLM.

SQLite is suitable for small to medium deployments.

12. Future Scope
The project can be enhanced by incorporating advanced Machine Learning models for intelligent risk prediction instead of rule-based analysis. Future versions may include multilingual contract support, cloud deployment, user authentication, contract comparison, semantic search using vector databases, Retrieval-Augmented Generation (RAG) based contract chatbot, digital signature verification, and integration with enterprise contract management systems.

13. Conclusion
The AI Contract Risk Detector demonstrates how Artificial Intelligence, Natural Language Processing, OCR, and modern web technologies can automate legal contract analysis. The system reduces the time required for manual review by identifying risky clauses, extracting important information, generating AI-powered summaries, and maintaining contract records. The project serves as a practical and scalable solution for intelligent document analysis while providing a strong foundation for future AI-driven legal technologies.

References
FastAPI Documentation. https://fastapi.tiangolo.com/

React.js Documentation. https://react.dev/

SQLite Documentation. https://www.sqlite.org/docs.html

PyPDF2 Documentation. https://pypdf2.readthedocs.io/

spaCy Documentation. https://spacy.io/

Tesseract OCR Documentation. https://tesseract-ocr.github.io/

Ollama Documentation. https://ollama.com/

Python Software Foundation. https://www.python.org/

Pillow Documentation. https://pillow.readthedocs.io/

Jurafsky, D., & Martin, J. H. Speech and Language Processing. Pearson Education
