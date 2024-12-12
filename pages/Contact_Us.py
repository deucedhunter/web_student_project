import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv('topics.csv')
print(df)
with st.form("my_form"):
    email_address = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",df['topic'])
    raw_message = st.text_area("Text")
    submit = st.form_submit_button("Submit")
    message=f"""Subject:{topic}
    
    
From:{email_address}
{raw_message}"""
    if submit:
        send_email(email_address, message=message)
        st.info("Email sent")