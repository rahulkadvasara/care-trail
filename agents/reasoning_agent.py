import os
from groq import Groq
from dotenv import load_dotenv

# LOAD .env FILE
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


SYSTEM_PROMPT = """
You are a healthcare information assistant.
You must answer ONLY using the retrieved memory.
Do NOT provide diagnosis or treatment.
If insufficient information exists, say so clearly.
"""

def generate_response(query, memories):
    context = "\n".join(
        [f"- ({m['date']}) {m['text']}" for m in memories]
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"""
User Question:
{query}

Retrieved Memory:
{context}

Answer strictly using the retrieved memory and mention what was used.
"""}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
