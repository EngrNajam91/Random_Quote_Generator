import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="📜", layout="centered")

st.title("📜 Random Quote Generator")

# Some sample quotes
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Happiness depends upon ourselves. – Aristotle",
    "It always seems impossible until it is done. – Nelson Mandela",
    "If you want to lift yourself up, lift up someone else. – Booker T. Washington",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
]

# Button to generate random quote
if st.button("✨ Generate Quote"):
    st.success(random.choice(quotes))
else:
    st.info("Click the button to get a random quote!")
