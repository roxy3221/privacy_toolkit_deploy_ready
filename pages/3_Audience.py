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
This digital privacy toolkit is designed for **newcomers to Canada**, including immigrants, refugees, international students, and other recently arrived residents.
""")

st.markdown("---")
st.markdown('<div class="section-title">Primary Audience: New Immigrants (Ages 18–55)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="audience-box">
<ul>
    <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
    <li>More likely to face scams, data misuse, or lack of informed consent</li>
    <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
</ul>
<b>The toolkit supports safer, more confident digital choices.</b>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Secondary & Tertiary Audiences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="audience-box">
<ul>
    <li><b>Settlement workers & librarians:</b> Use toolkit in digital literacy programs</li>
    <li><b>Educators & support staff:</b> Help reinforce understanding and trust</li>
    <li><b>Policy makers & advocates:</b> Support inclusive, safer digital spaces</li>
    <li><b>Mental health professionals:</b> Recognize privacy as part of well-being</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-title">Toolkit Goals</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="goal-box">Help newcomers understand privacy rights in Canada</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">Provide tools for safe digital communication</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="goal-box">Increase awareness of data safety and rights</div>', unsafe_allow_html=True)
    st.markdown('<div class="goal-box">Reduce risks of fraud, exclusion, and harm</div>', unsafe_allow_html=True)
