from openai import OpenAI
import json
from prompts import INTENT_PROMPT 

client = OpenAI()

def extract_intent(message : str):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": INTENT_PROMPT},
            {"role": "user", "content": message}
        ],
        temperature = 0
    )

    return json.loads(response.choices[0].message.content)