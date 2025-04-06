import streamlit as st
import base64

# Page setup
st.set_page_config(page_title="Privacy Toolkit", layout="wide")

# Styling
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Georgia', serif;
        }

        .typewriter {
            font-size: 2.75em;
            color: #002145;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #002145;
            width: 0;
            animation: typing 3s steps(40, end) forwards, blink 1s infinite;
            margin-top: 1rem;
            margin-bottom: 1rem;
            text-align: center;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink {
            50% { border-color: transparent }
        }

        .section-box {
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            padding: 1rem;
            background-color: #ffffff;
            height: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# UofT Logo
logo_base64 = base64.b64encode(open("uoft_logo.png", "rb").read()).decode()
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='180'>
    </div>
    """,
    unsafe_allow_html=True
)

# Animated Title
st.markdown("<div class='typewriter'>Welcome to the Privacy Toolkit</div>", unsafe_allow_html=True)

# Intro
st.write("""
This toolkit helps newcomers to Canada understand privacy rights, protect their personal data,
avoid scams, and safely use digital services in their new life in Canada.
""")

st.markdown("---")
st.subheader("What You’ll Find Here")

# Section previews
cols = st.columns(3)
with cols[0]:
    st.markdown("<div class='section-box'><strong>Privacy Quiz</strong><br/>Test your knowledge with real-life scenarios and tips.</div>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<div class='section-box'><strong>Resource Library</strong><br/>Explore privacy laws, digital safety, and healthcare consent.</div>", unsafe_allow_html=True)
with cols[2]:
    st.markdown("<div class='section-box'><strong>About the Project</strong><br/>Learn who we are and what inspired this toolkit.</div>", unsafe_allow_html=True)

st.markdown("---")
st.info("Use the sidebar on the left to navigate between sections.")
