import streamlit as st

# --- Global styling for full-screen light blue ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .resource-card {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
        }
        .resource-card a {
            text-decoration: none;
            font-weight: bold;
            color: #002145;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers,
unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status.
Below are curated topics that link to detailed resource pages.
""")

st.markdown("---")

# --- Clickable Link Cards (for deployed app) ---
base_url = "https://yourappname.streamlit.app"  # Replace with your deployed base URL

resources = [
    {"title": "A Newcomer's Guide", "path": "A_Newcomers_Guide"},
    {"title": "Staying Safe Online", "path": "Staying_Safe_Online"},
    {"title": "How Police Use Your Data", "path": "How_Police_Use_Data"},
    {"title": "Protecting Yourself from Scams", "path": "Protecting_Yourself"},
    {"title": "Understanding AI in Canada", "path": "Understanding_AI"},
]

for res in resources:
    st.markdown(f"""
    <div class='resource-card'>
        <a href='{base_url}/{res['path']}' target='_blank'>{res['title']}</a>
    </div>
    """, unsafe_allow_html=True)

# --- Additional External Resources List ---
st.markdown("---")
st.subheader("Additional Resources")

resources_list = [
    {
        "title": "Canadian Anti-Fraud Centre",
        "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
        "desc": "Info on fraud and identity theft. Report if you're a victim!"
    },
    {
        "title": "Data Detox Kit",
        "url": "https://datadetoxkit.org/en/home",
        "desc": "Guides about AI, digital privacy, wellbeing, misinformation, and more."
    },
    {
        "title": "Privacy in Public Spaces (Edwards & Urquhart, 2016)",
        "url": "https://doi.org/10.1093/ijlit/eaw007",
        "desc": "Understanding open-source and social media intelligence used by law enforcement."
    },
    {
        "title": "Canada's Anti-Spam Law (CASL)",
        "url": "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
        "desc": "Know five common types of spam and how to avoid them."
    },
    {
        "title": "Ensuring Your Privacy is Protected (IPC Ontario)",
        "url": "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
        "desc": "Tips to help you safeguard your privacy rights."
    },
    {
        "title": "Digital Equity Report for Newcomers",
        "url": "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
        "desc": "Challenges and solutions for digital access in immigrant services."
    },
    {
        "title": "Free Help for Newcomers (YMCA)",
        "url": "https://www.ymcagta.org/immigrant-services",
        "desc": "Language training and cultural orientation services."
    },
    {
        "title": "Meaningful Consent Guidelines (Canada)",
        "url": "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
        "desc": "How companies must explain privacy terms clearly."
    },
    {
        "title": "Guide on the Use of Generative AI",
        "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
        "desc": "Safe, ethical use of AI tools by organizations."
    },
    {
        "title": "Info Source: Personal Information Banks",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
        "desc": "How government agencies store and use your data."
    },
    {
        "title": "National Cyber Threat Assessment (2025–26)",
        "url": "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "desc": "Emerging threats like AI scams and supply chain attacks."
    },
    {
        "title": "Language Classes (Government Funded)",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
        "desc": "Government programs to help you learn English/French."
    },
    {
        "title": "Newcomer Fraud Vulnerability (News)",
        "url": "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
        "desc": "Survey: Newcomers are twice as likely to face fraud."
    },
    {
        "title": "Responsible AI (Learning Together)",
        "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
        "desc": "Teaches ethical AI use, especially avoiding racial bias in data."
    }
]

for res in resources_list:
    st.markdown(f"""<p style='margin-bottom: 0.3rem;'>
        <a href="{res['url']}" target="_blank" style="font-weight: bold; color: #002145;">{res['title']}</a><br>
        <span style="color: #333;">{res['desc']}</span>
    </p>""", unsafe_allow_html=True)
