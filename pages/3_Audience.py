import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }

        .section-title {
            font-size: 2rem;
            font-weight: bold;
            margin-top: 2rem;
            color: #1a2e3b;
        }

        .description {
            font-size: 1.05rem;
            color: #444;
            margin-bottom: 1.8rem;
        }

        .big-box {
            background-color: white;
            padding: 2rem 2.2rem;
            border-radius: 12px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.06);
            margin-bottom: 2rem;
        }

        .big-box h3 {
            margin-top: 1.5rem;
            font-size: 1.2rem;
            color: #002145;
        }

        .big-box ul {
            padding-left: 1.3rem;
        }

        .big-box li {
            margin-bottom: 0.5rem;
        }

        .emphasis {
            font-weight: bold;
            margin-top: 0.6rem;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# --- Content ---
st.markdown('<div class="section-title">Audience Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="description">This digital privacy toolkit is designed for <b>newcomers to Canada</b>, including immigrants, refugees, international students, and newly arrived residents.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="big-box">
    <h3>Primary Audience: New Immigrants (Ages 18–55)</h3>
    <ul>
        <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
        <li>More likely to face scams, data misuse, or lack of informed consent</li>
        <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
    </ul>
    <span class="emphasis">The toolkit supports safer, more confident digital choices.</span>

    <h3>Secondary & Tertiary Audiences</h3>
    <ul>
        <li><b>Settlement workers & librarians:</b> Use toolkit in digital literacy programs</li>
        <li><b>Educators & support staff:</b> Help reinforce understanding and trust</li>
        <li><b>Policy makers & advocates:</b> Promote inclusive, safer digital spaces</li>
        <li><b>Mental health professionals:</b> Recognize privacy as part of well-being</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Toolkit Goals</div>', unsafe_allow_html=True)
st.markdown("""
<div class="big-box">
    <ul>
        <li>Help newcomers understand their privacy rights in Canada</li>
        <li>Provide tools for secure communication and online navigation</li>
        <li>Raise awareness about data collection and digital safety</li>
        <li>Reduce risks tied to scams, discrimination, or misinformation</li>
    </ul>
</div>
""", unsafe_allow_html=True)
