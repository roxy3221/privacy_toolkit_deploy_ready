import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Staying Safe Online", layout="wide")

# --- Global Styles ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.06);
            margin-bottom: 2rem;
        }
        .tip {
            background-color: white;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-radius: 1rem;
            box-shadow: 0 0 8px rgba(0,0,0,0.05);
        }
        .tip h4 {
            margin-bottom: 0.5rem;
            color: #2c3e50;
        }
        .tip p {
            margin: 0.2rem 0 0.6rem;
        }
        .title {
            font-size: 2.1rem;
            font-weight: 700;
            color: #00274D;
            margin-bottom: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>Staying Safe Online</div>", unsafe_allow_html=True)
st.write("Cybersecurity and digital equity are critical for newcomers navigating life in Canada.")

# --- 2 Side-by-Side Cards: Risks + Inclusion ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Key Risks")
    st.markdown("""
- **Unsecured networks:** Public Wi-Fi (e.g., in cafes) can let hackers steal your data.  
- **Fake websites/emails:** Scammers might pretend to be the government (like IRCC).  
- **Data leaks:** Apps or services you use might accidentally expose your private info.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Digital Equity & Inclusion")
    st.markdown("""
**Digital Equity** means everyone can access the technology needed for jobs, education, and services.  
**Digital Inclusion** ensures even disadvantaged groups (like newcomers) can use the internet safely.

**Why This Matters:**  
- You might miss job opportunities posted online.  
- Lose important immigration updates.  
- Miss out on virtual healthcare appointments.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Step-by-Step Tips Section ---
st.markdown("### 5 Smart Steps to Stay Secure")

st.markdown('<div class="tip"><h4>1. Use Strong Passwords</h4><p>Mix letters, numbers, and symbols. Don’t reuse passwords across websites.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="tip"><h4>2. Avoid Public Wi-Fi for Banking</h4><p>Use mobile data or a secure home connection when checking bank accounts or sensitive apps.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="tip"><h4>3. Spot Scams</h4><p>Real government sites end in <code>.gc.ca</code>. IRCC will never call or email asking for money or passwords.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="tip"><h4>4. Keep Devices Updated</h4><p>Regular software updates fix security problems that hackers may use to break into your accounts.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="tip"><h4>5. Learn About Digital Safety</h4><p>Visit <a href="https://www.getcybersafe.gc.ca/en" target="_blank">Get Cyber Safe</a> for tips in many languages.</p></div>', unsafe_allow_html=True)

# --- Suggested Resources ---
st.markdown("### Suggested Resources")
st.markdown("""
- **[National Cyber Threat Assessment 2025–2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)**  
  Overview of Canada's current and future digital threats.
  
- **[Digital Equity in Newcomer Services – Peel Region](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)**  
  Research on challenges faced by newcomers in accessing digital tools and inclusion services.

- **[Get Cyber Safe – Canada’s Digital Safety Hub](https://www.getcybersafe.gc.ca/en)**  
  Government-approved tips, guides, and checklists to help individuals stay safe online.
""")
