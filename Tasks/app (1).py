import streamlit as st
import google.generativeai as genai

api_key = open("APIKEY.txt")
key =  api_key.read()

genai.configure(api_key=key)
st.title(":desktop_computer: AI Code Reviewer")


code_snippet = st.text_area("Enter your Python code here...")

prompt = f"The following Python code has an error. Debug it and give me the correct code"

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


button = st.button("Generate")

if button:
    response = model.generate_content([code_snippet,prompt])
    st.title("Fixed code")
    st.write(response.text)