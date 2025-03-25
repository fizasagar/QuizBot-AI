import streamlit as st
import random

# Custom CSS for Gradient Background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #C599B6, #E6B2BA, #FAD0C4);
        background-attachment: fixed;
        color: black; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Predefined Python quiz questions
quiz_data = [
    ("Which data structure is mutable?", ["Tuple", "List", "String", "Enum"], "List"),
    ("What keyword is used for defining a function?", ["func", "define", "lambda", "def"], "def"),
    ("Which of these data structures maintains order?", ["Set", "Dictionary", "List", "Enum"], "List"),
    ("How do you check if a key exists in a dictionary?", ["dict.has_key()", "if key in dict", "dict.exists()", "check key dict"], "if key in dict"),
    ("Which statement is used for decision-making?", ["if-else", "loop", "define", "class"], "if-else"),
    ("What is the default value returned by a function if no return statement is used?", ["0", "False", "None", "Empty String"], "None"),
    ("Which data structure stores unique values only?", ["List", "Set", "Dictionary", "Tuple"], "Set"),
    ("How do you define a tuple?", ["[1,2,3]", "(1,2,3)", "{1,2,3}", "'1,2,3'"], "(1,2,3)"),
    ("Which function is used to get user input?", ["get()", "read()", "input()", "scan()"], "input()"),
    ("Which module in Python is used for working with enumerations?", ["enum_class", "enumlib", "enum", "enumtypes"], "enum")
]

st.title("Ultimate Python Quiz 🎓📖")
st.write("Think you know Python? Take this 10-question challenge and prove your skills! Let's see if you can ace the Ultimate Python Quiz! 🧠💪")

# Initialize session state variables
if "score" not in st.session_state:
    st.session_state["score"] = 0
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0
if "quiz_over" not in st.session_state:
    st.session_state["quiz_over"] = False
if "answer_submitted" not in st.session_state:
    st.session_state["answer_submitted"] = False

# **Check if quiz is over before accessing quiz_data**
if st.session_state["question_index"] >= len(quiz_data):
    st.session_state["quiz_over"] = True

# Show quiz if not over
if not st.session_state["quiz_over"]:
    question, options, correct_answer = quiz_data[st.session_state["question_index"]]

    st.subheader(question)
    user_answer = st.radio("Choose your answer:", options)

    # Submit Answer Button
    if st.button("Submit Answer") and not st.session_state["answer_submitted"]:
        st.session_state["answer_submitted"] = True

        if user_answer == correct_answer:
            st.session_state["score"] += 1
            st.success("✅ Correct! Well done! 🎉")
        else:
            st.error(f"❌ Incorrect! The correct answer is: {correct_answer}")

    
    # Automatically move to next question after 2 seconds
    st.session_state["question_index"] += 1
    st.session_state["answer_submitted"] = False  # Reset for next question

    if st.session_state["question_index"] >= len(quiz_data):
        st.session_state["quiz_over"] = True
    else:
        st.rerun()  # Auto-refresh to show next question

# Show final score when quiz ends
if st.session_state["quiz_over"]:
    st.balloons()
    st.success(f"🎉 Quiz Completed! Your final score: {st.session_state['score']} / {len(quiz_data)}")
    if st.button("Restart Quiz"):
        st.session_state["question_index"] = 0
        st.session_state["score"] = 0
        st.session_state["quiz_over"] = False
        st.session_state["answer_submitted"] = False
        st.rerun()
