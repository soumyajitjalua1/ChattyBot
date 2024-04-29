# Correct import statement
from langchain.llms.ctransformers import CTransformers  # Ensure correct import statement

from langchain.prompts import PromptTemplate
import streamlit as st

# Define getLLamaresponse function
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='C:\\Users\\soumy\\Downloads\\llama-2-7b-chat.ggmlv3.q6_K.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})
    
    template = """
                Write a blog for {blog_style} job profile for a topic {input_text}. The blog should be {no_words} words long.
               """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
    
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

# Streamlit setup and UI
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",  # You can use any suitable emoji here
    layout="centered",
    initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# creating two more columns for additional 2 fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
