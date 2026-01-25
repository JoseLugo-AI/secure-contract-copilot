import re

def mask_sensitive_info(text):
    # Basic Regex for Counterparty/Competitor masking
    # In a real enterprise app, we'd use a list of known competitors
    masked_text = re.sub(r'(?i)CompetitorX|CompetitorY', "[REDACTED_COMPETITOR]", text)
    
    # Masking potential PII like Phone Numbers
    masked_text = re.sub(r'\+?\d{10,12}', "[REDACTED_PHONE]", masked_text)
    
    return masked_text