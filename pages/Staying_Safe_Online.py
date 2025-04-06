import streamlit as st

# Page setup
st.set_page_config(page_title="Staying Safe Online", layout="wide")

# Global styles
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
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 0.7rem;
        }
        ul {
            padding-left: 1.2rem;
        }
        a {
            text-decoration: none;
            color: #003366;
            font-weight: 500;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>Staying Safe Online</div>", unsafe_allow_html=True)
st.write("Cybersecurity and digital equity are critical for newcomers navigating life in Canada.")

# --- Section 1: Key Risks + Digital Equity ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Key Risks")
    st.markdown("""
- **Unsecured networks:** Public Wi-Fi can expose your personal data.  
- **Fake websites/emails:** Scammers may pose as IRCC or banks.  
- **Data leaks:** Poorly secured apps may expose your info.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Digital Equity & Inclusion")
    st.markdown("""
**Digital Equity** means everyone has access to key technology and internet.  
**Digital Inclusion** ensures disadvantaged communities — like newcomers — can use digital services safely.

**Why This Matters:**  
- Missing job opportunities  
- Losing immigration updates  
- Not accessing online healthcare  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Section 2: Protection Tips ---
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

# --- Section 3: Suggested Resources ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### Suggested Resources")
st.markdown("""
- [**National Cyber Threat Assessment 2025–2026**](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)  
  Understand emerging cyber threats like AI-driven scams and supply chain attacks.

- [**Exploring Digital Equity for Newcomer Services (Peel Region)**](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)  
  Research on challenges faced by newcomers in accessing digital tools, with hybrid service recommendations.

- [**Get Cyber Safe – Canada’s Digital Safety Hub**](https://www.getcybersafe.gc.ca/en)  
  Tips, guides, and checklists to help individuals stay safe online — available in multiple languages.
""")
st.markdown("</div>", unsafe_allow_html=True)
