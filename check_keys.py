import os
from dotenv import load_dotenv

# Load the variables from your .env file
load_dotenv()

def verify_config(name):
    value = os.getenv(name)
    if value and len(value) > 5:
        # We only show the first 5 chars for security (CISSP habit!)
        print(f"✅ {name}: Found! (Starts with: {value[:5]}...)")
    else:
        print(f"❌ {name}: NOT FOUND or EMPTY. Check your .env file.")

print("\n--- 🛡️ SECURE CONTRACT CO-PILOT: SYSTEM CHECK ---")
verify_config("AZURE_OPENAI_API_KEY")
verify_config("AZURE_OPENAI_ENDPOINT")
verify_config("AZURE_OPENAI_CHAT_DEPLOYMENT")
verify_config("DOCUMENT_INTELLIGENCE_KEY")
verify_config("DOCUMENT_INTELLIGENCE_ENDPOINT")
print("------------------------------------------------\n")