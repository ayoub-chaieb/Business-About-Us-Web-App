import streamlit as st
import pandas as pd
from send_email import send_email

st.set_page_config("Contact us !", layout="wide")
df = pd.read_csv("topics.csv")

with st.form("email_form", clear_on_submit=True, border=True):
    email = st.text_input("Your email")
    topic = st.selectbox("What do you want to contact us about ?", df["topic"])

    message = st.text_area("Your message")

    submitted = st.form_submit_button("Submit")

    if submitted:
        send_email(email, topic, message)
        st.info("Your message is sent successfully")
