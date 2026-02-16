import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (.env)
load_dotenv()

# Create the OpenAI client once
client = OpenAI()

# App title
st.title("🛏️ Bedtime Story Generator")

st.write("Enter a topic and generate a one-paragraph bedtime story.")

# Text input field for the story topic
topic = st.text_input(
    "Story topic",
    placeholder="e.g. unicorn, dragon, astronaut, puppy"
)

# Button triggers the API call
if st.button("Generate story"):
    if topic.strip() == "":
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Creating a cozy bedtime story..."):
            response = client.responses.create(
                model="gpt-5-nano",
                input=f"Write a one-paragraph bedtime story about a {topic}."
            )

        st.success("Here’s your story:")
        st.write(response.output_text)