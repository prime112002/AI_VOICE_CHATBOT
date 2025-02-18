import openai
import mysql.connector
from gtts import gTTS
import os
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
db_config = {
    'host': 'localhost',  # Replace with your MySQL host
    'user': 'root',       # Replace with your MySQL username
    'password': 'Satwik@123',  # Replace with your MySQL password
    'database': 'voice_bot_db'  # Replace with your database name
}

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def speech_to_text(audio_file_path):
    """Convert audio to text using OpenAI Whisper."""
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        return response['text']
    except Exception as e:
        print(f"Error during speech-to-text conversion: {e}")
        return None

def text_to_speech(input_text):
    """Convert text to speech using gTTS."""
    try:
        # Generate a unique filename for the audio file
        audio_file_path = f"temp_audio/temp_audio_response_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=input_text, lang='en')
        tts.save(audio_file_path)
        return audio_file_path
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return None

def fetch_customer_data(account_number):
    """Fetch customer data from the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE account_number = %s", (account_number,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching customer data: {e}")
        return None

def log_query(user_query, response, response_time):
    """Log user queries and responses to the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO queries (user_query, response, response_time) VALUES (%s, %s, %s)",
                      (user_query, response, response_time))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error logging query: {e}")

def get_answer(messages):
    """Generate a response using OpenAI GPT-3.5."""
    try:
        system_message = [{"role": "system", "content": "You are a helpful AI chatbot for customer support."}]
        messages = system_message + messages
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I encountered an error. Please try again."