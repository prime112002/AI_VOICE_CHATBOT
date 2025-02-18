import streamlit as st
from utils import speech_to_text, get_answer, text_to_speech, fetch_customer_data, log_query
from audio_recorder_streamlit import audio_recorder
import os
import uuid
import time

# Create a temporary folder for audio files
if not os.path.exists("temp_audio"):
    os.makedirs("temp_audio")

# Initialize session state for managing chat messages
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

initialize_session_state()

st.title("Intelligent Voice Bot for Customer Interaction 🤖")

# Create a container for the microphone and audio recording
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

if audio_bytes:
    with st.spinner("Transcribing..."):
        # Generate a unique filename for the audio file
        audio_file_path = f"temp_audio/temp_audio_{uuid.uuid4().hex}.wav"
        with open(audio_file_path, "wb") as f:
            f.write(audio_bytes)

        # Convert the audio to text using the speech_to_text function
        try:
            transcript = speech_to_text(audio_file_path)
            if transcript:
                st.session_state.messages.append({"role": "user", "content": transcript})
                with st.chat_message("user"):
                    st.write(transcript)
        except Exception as e:
            st.error(f"Error during speech-to-text conversion: {e}")
        finally:
            # Clean up the temporary audio file
            if os.path.exists(audio_file_path):
                os.remove(audio_file_path)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            try:
                start_time = time.time()
                final_response = get_answer(st.session_state.messages)
                response_time = time.time() - start_time
                log_query(st.session_state.messages[-1]["content"], final_response, response_time)
            except Exception as e:
                st.error(f"Error generating response: {e}")
                final_response = "Sorry, I encountered an error. Please try again."

        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})

        with st.spinner("Generating audio response..."):
            try:
                audio_file = text_to_speech(final_response)
                st.audio(audio_file, format="audio/mp3")
            except Exception as e:
                st.error(f"Error generating audio: {e}")
            finally:
                # Clean up the temporary audio file
                if os.path.exists(audio_file):
                    os.remove(audio_file)