import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)


def get_models():
    '''
    models/gemini-1.0-pro\n
    models/gemini-1.0-pro-001\n
    models/gemini-1.0-pro-latest\n
    models/gemini-1.0-pro-vision-latest\n
    models/gemini-1.5-pro-latest\n
    models/gemini-pro\n
    models/gemini-pro-vision\n
    '''
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

# get_models()
model = genai.GenerativeModel('gemini-pro')

prompt_parts = [
    "Write a Python function and explain it to me",
]

response = model.generate_content(prompt_parts)
print(response.text)
