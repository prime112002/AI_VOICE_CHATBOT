from openai import OpenAI
import os
import time

# Setup OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_answer(messages):
    """Generate a response using OpenRouter."""
    try:
        system_prompt = {"role": "system", "content": "You are a helpful AI chatbot for customer support."}
        start_time = time.time()
        
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[system_prompt] + messages
        )
        
        end_time = time.time()
        response_text = response.choices[0].message.content
        log_query(messages[-1]["content"], response_text, end_time - start_time)
        return response_text
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I encountered an error while generating a response."

def log_query(user_query, response, response_time):
    print(f"[LOG] User query: {user_query}")
    print(f"[LOG] Response: {response}")
    print(f"[LOG] Response time: {response_time:.2f} seconds")
