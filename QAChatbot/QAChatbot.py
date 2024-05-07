import google.generativeai as genai
import streamlit as st
st.set_page_config(page_title="QA Chatbot", page_icon=":robot:")
st.title('QA Chatbot')

from dotenv import load_dotenv
load_dotenv()



import os


genai.configure(api_key = os.getenv('GENAI_API_KEY'))

history = []

model = genai.GenerativeModel("gemini-pro")
chat= model.start_chat(history=history)

def get_gemini_response(input_text):
    return chat.send_message(input_text)



st.header("Gemini LLM Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("You: ", key="input")

submit=st.button("Submit")

if submit and input:
    st.session_state['chat_history'].append(f"You: {input}")
    response=get_gemini_response(input)
    st.subheader("Bot: ")
    st.write(response.candidates[0].content.parts[0].text)
    # for chunk in response:
    #     st.write(chunk)
    #     st.session_state['chat_history'].append(f"Bot: {chunk.text}") 

# for role,text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")        