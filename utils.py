import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter API setup
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def get_answer(messages):
    """Generate a response using OpenRouter."""
    try:
        system_prompt = {"role": "system", "content": "You are a helpful AI chatbot for customer support."}
        response = openai.ChatCompletion.create(
            model="mistralai/mixtral-8x7b-instruct",  # Valid OpenRouter model slug
            messages=[system_prompt] + messages
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I encountered an error while generating a response."

def log_query(user_query, response, response_time):
    """Simple logging to console instead of database."""
    print(f"[LOG] User query: {user_query}")
    print(f"[LOG] Response: {response}")
    print(f"[LOG] Response time: {response_time:.2f} seconds")
