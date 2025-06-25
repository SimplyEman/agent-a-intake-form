
def parse_email_scope(email_text):
    # Simple hardcoded logic for now; replace with offline LLM later
    if "extension of shelf-life" in email_text:
        return "To register an extension of shelf-life from 24 to 36 months based on new stability data, with updates to SPC sections 4.2, 5.1, and 6.6."
    elif "change in manufacturing site" in email_text:
        return "To register a change in manufacturing site with updates to SPC sections 3.2 and 6.3."
    else:
        return "To register a variation based on the attached details. Please verify SPC section references manually."
