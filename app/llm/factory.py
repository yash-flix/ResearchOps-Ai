from langchain.chat_models import init_chat_model

def get_llm():
    return init_chat_model(
         "groq:llama-3.3-70b-versatile"
    )