import os
import re
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# --- 1. CISSP SECURITY LAYER: LOCAL REDACTOR ---
def local_redact(text):
    """Masks names and PII locally before cloud processing."""
    # Mask specific names (like yours) and common PII patterns
    redacted = re.sub(r'(Name:?\s*)([A-Z][a-z]+\s[A-Z][a-z]+\s?[A-Z]?[a-z]*)', r'\1[PROTECTED_IDENTITY]', text)
    redacted = re.sub(r'(BPA Number:?\s*)(\w+)', r'\1[REDACTED_ID]', redacted)
    return redacted

# --- 2. INITIALIZE AZURE CLIENT ---
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

# --- 3. RISK ANALYSIS ENGINE WITH COST TRACKING ---
def analyze_contract_risks(contract_text):
    # January 2026 Azure GPT-4o Pricing
    PRICE_INPUT_1K = 0.0025  
    PRICE_OUTPUT_1K = 0.0100 

    # Local Scrubbing
    secure_text = local_redact(contract_text)
    
    system_prompt = "You are a Senior Legal Counsel. Analyze this contract for liability, termination, and compliance risks."

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Analyze: {secure_text[:4000]}"}
        ],
        temperature=0.1
    )

    # Cost Tracking
    usage = response.usage
    input_cost = (usage.prompt_tokens / 1000) * PRICE_INPUT_1K
    output_cost = (usage.completion_tokens / 1000) * PRICE_OUTPUT_1K
    total_cost = input_cost + output_cost

    report = response.choices[0].message.content
    
    cost_footer = f"\n\n--- 💰 COST ANALYSIS ---"
    cost_footer += f"\nTokens Used: {usage.total_tokens} (In: {usage.prompt_tokens}, Out: {usage.completion_tokens})"
    cost_footer += f"\nEstimated Cost: ${total_cost:.4f}"
    
    return report + cost_footer

# --- 4. TEST EXECUTION ---
if __name__ == "__main__":
    from contract_parser import get_contract_details
    
    print("🧠 Starting Secure Risk Analysis with Cost Tracking...")
    try:
        _, full_text = get_contract_details("test_contract.pdf")
        final_report = analyze_contract_risks(full_text)
        print("\n--- ⚖️ LEGAL RISK REPORT ---")
        print(final_report)
    except Exception as e:
        print(f"❌ Error: {e}")