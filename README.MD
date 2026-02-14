📩 CustomerCare-AI

AI Workflow for Understanding Customer Enquiries and Drafting Reliable Responses
🔎 Objective

This project demonstrates how to design a **real-world AI workflow** that:

* Understands customer intent
* Asks relevant follow-up questions
* Provides safe, non-hallucinated guidance
* Handles missing or uncertain information gracefully
* Remains reliable even if the LLM fails

The goal is to showcase **practical LLMOps thinking**, not just prompting.


🏗️ System Architecture:- 
Customer Message
      ↓
Intent Extraction (LLM)
      ↓
Validation + Guardrails
      ↓
Fallback Handling (if AI fails)
      ↓
Response Composer
      ↓
Safe, Human-Like Reply


This ensures:

* No hallucinated claims
* Explainable behavior
* Stable automation



⚙️ Tech Stack

| Component        | Technology          |
| ---------------- | ------------------- |
| Backend API      | FastAPI             |
| LLM Integration  | OpenAI API          |
| Validation       | Python + Guardrails |
| Environment Mgmt | python-dotenv       |
| Server           | Uvicorn             |


📁 Project Structure


customer-care-ai/
│
├── app.py                 # FastAPI entry point
├── intent_engine.py       # LLM + structured extraction
├── response_engine.py     # Safe reply generation
├── guardrails.py          # Validation & fallback logic
├── prompts.py             # System prompts
├── requirements.txt
├── .env                   # API key (not committed)
└── README.md

🚀 Setup & Execution Process

 1️⃣ Clone / Download Project

```
git clone <repo-link>
cd customer-care-ai
```

---

2️⃣ Create Virtual Environment

Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

-------------------------------------------------------------------------------------------

3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

----------------------------------------------------------------------------------------------

🔐 Environment Variable Initialization

Create a file named:

```
.env
```

Inside the project root.

Add your OpenAI API key:

```
OPENAI_API_KEY=your_actual_api_key_here
```

⚠️ Important:

* Do NOT add quotes
* Do NOT commit `.env` to Git
* This keeps credentials secure

----------------------------------------------------------------------------------------------

🔑 How to Get API Key

1. Visit: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Generate a new secret key
3. Paste it into `.env` file

----------------------------------------------------------------------------------------------

▶️ Running the Application

Start the FastAPI server:

```
uvicorn app:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

---

🧪 Testing the Workflow

Open in browser:

```
http://127.0.0.1:8000/docs
```

Use Swagger UI:

1. Click `POST /generate-reply`
2. Click **Try it out**
3. Enter example message:

```
Hi, I am getting damp patches on my bedroom wall after rains.
```

4. Click **Execute**

---

✅ Example Behavior

The system will:

✔ Acknowledge the issue
✔ Ask clarifying questions
✔ Provide safe next steps
✔ Avoid assumptions
✔ Never crash if AI fails

----------------------------------------------------------------------------------------------

🛡️ Reliability Features Implemented

* Structured intent extraction (JSON-only enforcement)
* Guardrails to prevent hallucinated advice
* Graceful fallback if API/model fails
* Deterministic prompting (temperature = 0)
* Validation layer before response generation

----------------------------------------------------------------------------------------------

⚠️ Known Limitations

* No image-based diagnosis yet
* No domain knowledge retrieval (RAG)
* Single-turn interaction (no memory)
* Uses general model instead of fine-tuned one

----------------------------------------------------------------------------------------------

🔮 Future Improvements

* Add document retrieval for verified repair guidance
* Add conversation memory
* Add severity classification
* Add monitoring dashboard
* Multi-language support

----------------------------------------------------------------------------------------------



**Author:** Ritanshu Mankar

----------------------------------------------------------------------------------------------


