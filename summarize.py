import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

if not API_TOKEN:
    raise ValueError("❌ HUGGINGFACE_API_KEY is not set in the .env file.")

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def generate_summary(text):
    # Optional: limit input size to avoid token overflow
    if len(text) > 2000:
        text = text[:2000]

    payload = { "inputs": text }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code != 200:
            print("❌ Error from Hugging Face API:")
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
            return "Error: Unable to summarize. Please try again later."

        data = response.json()
        return data[0].get('summary_text', 'No summary generated.')
    
    except Exception as e:
        print("⚠️ Exception while calling Hugging Face API:", str(e))
        return "Error: Exception occurred during summarization."
