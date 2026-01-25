import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

def get_contract_details(file_path):
    # 1. Initialize the Client
    client = DocumentIntelligenceClient(
        endpoint=os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT"),
        credential=AzureKeyCredential(os.getenv("DOCUMENT_INTELLIGENCE_KEY"))
    )

    # 2. Open the contract file
    with open(file_path, "rb") as f:
        # We use the "prebuilt-contract" model - this is the enterprise secret sauce
        poller = client.begin_analyze_document("prebuilt-contract", f)
        result = poller.result()

    # 3. Extract the high-value fields
    contract_data = {}
    if result.documents:
        doc = result.documents[0]
        # We look for specific legal fields Azure already knows
        for field_name in ["Parties", "EffectiveDate", "Termination", "GoverningLaw", "Renewal"]:
            field = doc.fields.get(field_name)
            if field:
                contract_data[field_name] = field.get('content')
    
    return contract_data, result.content # Returns specific fields + the full text

# --- TEST THE PARSER ---
if __name__ == "__main__":
    print("🚀 Starting Extraction from test_contract.pdf...")
    try:
        data, full_text = get_contract_details("test_contract.pdf")
        
        print("\n--- 📄 EXTRACTED LEGAL FIELDS ---")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        print("\n--- 📑 PREVIEW OF FULL TEXT (First 200 chars) ---")
        print(f"{full_text[:200]}...")
        print("---------------------------------")
        
    except Exception as e:
        print(f"❌ Error during extraction: {e}")