import streamlit as st

# --- Global styling for full-screen light blue ---
st.markdown("""
    <style>
        /* Make entire screen light blue */
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
        }
        /* Use Georgia font */
        body {
            font-family: 'Georgia', serif;
        }
        /* Optional container padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        /* Heading styling */
        h1 {
            font-size: 2em;
            color: #002145;
        }
    </style>
""", unsafe_allow_html=True)

st.title("About Us")

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
