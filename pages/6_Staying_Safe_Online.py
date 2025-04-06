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

# 加粗加大标题：How to Protect Yourself
st.markdown("""
    <h3 style='margin-bottom: 1rem; font-size: 1.6rem;'>How to Protect Yourself</h3>
""", unsafe_allow_html=True)

# 保留原本的折叠卡片（Accordion）结构
with st.expander("Use Strong Passwords"):
    st.write("Create passwords with letters, numbers, and symbols (e.g., Sunshine2023!).")
    st.write("Never reuse passwords for multiple accounts.")

with st.expander("Avoid Public Wi-Fi for Sensitive Tasks"):
    st.write("Don’t check bank accounts or share personal info on café/airport Wi-Fi. Use mobile data instead.")

with st.expander("Spot Scams"):
    st.write("Government agencies (like IRCC) will never call or email asking for money or passwords.")
    st.write("Check website URLs: Scammers use fake links like IRCC-service.ca (real site: Canada.ca).")

with st.expander("Keep Software Updated"):
    st.write("Update your phone, computer, and apps regularly to fix security gaps.")

with st.expander("Learn About Digital Safety"):
    st.write("Visit Get Cyber Safe for tips in multiple languages.")

# 加大标题：Suggested Resources
st.markdown("""
    <h3 style='margin-top: 2rem; font-size: 1.6rem;'>Suggested Resources</h3>
""", unsafe_allow_html=True)

# 资源列表（保持原样或根据你需要修改）
st.markdown("""
- [**National Cyber Threat Assessment 2025–2026**](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)  
  Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams.

- [**Exploring Digital Equity for Newcomer Services**](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)  
  Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services.
""")
