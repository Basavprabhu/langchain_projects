#conversational ai bot that remembers the chat


import streamlit as st


from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models import ChatOpenAI

st.set_page_config(page_title="Conversational Q&A Bot")
st.header("Hey,let's chat")

from dotenv import load_dotenv  # type: ignore
load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a comedian AI assistant")
    ]

def get_chatmodel_response(question):
    # llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("ask a question")

if submit:
    st.subheader("the response is")
    st.write(response)

