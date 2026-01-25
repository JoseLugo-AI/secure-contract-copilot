from dotenv import load_dotenv
import os

load_dotenv()

print(f"Azure Endpoint Found: {bool(os.getenv('AZURE_OPENAI_ENDPOINT'))}")
print(f"Doc Intel Found: {bool(os.getenv('DOCUMENT_INTELLIGENCE_ENDPOINT'))}")