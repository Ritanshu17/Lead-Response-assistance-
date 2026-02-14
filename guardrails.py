def validate_intent(intent):
    if intent['problem'] == 'unknown':
        raise ValueError("Insufficient information.")
    return True