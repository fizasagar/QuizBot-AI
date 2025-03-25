import streamlit as st
import openai

def generate_quiz(topic):
    """Generates a quiz based on the given topic using OpenAI API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": f"Generate a short 3-question quiz on {topic}."}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "Error generating quiz. Please try again."

# Streamlit UI
st.title("QuizBot AI 🤖")
st.write("Generate an AI-powered quiz on any topic instantly!")

# User input for quiz topic
topic = st.text_input("Enter a topic for your quiz:")

if st.button("Generate Quiz"):
    if topic:
        quiz = generate_quiz(topic)
        st.subheader("Here is your quiz:")
        st.write(quiz)
    else:
        st.warning("Please enter a topic before generating the quiz.")
