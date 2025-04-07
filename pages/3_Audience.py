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
        .subtitle {
            font-size: 1.05rem;
            color: #444;
            margin-bottom: 2rem;
        }
        .audience-section {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            margin-top: 1rem;
        }
        .audience-box {
            background-color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            flex: 1 1 45%;
            min-width: 280px;
        }
        .audience-box h3 {
            margin-top: 0;
            font-size: 1.2rem;
            color: #002145;
        }
        .audience-box ul {
            padding-left: 1.2rem;
            margin-top: 0.5rem;
        }
        .audience-box li {
            margin-bottom: 0.4rem;
        }
        .emphasis {
            font-weight: bold;
            margin-top: 0.5rem;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.markdown('<div class="section-title">Audience Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This digital privacy toolkit is designed for <b>newcomers to Canada</b>, including immigrants, refugees, international students, and newly arrived residents.</div>', unsafe_allow_html=True)

# --- Two-Column Audience Section ---
st.markdown('<div class="audience-section">', unsafe_allow_html=True)

# --- Primary Audience ---
st.markdown("""
    <div class="audience-box">
        <h3>Primary Audience: New Immigrants (Ages 18–55)</h3>
        <ul>
            <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
            <li>More likely to face scams, data misuse, or lack of informed consent</li>
            <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
        </ul>
        <span class="emphasis">The toolkit supports safer, more confident digital choices.</span>
    </div>
""", unsafe_allow_html=True)

# --- Secondary Audience ---
st.markdown("""
    <div class="audience-box">
        <h3>Secondary & Tertiary Audiences</h3>
        <ul>
            <li><b>Settlement workers & librarians:</b> Use toolkit in digital literacy programs</li>
            <li><b>Educators & support staff:</b> Help reinforce understanding and trust</li>
            <li><b>Policy makers & advocates:</b> Promote inclusive, safer digital spaces</li>
            <li><b>Mental health professionals:</b> Recognize privacy as part of well-being</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
