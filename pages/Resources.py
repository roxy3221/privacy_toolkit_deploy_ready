import streamlit as st

# --- Global styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            color: black !important;
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers,
unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status.
Below are tips to help you protect your privacy and a list of useful resources to explore.
""")

st.markdown("---")

st.write("""
**Here you'll find subpages in the sidebar**:

- A Newcomer's Guide
- Staying Safe Online
- How Police Use Your Data
- Protecting Yourself from Scams
- Understanding AI in Canada
""")

st.markdown("""
**Pick the subpage you want from the sidebar** to view its details.
""")

st.markdown("---")
st.subheader("Additional General Resources")

links = [
    ("Canadian Anti-Fraud Centre", "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
     "Scam alerts, fraud reporting, and identity theft info."),
    ("Data Detox Kit", "https://datadetoxkit.org/en/home",
     "Guides on AI, digital privacy, security, health data, and more."),
    ("CASL – Anti-Spam Law", "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
     "How to recognize and report spam or phishing."),
    ("Ensuring Your Privacy Is Protected", "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
     "Tips to safeguard your data."),
    ("Digital Equity for Newcomers", "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
     "Challenges and solutions in digital access for immigrants."),
    ("YMCA: Help for Newcomers", "https://www.ymcagta.org/immigrant-services",
     "Free language training and cultural orientation."),
    ("Guide on the Use of Generative AI", "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
     "Ethical guidelines for using AI."),
    ("Info Source: Personal Information Banks", "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
     "How government agencies store and use personal data."),
    ("National Cyber Threat Assessment 2025-26", "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
     "Learn about emerging cyber threats in Canada."),
    ("Newcomer Fraud Risk Survey", "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
     "Survey: newcomers face 2x the risk of fraud.")
]

for title, url, desc in links:
    st.markdown(f"- **[{title}]({url})** — {desc}")
