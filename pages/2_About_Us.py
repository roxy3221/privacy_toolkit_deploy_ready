import streamlit as st

# --- Full-screen light blue background + styling ---
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
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            font-size: 2em;
            color: #002145;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page content ---
st.title("About Us")

# 📸 Smaller image with fixed width
st.image("about-us.png", width=600)

st.write("""
We are students from the University of Toronto’s Privacy Studies course — 
**Yanyue Zhang**, **Megan Luo**, and **Shazad Braich** — who created this digital toolkit
to support newcomers in Canada as they face real privacy challenges in daily life.
""")

st.header("Why We Made This")
st.write("""
Many newcomers are unaware of how their personal data can be used, shared, or misused in digital spaces.
This project is our way of sharing knowledge, promoting safety, and making privacy accessible.
""")

st.header("Contact Us")
st.write("""Email: [yanyue.zhang@mail.utoronto.ca](mailto:yanyue.zhang@mail.utoronto.ca)""")
