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


st.title("Audience Overview")

st.write("""
This digital privacy toolkit is designed for **newcomers to Canada** — including immigrants, refugees, international students, and other newly arrived residents.
We understand that settling in a new country comes with unique challenges, especially when navigating online services, legal systems, and digital safety.
""")

st.markdown("---")
st.header("Why This Matters")

st.write("""
Newcomers are more vulnerable to:
- **Scams** targeting people unfamiliar with Canadian systems
- **Language barriers** that affect healthcare, legal consent, or job applications
- **Overexposure of personal information** through forms, apps, or public networks
- **Digital surveillance** or misinformation that may not be easy to detect

This toolkit provides trustworthy information in accessible language to help you take control of your digital life in Canada.
""")

st.markdown("---")
st.header("Toolkit Goals")

cols = st.columns(2)
cols[0].write("✅ Help newcomers understand their privacy rights in Canada")
cols[0].write("✅ Provide tools for secure communication and online navigation")
cols[1].write("✅ Increase awareness of data collection and digital safety")
cols[1].write("✅ Reduce risks tied to fraud, discrimination, or misinformation")
