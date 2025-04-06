import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        .block-container {
            background-color: #F0F6FB;
            padding-top: 2rem;
            padding-bottom: 2rem;
            font-family: 'Georgia', serif;
        }
        .card {
            background-color: white;
            border-radius: 12px;
            padding: 1.2rem 1.5rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        }
        .card h4 {
            margin-top: 0;
            font-size: 1.1rem;
        }
        .card p, .card li {
            font-size: 0.88rem;
            line-height: 1.5;
        }
        ul {
            padding-left: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Staying Safe Online")

# --- Card 1 ---
st.markdown("""
<div class="card">
    <h4>Why Digital Safety Matters for Newcomers</h4>
    <p>Canada faces growing cyber threats, like hackers attacking banks, hospitals, or government services. These attacks can disrupt daily life—for example, freezing online banking or shutting down hospital systems.</p>
    <p>As a newcomer, you may rely heavily on the internet for jobs, healthcare, and staying connected. But not all websites or apps are safe, and your personal data (like passwords or bank details) could be stolen if you’re not careful.</p>
</div>
""", unsafe_allow_html=True)

# --- Card 2 ---
st.markdown("""
<div class="card">
    <h4>Key Risks</h4>
    <ul>
        <li><strong>Unsecured networks:</strong> Public Wi-Fi (e.g., in cafes) can let hackers steal your data.</li>
        <li><strong>Fake websites/emails:</strong> Scammers might pretend to be the government (like IRCC) to trick you into sharing personal info.</li>
        <li><strong>Data leaks:</strong> Apps or services you use might accidentally expose your private information.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- Card 3 ---
st.markdown("""
<div class="card">
    <h4>Digital Equity & Inclusion: What It Means for You</h4>
    <p><strong>Digital Equity</strong> means everyone can access technology needed for jobs, education, and services.</p>
    <p><strong>Digital Inclusion</strong> means ensuring even disadvantaged groups (like newcomers) can use the internet safely.</p>
    <p><strong>Why This Matters:</strong></p>
    <ul>
        <li>Job opportunities posted online</li>
        <li>Important updates about your immigration status</li>
        <li>Virtual healthcare appointments</li>
    </ul>
</div>
""", unsafe_allow_html=True)

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
