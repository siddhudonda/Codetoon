# core/gemini_api.py

import google.generativeai as genai
import os
from .prompt import GEMINI_PROMPT

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_cartoon_story(code):
    full_prompt = GEMINI_PROMPT + "\n```" + code + "\n```"
    response = model.generate_content(full_prompt)
    return response.text
