# 🛡️ PlagiarismGuard AI

<div align="center">

# 🚀 Advanced Document Similarity & Plagiarism Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge\&logo=streamlit)
![DSA](https://img.shields.io/badge/Algorithms-KMP%20%7C%20Rabin--Karp-green?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Text%20Processing-orange?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-Portfolio%20Ready-success?style=for-the-badge)

### Detect • Analyze • Visualize • Report

An advanced plagiarism detection and document similarity analytics platform built using Python, Streamlit, KMP, Rabin-Karp, Winnowing Fingerprinting, MinHash, and Locality Sensitive Hashing (LSH).

</div>

---

# 📌 Overview

PlagiarismGuard AI is a professional document similarity analysis platform designed to detect exact matches, near-duplicate content, and plagiarism patterns using advanced Data Structures & Algorithms.

The platform processes uploaded documents, computes similarity using multiple techniques, visualizes results through interactive dashboards, and generates PDF reports for analysis.

---

# ✨ Key Features

## 📄 Document Processing

✅ Upload Original Document

✅ Upload Submission Document

✅ Real-Time Analysis

✅ Text Preprocessing

✅ Tokenization

✅ Cleaning & Normalization

---

## 🧠 Advanced Algorithms

### 🔹 KMP (Knuth-Morris-Pratt)

Efficient exact pattern matching using the Longest Prefix Suffix (LPS) array.

### 🔹 Rabin-Karp

String matching using rolling hash and hashing techniques.

### 🔹 Winnowing Fingerprinting

Near-duplicate document detection using document fingerprints.

### 🔹 MinHash

Compact document signatures for scalable similarity estimation.

### 🔹 Locality Sensitive Hashing (LSH)

Fast similarity search without comparing every document pair.

---

## 📊 Analytics Dashboard

### Executive Dashboard

* Similarity Score
* Winnowing Score
* MinHash Score
* Risk Assessment
* Interactive Charts

### Document Analysis

* Original Document Preview
* Submission Document Preview
* Common Matching Words
* Document Statistics

### Reports Center

* PDF Report Generation
* Similarity Summary
* Risk Classification

---

# 📷 Project Screenshots

## 🏠 Dashboard

![Dashboard](screenshots/dashboard-home.png)

---

## 📊 Similarity Analytics

![Metrics](screenshots/dashboard-metrics.png)

---

## 📄 Document Analysis

![Document Analysis](screenshots/document-analysis.png)

---

## 📑 Reports Center

![Reports](screenshots/reports-page.png)

---

# 🏗️ Project Architecture

```text
PlagiarismGuard-AI
│
├── app
│   │
│   ├── algorithms
│   │   ├── kmp.py
│   │   └── rabin_karp.py
│   │
│   ├── dashboard
│   │   └── dashboard.py
│   │
│   ├── detection
│   │   ├── similarity.py
│   │   ├── winnowing.py
│   │   └── minhash_lsh.py
│   │
│   ├── preprocessing
│   │   └── preprocess.py
│   │
│   └── utils
│       ├── file_loader.py
│       └── report_generator.py
│
├── data
│
├── reports
│
├── screenshots
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Algorithm Details

| Algorithm  | Purpose                |
| ---------- | ---------------------- |
| KMP        | Exact Pattern Matching |
| Rabin-Karp | Rolling Hash Matching  |
| Winnowing  | Fingerprint Generation |
| MinHash    | Similarity Estimation  |
| LSH        | Fast Similarity Search |

---

# 📈 Similarity Metrics

The platform generates:

### 📊 Similarity Score

Measures exact overlap between documents.

### 🔍 Winnowing Score

Measures fingerprint similarity.

### ⚡ MinHash Score

Measures signature-based similarity.

### 🚨 Risk Level

Classifies plagiarism risk as:

* 🟢 Low Risk
* 🟡 Moderate Risk
* 🟠 High Risk
* 🔴 Critical Risk

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/sujalkrshaw/PlagiarismGuard-AI.git
```

Move Into Project

```bash
cd PlagiarismGuard-AI
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

Launch Streamlit Dashboard

```bash
python -m streamlit run app/dashboard/dashboard.py
```

Dashboard will open at:

```text
http://localhost:8501
```

---

# 📑 PDF Reporting

Generate professional plagiarism reports including:

* Similarity Score
* Winnowing Score
* MinHash Score
* Risk Classification
* Executive Summary

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Data Structures & Algorithms
* String Matching Algorithms
* Hashing Techniques
* Fingerprinting Systems
* Similarity Search
* Dashboard Development
* Software Engineering
* PDF Report Generation
* Python Development
* Streamlit Applications

---

# 🔮 Future Enhancements

* PDF Upload Support
* DOCX Upload Support
* Semantic Similarity using AI
* Multi-Document Comparison
* User Authentication
* Database Integration
* Cloud Deployment
* REST API Integration
* Advanced Analytics Dashboard

---

# 💻 Tech Stack

### Backend

* Python

### Algorithms

* KMP
* Rabin-Karp
* Winnowing
* MinHash
* LSH

### Dashboard

* Streamlit
* Plotly
* Pandas

### Reporting

* ReportLab

---

# 🧑‍💻 Author

## Sujal Kumar  Shaw

B.Tech Student | Python Developer | DSA Enthusiast | Dashboard Developer

---

# ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

<div align="center">

## 🚀 Built with Python, Streamlit, KMP, Rabin-Karp, Winnowing, MinHash & LSH

### Thank you for visiting this repository ❤️

</div>
