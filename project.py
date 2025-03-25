import streamlit as st
import openai

# OpenAI API Key (Replace with your actual API key)
openai.api_key = "your_openai_api_key"

def get_quiz_question(topic):
    """Generate a multiple-choice quiz question from AI."""
    prompt = f"Generate a multiple-choaice question about {topic} with four options and the correct answer. Format it as: Question, Option A, Option B, Option C, Option D, Correct Option."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].split("\n")

st.title("QuizBot AI 🤖")

topic = st.text_input("Kis topic pe quiz chahiye? (e.g., Python, Science, History)")

if st.button("Generate Quiz"):
    if topic:
        quiz_data = get_quiz_question(topic)
        if len(quiz_data) == 6:
            st.session_state["question"] = quiz_data[0]
            st.session_state["options"] = quiz_data[1:5]
            st.session_state["correct_answer"] = quiz_data[5].split(": ")[1]
            st.radio("Select the correct answer:", st.session_state["options"], key="user_answer")
        else:
            st.error("AI se sahi format mein question nahi mila. Dobara try karo!")
    else:
        st.error("Pehle ek topic likho!")

if st.button("Submit Answer"):
    if "question" in st.session_state and "user_answer" in st.session_state:
        if st.session_state["user_answer"] == st.session_state["correct_answer"]:
            st.success("✅ Bilkul sahi jawab! Great job! 🎉")
        else:
            st.error(f"❌ Galat jawab! Sahi jawab: {st.session_state['correct_answer']}")
    else:
        st.error("Pehle question generate kro aur answer select kro!")
