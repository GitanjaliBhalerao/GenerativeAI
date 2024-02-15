import streamlit as st

from langchain.llms import OpenAI

#When deployed on huggingface spaces, this values has to be passed using Variables & Secrets setting, as shown in the video :)
import os
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_SECRET_KEY"

#Function to return the response
def load_answer(question):
    # "text-davinci-003" model is depreciated, so using the latest one https://platform.openai.com/docs/deprecations
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

