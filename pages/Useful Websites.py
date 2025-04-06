import streamlit as st

# --- Minimalist Global Styling (light blue, no underline) ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            color: black !important;
            font-family: 'Georgia', serif;
            margin: 0; 
            padding: 0;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        a {
            text-decoration: none !important;
            color: black !important;
        }
        a:hover {
            text-decoration: underline !important;
        }
        .resource-card {
            background-color: #ffffff;
            border: 1px solid #d6d6d6;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .resource-card:hover {
            border-color: #999999;
        }
        .resource-title {
            font-size: 1rem;
            font-weight: bold;
            margin-bottom: 0.3rem;
        }
        .resource-desc {
            font-size: 0.9rem;
            line-height: 1.4;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Title & Intro ---
st.title("Useful Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers 
because of language barriers, unfamiliarity with local systems, or urgent needs like finding jobs 
or settling immigration status. Below are tips to help you protect your privacy and a list of useful resources to explore.
""")

st.markdown("---")

# -- Resource Data: Title, URL, Description
resources = [
    {
        "title": "Canadian Anti-Fraud Centre",
        "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
        "desc": """The Canadian Anti-Fraud Centre collects information on fraud and identity theft. 
We provide information on past and current scams affecting Canadians. If you think 
you're a victim of fraud, report it!"""
    },
    {
        "title": "Data Detox Kit",
        "url": "https://datadetoxkit.org/en/home",
        "desc": """Explore guides about Artificial Intelligence, digital privacy, security, wellbeing, 
misinformation, health data, and tech and the environment."""
    },
    {
        "title": "Edwards, L., & Urquhart, L. (2016). Privacy in Public Spaces",
        "url": "https://doi.org/10.1093/ijlit/eaw007",
        "desc": """Discusses expectations of privacy in social media intelligence (SOCMINT) 
and open source intelligence (OSINT) used by law enforcement."""
    },
    {
        "title": "Enforcing Canada’s Anti-Spam Legislation (CASL)",
        "url": "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
        "desc": "Understand five common types of spam and scam."
    },
    {
        "title": "Ensuring your privacy is protected",
        "url": "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
        "desc": "Ways to help you protect your privacy."
    },
    {
        "title": "Exploring Digital Equity for Newcomer Services",
        "url": "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
        "desc": """Highlights challenges newcomers face in accessing digital tools and 
recommends hybrid (online + in-person) services."""
    },
    {
        "title": "Free Help For Newcomers",
        "url": "https://www.ymcagta.org/immigrant-services",
        "desc": """Offers language training and cultural orientation to ease integration."""
    },
    {
        "title": "Guidelines for obtaining meaningful consent",
        "url": "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
        "desc": """Details how organizations must simplify privacy information to ensure 
people truly understand what they’re agreeing to."""
    },
    {
        "title": "Guide on the use of generative artificial intelligence",
        "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
        "desc": """Learn about how to use AI tools while protecting people’s privacy."""
    },
    {
        "title": "Info Source: Personal Information Banks",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
        "desc": "Explains how government agencies store and use data like biometrics."
    },
    {
        "title": "International Journal of Law & Info Tech",
        "url": "https://doi-org.myaccess.library.utoronto.ca/10.1093/ijlit/eaw007",
        "desc": """Understanding data surveillance and data profiling in modern contexts."""
    },
    {
        "title": "Language Barriers in Access to Health Care",
        "url": "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html",
        "desc": """Explains how language gaps affect care quality and lists solutions like 
interpreter training."""
    },
    {
        "title": "Language classes funded by the Government of Canada",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
        "desc": """Government-funded programs to help newcomers learn English/French."""
    },
    {
        "title": "Learning Together for Responsible Artificial Intelligence",
        "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
        "desc": """Teaches how to use AI ethically, like avoiding data that reflects racial biases."""
    },
    {
        "title": "National Cyber Threat Assessment 2025-2026",
        "url": "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "desc": """Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams."""
    },
    {
        "title": "New to Canada? Beware, you’re twice as likely to become a fraud victim",
        "url": "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
        "desc": "What are the most reported types of fraud?"
    }
]

# --- Render each resource as a simple card
for r in resources:
    st.markdown(f"""
    <div class="resource-card">
        <div class="resource-title"><a href="{r['url']}" target="_blank">{r['title']}</a></div>
        <div class="resource-desc">{r['desc']}</div>
    </div>
    """, unsafe_allow_html=True)
