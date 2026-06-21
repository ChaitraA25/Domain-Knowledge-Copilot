from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_answer(question: str, context: str):
    prompt = f"""
    
You are a helpful assistant.

Answer the questions ONLY using the provided content,

Context:{context}

Question:{question}
"""
    response = client.responses.create(
        model = "gpt-4.1-mini",
        input = prompt
    )

    return response.output_text