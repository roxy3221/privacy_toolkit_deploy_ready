import streamlit as st

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
        h1 {
            font-size: 2.75em;
            color: #002145;
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

st.title("About Us")
st.write("Any info about your team, contact, references, etc.")


import streamlit as st


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
    </style>
""", unsafe_allow_html=True)

import streamlit as st

st.title("About Us")

st.write("""We are students from the University of Toronto’s Privacy Studies course — **Yanyue Zhang**, **Megan Luo**, and **Shazad Braich** — who created this digital toolkit
to support newcomers in Canada as they face real privacy challenges in daily life.""")

st.header("Why We Made This")
st.write("""Many newcomers are unaware of how their personal data can be used, shared, or misused in digital spaces.
This project is our way of sharing knowledge, promoting safety, and making privacy accessible.""")

st.header("Literature Review")
st.markdown("""
- Brunton & Nissenbaum (2015). *Obfuscation: A User’s Guide for Privacy and Protest.*
- Maitland & Xu (2015). *Technology, risk and privacy in global contexts.*
- Kalhan (2013). *Immigration policing and surveillance.*
- Office of the Privacy Commissioner of Canada: [For Individuals](https://www.priv.gc.ca/en/for-individuals/)
""")
