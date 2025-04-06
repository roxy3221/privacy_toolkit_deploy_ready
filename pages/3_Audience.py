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
        .goal-box, .audience-box {
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
This digital privacy toolkit is primarily designed for **newcomers to Canada**, including immigrants, refugees, international students, and other recently arrived residents.
""")

st.markdown("---")
st.markdown('<div class="section-title">3.1 Primary Audience: New Immigrants (Ages 18–55)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="audience-box">
<ul>
    <li>Often unfamiliar with Canadian digital laws & systems</li>
    <li>Vulnerable to scams, data misuse, and uninformed consent</li>
    <li>Regularly required to share sensitive info (e.g., immigration, jobs, banking)</li>
</ul>
<b>This toolkit empowers informed, confident digital decisions.</b>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">3.2 Secondary & Tertiary Audiences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="audience-box">
<ul>
    <li><b>Settlement workers & librarians:</b> Use the toolkit in digital literacy programs</li>
    <li><b>Educators & support staff:</b> Reinforce trust and understanding</li>
    <li><b>Policy makers & advocacy groups:</b> Promote broader inclusion and funding</li>
    <li><b>Mental health advocates:</b> Recognize digital safety as part of well-being</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-title">Toolkit Goals</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="goal-box">✅ Help newcomers understand their privacy rights in Canada</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">✅ Provide tools for secure communication and online navigation</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="goal-box">✅ Increase awareness of data collection and digital safety</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">✅ Reduce risks tied to fraud, discrimination, or misinformation</div>', unsafe_allow_html=True)
