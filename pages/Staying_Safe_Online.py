import streamlit as st

# Set page config
st.set_page_config(page_title="Staying Safe Online", layout="wide")

# Global styling
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        .card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 2rem;
        }
        .title {
            font-size: 2.1rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .section-header {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        ul {
            padding-left: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<div class='title'>Staying Safe Online</div>", unsafe_allow_html=True)
st.write("Cybersecurity and digital equity are critical for newcomers navigating life in Canada.")

# Row of 2 side-by-side cards
col1, col2 = st.columns(2)

# Card 1: Key Risks
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Key Risks")
    st.markdown("""
    - **Unsecured networks:** Public Wi-Fi can expose your personal data.  
    - **Fake websites/emails:** Scammers may pose as IRCC or banks.  
    - **Data leaks:** Poorly secured apps may expose your info.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Card 2: Digital Equity
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Digital Equity & Inclusion")
    st.markdown("""
    **Digital Equity** means everyone has access to key technology and internet.  
    **Digital Inclusion** ensures that disadvantaged communities — like newcomers — can use digital services safely.

    **Why This Matters:**  
    - Missing job opportunities  
    - Losing immigration updates  
    - Not accessing online healthcare  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Spacer
st.write("")

# Full-width Card: Protection Steps
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### How to Protect Yourself")
st.markdown("""
- **Use Strong Passwords:** Mix letters, numbers, and symbols (e.g., Sunshine2023!).  
- **Avoid Public Wi-Fi:** Don’t check banking or share info on open networks.  
- **Spot Scams:** IRCC will never email or call asking for money or passwords.  
- **Keep Software Updated:** Regular updates prevent hacking.  
- **Learn More:** Explore [Get Cyber Safe](https://www.getcybersafe.gc.ca/en) for multilingual tips.  
""")
st.markdown("</div>", unsafe_allow_html=True)
