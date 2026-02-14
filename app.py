from fastapi import FastAPI
from intent_engine import extract_intent
from guardrails import validate_intent
from response_engine import build_response

app = FastAPI()

@app.post("/generate-reply")

def generate_reply(message: str):
    intent = extract_intent(query)
    validate_intent(intent)
    response = build_response(intent)

    return{
        "intent": intent,
        "reply": response
    } 