import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Audience Overview", layout="wide")

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        .main-container {
            max-width: 900px;
            margin: 3rem auto;
            padding: 2rem 2.5rem;
            background-color: white;
            border-radius: 14px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        }
        h1 {
            color: #002145;
            font-size: 2.3rem;
            margin-bottom: 1.2rem;
        }
        h2 {
            color: #002145;
            font-size: 1.4rem;
            margin-top: 2rem;
            margin-bottom: 0.8rem;
        }
        p, li {
            font-size: 1.02rem;
            line-height: 1.6;
        }
        ul {
            margin-top: 0.4rem;
            padding-left: 1.3rem;
        }
        .highlight {
            font-weight: bold;
            margin-top: 1rem;
        }
        .goal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        .goal-box {
            background-color: #f2f8fc;
            padding: 1rem 1.2rem;
            border-radius: 10px;
            border: 1px solid #d6e6f2;
        }
    </style>
""", unsafe_allow_html=True)

# --- Content Block ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Title & Intro ---
st.markdown("<h1>Audience Overview</h1>", unsafe_allow_html=True)
st.markdown("""
<p>This digital privacy toolkit is designed for <strong>newcomers to Canada</strong>, including immigrants, refugees, international students, and other recently arrived residents.</p>
""", unsafe_allow_html=True)

# --- Primary Audience ---
st.markdown("<h2>Primary Audience: New Immigrants (Ages 18–55)</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
    <li>More likely to face scams, data misuse, or lack of informed consent</li>
    <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
</ul>
<p class="highlight">The toolkit supports safer, more confident digital choices.</p>
""", unsafe_allow_html=True)

# --- Secondary Audiences ---
st.markdown("<h2>Secondary & Tertiary Audiences</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li><strong>Settlement workers & librarians:</strong> Use toolkit in digital literacy programs</li>
    <li><strong>Educators & support staff:</strong> Help reinforce understanding and trust</li>
    <li><strong>Policy makers & advocates:</strong> Promote inclusive, safer digital spaces</li>
    <li><strong>Mental health professionals:</strong> Recognize privacy as part of well-being</li>
</ul>
""", unsafe_allow_html=True)

# --- Toolkit Goals ---
st.markdown("<h2>Toolkit Goals</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="goal-grid">
  <div class="goal-box">Help newcomers understand their privacy rights in Canada</div>
  <div class="goal-box">Provide tools for secure communication and online navigation</div>
  <div class="goal-box">Increase awareness of data collection and digital safety</div>
  <div class="goal-box">Reduce risks tied to scams, discrimination, or misinformation</div>
</div>
""", unsafe_allow_html=True)

# --- Close Main Container ---
st.markdown("</div>", unsafe_allow_html=True)
