import streamlit as st
import os
from contract_parser import get_contract_details
from risk_analyzer import analyze_contract_risks

st.set_page_config(page_title="Secure Contract Co-Pilot", page_icon="🛡️")

st.title("🛡️ Secure Contract Co-Pilot")
st.markdown("### AI-Powered Legal Risk Analysis (CISSP-Grade Security)")

uploaded_file = st.file_uploader("Upload a Contract (PDF)", type="pdf")

if uploaded_file is not None:
    # Save the file temporarily
    with open("temp_contract.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🕵️ AI is auditing the contract..."):
        # 1. Parse
        _, full_text = get_contract_details("temp_contract.pdf")
        
        # 2. Analyze
        report = analyze_contract_risks(full_text)
        
        st.success("Analysis Complete!")
        
        # 3. Display Results
        st.markdown(report)
        
    # Clean up
    os.remove("temp_contract.pdf")

st.sidebar.info("This tool uses local redaction to protect PII before sending data to Azure OpenAI.")