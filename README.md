# 🛡️ Secure-Contract-Copilot: Legal Risk & PII Masking
**An AI-powered Legal Auditor for Defense & Enterprise Contracts with local PII Redaction.**

[![Status](https://img.shields.io/badge/Status-Project--Complete-success.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](#)
[![Security](https://img.shields.io/badge/Privacy-Local--Masking-red.svg)](#)
[![Model](https://img.shields.io/badge/Model-GPT--4o-blueviolet.svg)](#)

## 📖 Overview
The **Secure-Contract-Copilot** is a high-security legal analysis tool designed for government contractors and legal departments. It automates the extraction of complex contract clauses (NDA, BPA, FAR) while ensuring that sensitive identities and project IDs are masked locally before cloud analysis occurs.

- Reduced contract review time: 2.5–5+ hours → 11–30 minutes
- Zero PII leakage to cloud models
- Full audit trail with per-contract cost tracking

### Key Highlights:
* **🛡️ Local Identity Masking:** Uses Regex-based surgical redaction to mask names (e.g., [PROTECTED_IDENTITY]) and contract numbers (BPA/Project ID) before data leaves the local environment.
* **🧠 GPT-4o Risk Engine:** Employs a Senior Legal Counsel persona to analyze high-risk clauses including Unlimited Liability, Termination Notice, and Regulatory Compliance (FAR/U.S. Code).
* **🔍 Structural OCR:** Leverages Azure AI Document Intelligence "Prebuilt-Contract" models to maintain the structural integrity of legal documents during parsing.
* **💰 Cost Governance:** Integrated real-time token tracking provides a financial audit trail, calculating the exact USD cost of every contract analyzed.

---

## ⚖️ Compliance & Governance Frameworks
Designed to meet the rigorous standards of defense contracting and international privacy laws.

* **GDPR & Privacy:** Implements "Privacy by Design" by ensuring PII (Personal Identifiable Information) is never stored in cloud prompts.
* **FAR 3.104 Compliance:** Specifically scans for Procurement Integrity Act regulations and flags risks related to the handling of sensitive government information.
* **Title 18 U.S. Code § 1001:** Built-in awareness of criminal prosecution risks for false certifications within government contracts.
* **NIST AI RMF:** Aligns with the AI Risk Management Framework by providing consistent, deterministic risk levels (Low, Medium, High).

---

## 🛡️ Security & Hardening (CISSP Mindset)
This project focuses on the **Confidentiality** and **Economic Sustainability** of AI operations:

* **Surgical Redaction:** Unlike standard cloud-based redaction, our local `re` (Regex) layer ensures that sensitive names like "Jose Lugo" are never transmitted to the API provider.
* **Least Privilege Access:** Configured for Azure OpenAI using specific deployment nicknames, preventing unauthorized model access.
* **Zero Persistence:** Temporary PDF buffers are programmatically cleared after analysis to prevent data remnants on disk.
* **Dual-Validation:** Combines Azure AI Vision (for layout) with GPT-4o (for logic) to verify "hidden" risks that standard OCR might miss.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.14+
- Azure AI Document Intelligence (**Prebuilt-Contract** Model)
- Azure OpenAI (**GPT-4o** deployment)
- Streamlit (for the Dashboard UI)

### Installation & Usage
1. **Clone the repo:**
   git clone https://github.com/JoseLugo-AI/secure-contract-copilot.git
   cd secure-contract-copilot

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Configure Environment:** Create a .env file and add your Azure Endpoint, API Key, and Deployment Name.

4. **Launch Application:**
   streamlit run app.py

---

## 📜 License & Contributions
* **License:** MIT License.
* **Contributing:** Open to contributions regarding specialized FAR/DFARS clause detection or expanded PII masking patterns.

---

## 👨‍💻 Author
**Jose Lugo** *Infrastructure Security Expert & AI Solutions Architect*

A 12-year **U.S. Army Veteran** and **Senior Systems Administrator** specializing in **Cybersecurity (CISSP/Security+)**. Based in Germany, I bridge the gap between complex US-based security frameworks and European data privacy laws.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)
