import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

def InitializeGeminiLLM():
    GeminiApiKey=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GeminiApiKey)
    GeminiLLM = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    return GeminiLLM





