# Exercise 5 : Building a simple chatbot
# import streamlit as st
# import numpy as np

# st.title("My first chatbot app")


# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# Grab user inputs
# name = st.text_input("Enter your name")
# gender = st.selectbox("State your gender", ["Male", "Female"])
# age = st.text_input("State your age", 18)

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("Say something"):
#     if prompt == "Hello":
#         with st.chat_message("user"):
#             st.write("Hello")
#             st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("assistant"):
#             reply = "Hi there what can I do for you"
#             st.write(reply)
#             st.session_state.messages.append({"role": "assistant", "content": reply})

#     elif prompt == "What is your name?":
#         with st.chat_message("user"):
#             st.write("What is your name?")
#             st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("assistant"):
#             reply = "My name is EAI , an electronic artificial being"
#             st.write(reply)
#             st.session_state.messages.append({"role": "assistant", "content": reply})

#     elif prompt == "How old are you?":
#         with st.chat_message("user"):
#             st.write("How old are you?")
#             st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("assistant"):
#             reply = "Today is my birthday!"
#             st.write(reply)
#             st.session_state.messages.append({"role": "assistant", "content": reply})

#     else:
#         with st.chat_message("user"):
#             st.write(prompt)
#             st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("assistant"):
#             reply = "I am sorry, I am unable to help you with your query"
#             st.write(reply)
#             st.session_state.messages.append({"role": "assistant", "content": reply})


# Exercise 6: Building a simple chatbot that echo your responses (part 1)

# import streamlit as st

# st.title("Echo Bot")

# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# React to user input
# if prompt := st.chat_input("What is up?"):
    # st.chat_message("user").markdown(prompt)
    # st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {prompt}"
    # with st.chat_message("assistant"):
    #     st.markdown(response)
    # st.session_state.messages.append({"role": "assistant", "content": response})


# Exercise 6: Secrets- Shhh (part 2)
# import streamlit as st
# import openai 

# st.title("Api Call")
# openai.api_key = st.secrets["openapi_key"]
# MODEL = "gpt-3.5-turbo"


# response = openai.ChatCompletion.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Tell me about Singapore in the 1970s"},
#     ],
#     temperature=0,
# )
# st.write(response)

# Exercise 7 : Incorporate your LLM API call into your chatbot

# import streamlit as st
# import openai 

# def get_response_from_openai(prompt):
#     if prompt:
#         st.write(f"User has sent the following prompt: {prompt}")
#         # save user input in message history
#         st.session_state.messages.append(prompt)

#         openai.api_key = st.secrets["openapi_key"]
#         MODEL = "gpt-3.5-turbo"


#         response = openai.ChatCompletion.create(
#             model=MODEL,
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt},
#             ],
#             temperature=0,
#         )

#         return response
#     else:
#         return "No input detected. Please enter an input."
    
# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.title("Chat bot response from API call")

# if prompt:=st.chat_input("Say something"):
#     response = get_response_from_openai(prompt)
#     st.write(response)

# Exercise 8: Your first AI Chatbot

# import openai
# import streamlit as st

# st.title("ChatGPT-like clone")

# openai.api_key = st.secrets["openapi_key"]

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)


#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += response.choices[0].delta.get("content", "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})

# Exercise 9: Prompt Engineering
import streamlit as st
import openai

st.title("Api Call")
openai.api_key = st.secrets["openapi_key"]
MODEL = "gpt-3.5-turbo"


response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"},
        {"role": "user", "content": "Tell me about Singapore in the 1970s"},
    ],
    temperature=0,
)
st.write(response)

