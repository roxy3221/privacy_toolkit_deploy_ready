import streamlit as st
import base64

# Page setup
st.set_page_config(page_title="Privacy Toolkit", layout="wide")

# Styling
st.markdown("""
    <style>
        body {
            font-family: 'Georgia', serif;
            background-color: #F0F6FB;
        }
        .block-container {
            background-color: #F0F6FB;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            font-size: 2.75em;
            color: #002145;
            padding-bottom: 0.2em;
            margin-bottom: 0.5em;
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

# Base64 embed of logo (must match filename)
logo_base64 = base64.b64encode(open("uoft_logo.png", "rb").read()).decode()
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='180'>
    </div>
    """,
    unsafe_allow_html=True
)

# Title and intro
st.markdown("<h1>Welcome to the Privacy Toolkit</h1>", unsafe_allow_html=True)

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
