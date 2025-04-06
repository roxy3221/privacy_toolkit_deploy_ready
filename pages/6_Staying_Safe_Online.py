import streamlit as st

# --- Global Styling ---
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
        .card {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .indented {
            margin-left: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Staying Safe Online")

# --- Expandable Sections ---
with st.expander("Why Digital Safety Matters for Newcomers", expanded=True):
    st.markdown("""
    Canada faces growing cyber threats, like hackers attacking banks, hospitals, or government services.
    These attacks can disrupt daily life—for example, freezing online banking or shutting down hospital systems.
    
    As a newcomer, you may rely heavily on the internet for jobs, healthcare, and staying connected.
    But not all websites or apps are safe, and your personal data (like passwords or bank details) could be stolen if you’re not careful.
    """)

with st.expander("Key Risks", expanded=False):
    st.markdown("""
    - **Unsecured networks**: Public Wi-Fi (e.g., in cafes) can let hackers steal your data.  
    - **Fake websites/emails**: Scammers might pretend to be the government (like IRCC) to trick you into sharing personal info.  
    - **Data leaks**: Apps or services you use might accidentally expose your private information.
    """)

# --- Digital Equity Section ---
st.markdown('<div class="section-title">Digital Equity & Inclusion: What It Means for You</div>', unsafe_allow_html=True)
st.write("""
Digital Equity means everyone can access technology needed for jobs, education, and services.  
Digital Inclusion means ensuring even disadvantaged groups (like newcomers) can use the internet safely.
""")

st.markdown("**Why This Matters:**")
st.markdown("""
- Job opportunities posted online  
- Important updates about your immigration status  
- Virtual healthcare appointments  
""")

# --- Protect Yourself Section ---
st.markdown('<div class="section-title">How to Protect Yourself</div>', unsafe_allow_html=True)

with st.expander("1. Use Strong Passwords"):
    st.markdown('<div class="card">Create passwords with letters, numbers, and symbols (e.g., Sunshine2023!).<br>Never reuse passwords for multiple accounts.</div>', unsafe_allow_html=True)

with st.expander("2. Avoid Public Wi-Fi for Sensitive Tasks"):
    st.markdown('<div class="card">Don’t check bank accounts or share personal info on café/airport Wi-Fi.<br>Use mobile data instead.</div>', unsafe_allow_html=True)

with st.expander("3. Spot Scams"):
    st.markdown('<div class="card">Government agencies (like IRCC) will never call or email asking for money or passwords.<br>Check website URLs carefully — scammers use fake links like IRCC-service.ca (real site: Canada.ca).</div>', unsafe_allow_html=True)

with st.expander("4. Keep Software Updated"):
    st.markdown('<div class="card">Update your phone, computer, and apps regularly to fix security gaps.</div>', unsafe_allow_html=True)

with st.expander("5. Learn About Digital Safety"):
    st.markdown('<div class="card">Visit <a href="https://www.getcybersafe.gc.ca/en" target="_blank">Get Cyber Safe</a> for official guidance in multiple languages.</div>', unsafe_allow_html=True)

# --- Suggested Resources ---
st.markdown('<div class="section-title">📚 Suggested Resources</div>', unsafe_allow_html=True)
st.markdown("""
- **[National Cyber Threat Assessment 2025–2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)**  
  Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams.

- **[Exploring Digital Equity for Newcomer Services](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)**  
  Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services.
""")
