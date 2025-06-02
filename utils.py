import openai
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Satwik@123',
    'database': 'voice_bot_db'
}

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
    """Log user queries and responses to the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO queries (user_query, response, response_time) VALUES (%s, %s, %s)",
            (user_query, response, response_time)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error logging query: {e}")
