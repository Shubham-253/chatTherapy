from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a sarcastic therapist Dr. Groove Hsarcas, instead of helping, you confuse your clients. If someone asks a general knowldedge question instead of answering directly you make it a joke on your client"),
        ("human", "Question:{question}"),
    ]
)

# streamlit

st.title("Welcome! I am your therapist Dr. Groove Hsarcas")
input_text = st.text_input("Tell me your problem in brief, do not bore me with details")

#openai

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
