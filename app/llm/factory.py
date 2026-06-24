from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

loaded = load_dotenv()

print("DOTENV LOADED:", loaded)
print("GROQ EXISTS:", bool(os.getenv("GROQ_API_KEY")))

def get_llm():
    return init_chat_model(
         "groq:llama-3.3-70b-versatile"
    )

def get_fast_llm():
    return init_chat_model(
        "groq:llama-3.1-8b-instant"
    )