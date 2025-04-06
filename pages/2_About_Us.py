import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
        }
        .photo-names {
            text-align: center;
            margin-top: 0.5rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page content ---
st.title("About Us")

# --- Display photos using st.columns for layout ---
col1, col2 = st.columns(2)

with col1:
    st.image("Roxy.JPG", caption="Yanyue Zhang", width=250)

with col2:
    st.image("Megan.JPG", caption="Megan Luo", width=250)

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
