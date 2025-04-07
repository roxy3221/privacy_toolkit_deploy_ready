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
        h1 {
            color: #002145;
            font-size: 2.3rem;
            margin: 2rem auto 1.2rem auto;
            text-align: center;
        }
        h2 {
            color: #002145;
            font-size: 1.4rem;
            margin-bottom: 0.8rem;
            text-align: center;
        }
        p, li {
            font-size: 1.05rem;
            line-height: 1.6;
        }
        ul {
            margin-top: 0.4rem;
            padding-left: 1.3rem;
            text-align: left;
        }
        .highlight {
            font-weight: bold;
            margin-top: 1rem;
            text-align: center;
        }
        .audience-card {
            max-width: 800px;
            margin: 1.5rem auto;
            background-color: white;
            padding: 2rem 2.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            text-align: center;
        }
        .goal-boxes {
            max-width: 900px;
            margin: 1rem auto 2rem auto;
            padding: 0 1rem;
        }
        .goal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }
        .goal-item {
            background-color: #dceaf4;
            padding: 1rem 1.2rem;
            border-radius: 10px;
            border: 1px solid #c5dbe9;
        }
    </style>
""", unsafe_allow_html=True)

# --- Top Title ---
st.markdown("<h1>Audience Overview</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; max-width: 750px; margin: auto;'>This digital privacy toolkit is designed for <strong>newcomers to Canada</strong>, including immigrants, refugees, international students, and other recently arrived residents.</p>
""", unsafe_allow_html=True)

# --- Primary Audience Card ---
st.markdown('<div class="audience-card">', unsafe_allow_html=True)
st.markdown("<h2>Primary Audience</h2>", unsafe_allow_html=True)
st.markdown("""
<p><strong>New Immigrants (Ages 18–55)</strong></p>
<ul>
    <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
    <li>More likely to face scams, data misuse, or lack of informed consent</li>
    <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
</ul>
<p class="highlight">The toolkit supports safer, more confident digital choices.</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Secondary Audience Card ---
st.markdown('<div class="audience-card">', unsafe_allow_html=True)
st.markdown("<h2>Secondary & Tertiary Audiences</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li><strong>Settlement workers & librarians:</strong> Use toolkit in digital literacy programs</li>
    <li><strong>Educators & support staff:</strong> Help reinforce understanding and trust</li>
    <li><strong>Policy makers & advocates:</strong> Promote inclusive, safer digital spaces</li>
    <li><strong>Mental health professionals:</strong> Recognize privacy as part of well-being</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Toolkit Goals Section ---
st.markdown('<div class="goal-boxes">', unsafe_allow_html=True)
st.markdown("<h2>Toolkit Goals</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="goal-grid">
  <div class="goal-item">Help newcomers understand their privacy rights in Canada</div>
  <div class="goal-item">Provide tools for secure communication and online navigation</div>
  <div class="goal-item">Increase awareness of data collection and digital safety</div>
  <div class="goal-item">Reduce risks tied to scams, discrimination, or misinformation</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
