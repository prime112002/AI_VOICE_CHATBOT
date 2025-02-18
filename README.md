# Project Title

AI Voice Chatbot 🎤🤖



## SUMMARY

Welcome to the AI Voice Chatbot project! This is an intelligent voice-based chatbot designed to handle customer interactions using Speech-to-Text, Natural Language Processing (NLP), and Text-to-Speech technologies. The bot can understand user queries, generate dynamic responses, and speak back to the user, making it ideal for customer support, FAQs, and more.
### Tech Stack 🛠️


```
Frontend: Streamlit

Backend: Python

Speech-to-Text: OpenAI Whisper

Natural Language Processing: OpenAI GPT-3.5

Text-to-Speech: gTTS (Google Text-to-Speech)

Database: MySQL
```

### Prerequisites  🚀

Python 3.7 or higher

MySQL Server

OpenAI API Key

### Setup Instructions 🚀

A step by step series of examples that tell you how to get a development env running

we need to clone the repo
```
git clone https://github.com/prime112002/AI_VOICE_CHATBOT.git
cd AI_VOICE_CHATBOT
```
 Set Up the Environment
Install Dependencies:

```
pip install -r requirements.txt
```
Set Up MySQL Database:

Create a database named voice_bot_db.

Run the SQL script located at database/setup_database.sql to create the required tables.

Set Up Environment Variables:

Create a .env file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the App  🎯 🎯 🎯

 how to  Run the Application
```
streamlit run app.py
`
