import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
import streamlit as st
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.memory import ConversationBufferMemory

os.environ["OPENAI_API_KEY"]=openai_key

st.title('Celebrity search results')
input_text=st.text_input('Search the topic u want...')

#prompt template
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="tell me about {name}"
)



llm= OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='title')

second_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="when was {title} born?"
)

chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')

parent_chain=SimpleSequentialChain(chains=[chain,chain2],verbose=True)



if input_text:
    st.write(parent_chain.run(input_text))




