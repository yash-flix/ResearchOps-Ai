from dotenv import load_dotenv
import os

print("Starting...")

loaded = load_dotenv(".env")

print("Loaded:", loaded)


print("Done")

from app.tools.web_search import web_search

print(
    web_search.invoke(
        {"query": "What is LangGraph?"}
    )
)