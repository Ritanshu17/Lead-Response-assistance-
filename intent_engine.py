import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from prompts import INTENT_PROMPT 

#load environment variable from .env
load_dotenv()

#read api key from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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