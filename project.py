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
    ("Which data structure is mutable?", ["List", "Tuple", "String", "Enum"], "List"),
    ("What keyword is used for defining a function?", ["def", "func", "define", "lambda"], "def"),
    ("Which of these data structures maintains order?", ["Set", "Dictionary", "List", "Enum"], "List"),
    ("How do you check if a key exists in a dictionary?", ["if key in dict", "dict.has_key()", "dict.exists()", "check key dict"], "if key in dict"),
    ("Which statement is used for decision-making?", ["if-else", "loop", "define", "class"], "if-else"),
    ("What is the default value returned by a function if no return statement is used?", ["None", "0", "False", "Empty String"], "None"),
    ("Which data structure stores unique values only?", ["List", "Set", "Dictionary", "Tuple"], "Set"),
    ("How do you define a tuple?", ["(1,2,3)", "[1,2,3]", "{1,2,3}", "'1,2,3'"], "(1,2,3)"),
    ("Which function is used to get user input?", ["input()", "get()", "read()", "scan()"], "input()"),
    ("Which module in Python is used for working with enumerations?", ["enum", "enum_class", "enumlib", "enumtypes"], "enum")
]

st.title("QuizBot AI 🤖 - Python Edition")
st.write("Test your Python skills with an interactive quiz!")

# Generate a random question
if "question" not in st.session_state:
    if st.button("Generate Quiz"):
        question, options, correct_answer = random.choice(quiz_data)
        st.session_state["question"] = question
        st.session_state["options"] = options
        st.session_state["correct_answer"] = correct_answer
        st.session_state["user_answer"] = None

# Display the quiz if a question is generated
if "question" in st.session_state:
    st.subheader(st.session_state["question"])
    st.session_state["user_answer"] = st.radio("Choose your answer:", st.session_state["options"], key="quiz_options")

    # Submit button
    if st.button("Submit Answer"):
        if st.session_state["user_answer"]:
            if st.session_state["user_answer"] == st.session_state["correct_answer"]:
                st.success("✅ Correct! Well done! 🎉")
            else:
                st.error(f"❌ Incorrect! The correct answer is: {st.session_state['correct_answer']}")
            
            # Reset for new question
            st.session_state.pop("question")
        else:
            st.warning("Please select an answer before submitting!")
