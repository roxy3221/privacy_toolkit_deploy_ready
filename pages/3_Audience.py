import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        .section-title {
            font-size: 1.6rem;
            font-weight: bold;
            margin-top: 2rem;
        }
        .goal-box {
            background-color: white;
            padding: 1rem 1.2rem;
            border-radius: 12px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.07);
            margin-bottom: 1rem;
        }
        .goal-list {
            margin-left: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Content ---
st.title("Audience Overview")

st.write("""
This digital privacy toolkit is designed for **newcomers to Canada** — including immigrants, refugees, international students, and other newly arrived residents.

We understand that settling in a new country comes with unique challenges, especially when navigating online services, legal systems, and digital safety.
""")

st.markdown("---")
st.markdown('<div class="section-title">Why This Matters</div>', unsafe_allow_html=True)

st.write("""
Newcomers are more vulnerable to:
- Scams targeting people unfamiliar with Canadian systems
- Language barriers that affect healthcare, legal consent, or job applications
- Overexposure of personal information through forms, apps, or public networks
- Digital surveillance or misinformation that may not be easy to detect

This toolkit provides trustworthy information in accessible language to help you take control of your digital life in Canada.
""")

st.markdown("---")
st.markdown('<div class="section-title">Toolkit Goals</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="goal-box">1.Help newcomers understand their privacy rights in Canada</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">2.Provide tools for secure communication and online navigation</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="goal-box">3.Increase awareness of data collection and digital safety</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">4.Reduce risks tied to fraud, discrimination, or misinformation</div>', unsafe_allow_html=True)
