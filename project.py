import streamlit as st
import random

# Custom CSS for Gradient Background & Footer
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #C599B6, #E6B2BA, #FAD0C4);
        background-attachment: fixed;
        color: black; 
    }
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: black;
        font-weight: bold;
    }
    </style>
    <div class="footer">Crafted with ❤ & passion by Fiza Asif | © 2025</div>
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
    ("Which module in Python is used for working with enumerations?", ["enum", "enum_class", "enumlib", "enumtypes"], "enum")
]

st.title("Ultimate Python Quiz 🎓")
st.write("Think you know Python? 🧠 Take this 10-question challenge and prove your skills! 🎯 Let's see if you can ace the Ultimate Python Quiz! 🎓🔥")

# Initialize session state
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0
    st.session_state["score"] = 0
    st.session_state["quiz_questions"] = random.sample(quiz_data, 10)  # Pick 10 random questions

# Get the current question
if st.session_state["question_index"] < 10:
    question, options, correct_answer = st.session_state["quiz_questions"][st.session_state["question_index"]]
    
    st.subheader(f"Question {st.session_state['question_index'] + 1}: {question}")
    user_answer = st.radio("Choose your answer:", options, key=f"q{st.session_state['question_index']}")

    
  # Submit Answer Button
    if st.button("Submit Answer") and not st.session_state["answer_submitted"]:
        st.session_state["answer_submitted"] = True

        if user_answer == correct_answer:
            st.session_state["score"] += 1
            st.success("✅ Correct! Well done! 🎉")
        else:
            st.error(f"❌ Incorrect! The correct answer is: {correct_answer}")

    # Next Question Button (Only shows after answer is submitted)
    if st.session_state["answer_submitted"]:
        if st.button("Next Question"):
            st.session_state["question_index"] += 1
            st.session_state["answer_submitted"] = False  # Reset for next question
        
        # Move to next question
        st.session_state["question_index"] += 1
        st.rerun()

else:
    # Show final score
    st.subheader("Quiz Completed! 🎯")
    st.write(f"Your final score: **{st.session_state['score']} / 10**")
    st.balloons()

    # Reset quiz button
    if st.button("Restart Quiz"):
        st.session_state["question_index"] = 0
        st.session_state["score"] = 0
        st.session_state["quiz_questions"] = random.sample(quiz_data, 10)  # Reset with new random questions
        st.rerun()
