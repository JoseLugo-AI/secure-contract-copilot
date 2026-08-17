# Secure-Contract-Copilot: Legal Risk & PII Masking
**Portfolio demo — Azure OpenAI contract analysis with local PII redaction.**

[![Status](https://img.shields.io/badge/Status-Portfolio--Demo-lightgrey.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](#)
[![Security](https://img.shields.io/badge/Privacy-Local--Masking-red.svg)](#)
[![Model](https://img.shields.io/badge/Model-GPT--4o-blueviolet.svg)](#)

> **This is a portfolio / demo artifact, not a product and not a client deployment.** It shows how I approach Privacy-by-Design before data reaches a cloud model. My core offer is Microsoft 365 Copilot GDPR consulting: **[joselugo.de](https://joselugo.de)**.

## Overview
**Secure-Contract-Copilot** is a demo legal-analysis workflow: it extracts contract clauses (NDA, BPA, FAR) while masking sensitive identities and project IDs **locally** before cloud analysis.

Demo workflow notes already documented for this repo:

- Reduced contract review time: 2.5–5+ hours → 11–30 minutes
- Zero PII leakage to cloud models
- Full audit trail with per-contract cost tracking

### Key Highlights
* **Local Identity Masking:** Regex-based redaction masks names (e.g. `[PROTECTED_IDENTITY]`) and contract numbers (BPA/Project ID) before data leaves the local environment.
* **GPT-4o Risk Engine:** Uses a Senior Legal Counsel persona to analyze high-risk clauses including Unlimited Liability, Termination Notice, and Regulatory Compliance (FAR/U.S. Code).
* **Structural OCR:** Uses Azure AI Document Intelligence **Prebuilt-Contract** to keep legal-document structure during parsing.
* **Cost Governance:** Token tracking records the USD cost of each contract analyzed.

![Architecture diagram](./Secure-Contract-Copilot%20Architecture%20Diagram.png)

## Compliance & Governance Frameworks
This demo is designed around defense-contracting and privacy themes (it is not a certification or an audit result):

* **GDPR & Privacy:** Privacy by Design — PII is not stored in cloud prompts.
* **FAR 3.104:** Scans for Procurement Integrity Act themes and flags risks related to sensitive government information.
* **Title 18 U.S. Code § 1001:** Prompting includes awareness of false-certification risk in government contracts.
* **NIST AI RMF:** Risk labels are presented as Low, Medium, or High.

## Security & Hardening (CISSP Mindset)
Focus is **confidentiality** and **cost visibility** of the AI path:

* **Surgical Redaction:** The local `re` (regex) layer is meant to keep names such as "Jose Lugo" off the wire to the API provider.
* **Least Privilege Access:** Azure OpenAI is addressed via a specific deployment name.
* **Zero Persistence:** Temporary PDF buffers are cleared after analysis.
* **Dual-Validation:** Azure AI Document Intelligence (layout) plus GPT-4o (logic).

## Getting Started

### Prerequisites
- Python 3.14+
- Azure AI Document Intelligence (**Prebuilt-Contract** model)
- Azure OpenAI (**GPT-4o** deployment)
- Streamlit (dashboard UI)

### Installation & Usage
1. **Clone the repo:**

   ```bash
   git clone https://github.com/JoseLugo-AI/secure-contract-copilot.git
   cd secure-contract-copilot
   ```

2. **Install dependencies** (this repo does not currently ship a `requirements.txt`):

   ```bash
   pip install streamlit python-dotenv openai azure-ai-formrecognizer azure-identity
   ```

3. **Configure environment:** Create a `.env` file with your Azure endpoint, API key, and deployment name.

4. **Launch:**

   ```bash
   streamlit run app.py
   ```

## License & Contributions
* **License:** MIT License.
* **Contributing:** Open to contributions on specialized FAR/DFARS clause detection or expanded PII masking patterns.

## Author
**Jose Lugo** — Infrastructure Security Expert & AI Solutions Architect

A 12-year **U.S. Army Veteran** and **Senior Systems Administrator** specializing in **Cybersecurity (CISSP/Security+)**. Based in Germany. Core consulting offer: Microsoft 365 Copilot GDPR / DSGVO — [joselugo.de](https://joselugo.de).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)