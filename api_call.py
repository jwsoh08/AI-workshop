# Exercise 7: Calling OpenAI LLM API

import streamlit as st
import openai


st.title("Api Call")
openai.api_key = st.secrets["openapi_key"]
MODEL = "gpt-3.5-turbo"


response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about Singapore in the 1970s"},
    ],
    temperature=0,
)
st.write(response)
