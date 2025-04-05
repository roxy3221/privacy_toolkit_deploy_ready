import streamlit as st

# --- Global Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
        }
        body {
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stRadio > div {
            background-color: #F0F6FB;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Privacy Knowledge Quiz")
st.write("Answer the following 10 questions to test your understanding of privacy in Canada:")

# --- Quiz Content ---
quiz = [
    {"question": "Is it safe to share your SIN over email?", 
     "options": ["Yes", "No"], "answer": "No"},
    
    {"question": "What does PIPEDA stand for?", 
     "options": ["Personal Information Protection and Electronic Documents Act", "Privacy Info Policy for E-Docs"], 
     "answer": "Personal Information Protection and Electronic Documents Act"},
    
    {"question": "You receive a call from CRA asking for immediate payment. What should you do?", 
     "options": ["Pay immediately", "Ignore and report the call"], "answer": "Ignore and report the call"},
    
    {"question": "Can companies collect personal data without consent?", 
     "options": ["Yes", "No"], "answer": "No"},
    
    {"question": "Which is considered sensitive personal information?", 
     "options": ["Favorite food", "Medical history"], "answer": "Medical history"},
    
    {"question": "How should you manage multiple strong passwords?", 
     "options": ["Use one strong password", "Use a password manager"], "answer": "Use a password manager"},
    
    {"question": "Which is a real Canadian fraud reporting agency?", 
     "options": ["Canada Digital Safety Board", "Canadian Anti-Fraud Centre"], "answer": "Canadian Anti-Fraud Centre"},
    
    {"question": "Is public Wi-Fi safe for banking?", 
     "options": ["Yes", "No"], "answer": "No"},
    
    {"question": "Can you ask a company to delete your data in Canada?", 
     "options": ["Yes", "No"], "answer": "Yes"},
    
    {"question": "What does 2FA help with?", 
     "options": ["Faster login", "Stronger security"], "answer": "Stronger security"}
]

# --- Quiz Form ---
user_answers = []
score = 0

with st.form("quiz_form"):
    all_answered = True
    for i, q in enumerate(quiz):
        user_answer = st.radio(
            f"{i+1}. {q['question']}",
            q["options"],
            index=None,
            key=f"question_{i}"
        )
        user_answers.append(user_answer)
        if user_answer is None:
            all_answered = False

    submitted = st.form_submit_button("Submit Answers")

# --- Evaluation ---
if submitted:
    if not all_answered:
        st.warning("Please answer all questions before submitting.")
    else:
        for i, q in enumerate(quiz):
            if user_answers[i] == q["answer"]:
                score += 1

        percent = (score / len(quiz)) * 100
        st.markdown(f"### Your Score: {score}/10 ({percent:.0f}%)")

        if percent < 50:
            st.warning("Consider reviewing key privacy concepts and reviewing our resources.")
        elif percent < 80:
            st.info("Good start! You have a solid understanding, but there’s more to explore.")
        else:
            st.success("Excellent! You have a strong grasp of privacy and safety in Canada.")
