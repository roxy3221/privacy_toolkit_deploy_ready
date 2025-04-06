import streamlit as st

# --- Global styling ---
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
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Staying Safe Online")
st.markdown("### 💡 Why Digital Safety Matters for Newcomers")

st.write("""
As a newcomer in Canada, you rely on the internet to access jobs, services, and connect with others. But not all digital spaces are safe. From fake emails to data leaks, being cautious online protects your identity and opportunities.
""")

# Numbered Steps — Checklist Style
st.markdown("### 🛡️ 5 Smart Steps to Stay Secure")

st.markdown('<div class="tip"><h4>1. Use Strong Passwords</h4><p>Mix letters, numbers, and symbols. Don’t reuse passwords across websites.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="tip"><h4>2. Avoid Public Wi-Fi for Banking</h4><p>Use mobile data or a secure home connection when checking bank accounts or sensitive apps.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="tip"><h4>3. Spot Scams</h4><p>Real government sites end in <code>.gc.ca</code>. IRCC will never call or email asking for money or passwords.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="tip"><h4>4. Keep Devices Updated</h4><p>Regular software updates fix security problems that hackers may use to break into your accounts.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="tip"><h4>5. Learn About Digital Safety</h4><p>Visit <a href="https://www.getcybersafe.gc.ca/en" target="_blank">Get Cyber Safe</a> for tips in many languages.</p></div>', unsafe_allow_html=True)

# Additional Resources
st.markdown("### Suggested Resources")
st.markdown("""
- **[National Cyber Threat Assessment 2025-2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)**  
  Overview of Canada's current and future digital threats.
  
- **[Digital Equity in Newcomer Services – Peel Region](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)**  
  Highlights access issues newcomers face and offers digital inclusion recommendations.
""")
