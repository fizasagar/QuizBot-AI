import streamlit as st
import time

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
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "quiz_over" not in st.session_state:
    st.session_state.quiz_over = False
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

# Check if quiz is over
if st.session_state.question_index >= len(quiz_data):
    st.session_state.quiz_over = True

# Show quiz if not over
if not st.session_state.quiz_over:
    question, options, correct_answer = quiz_data[st.session_state.question_index]
    
    st.subheader(f"Question {st.session_state.question_index + 1}")
    st.write(question)
    
    # Only show radio and submit button if feedback isn't being shown
    if not st.session_state.show_feedback:
        user_answer = st.radio("Choose your answer:", options, key=f"q{st.session_state.question_index}")
        
        if st.button("Submit Answer"):
            st.session_state.show_feedback = True
            st.session_state.user_answer = user_answer
            st.session_state.correct_answer = correct_answer
            
            if user_answer == correct_answer:
                st.session_state.score += 1
            st.rerun()
    
    # Show feedback if submitted
    if st.session_state.show_feedback:
        if st.session_state.user_answer == st.session_state.correct_answer:
            st.success("✅ Correct! Well done! 🎉")
        else:
            st.error(f"❌ Incorrect! The correct answer is: {st.session_state.correct_answer}")
        
        # Automatically move to next question after delay
        time.sleep(2)
        st.session_state.question_index += 1
        st.session_state.show_feedback = False
        
        if st.session_state.question_index >= len(quiz_data):
            st.session_state.quiz_over = True
        st.rerun()

# Show final score when quiz ends
if st.session_state.quiz_over:
    st.balloons()
    st.success(f"🎉 Quiz Completed! Your final score: {st.session_state.score} / {len(quiz_data)}")
    if st.button("Restart Quiz"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.quiz_over = False
        st.session_state.show_feedback = False
        st.rerun()
