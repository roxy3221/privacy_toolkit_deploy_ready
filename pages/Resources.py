import streamlit as st

# --- Global styling for full-screen light blue ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
            font-family: 'Georgia', serif;
            color: black;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers,
unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status.
Below are tips to help you protect your privacy and a list of useful resources to explore.
""")

st.markdown("---")

# --- Dictionary of 5 topics ---
if "selected_topic" not in st.session_state:
    st.session_state["selected_topic"] = None

topics = {
    "A Newcomer's Guide": {
        "title": "A Newcomer's Guide to Healthcare, Privacy, and Jobs in Canada",
        "problem": "The Problem with Language Barriers",
        "description": """
People who don’t speak English or French well may get worse healthcare. 
When doctors and patients can’t understand each other, it can lead to mistakes. 
For example, a patient’s private health details might be shared with the wrong person, 
or a patient might agree to a treatment they don’t fully understand.
""",
        "resource": {
            "title": "Language Barriers in Access to Health Care",
            "desc": "Explains how language gaps affect care quality and lists solutions like interpreter training.",
            "url": "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html"
        }
    },
    "Staying Safe Online": {
        "title": "Staying Safe Online",
        "problem": "Recognizing Online Threats",
        "description": """
From phishing emails to fake websites, digital threats are common.
Learn how to protect your identity while accessing services online.
""",
        "resource": {
            "title": "Get Cyber Safe Guide",
            "desc": "Canada’s official guide for protecting yourself online from scams, fraud, and malware.",
            "url": "https://www.getcybersafe.gc.ca/en"
        }
    },
    "How Police Use Your Data": {
        "title": "How Police Use Your Personal Data in Canada",
        "problem": "Surveillance and Social Media Monitoring",
        "description": """
Immigration and police services may use social media activity and other digital data to monitor individuals.
Understanding your rights and what you share online is key.
""",
        "resource": {
            "title": "Surveillance & Social Media Intelligence",
            "desc": "Journal article exploring how law enforcement accesses and uses social media data.",
            "url": "https://doi.org/10.1093/ijlit/eaw007"
        }
    },
    "Protecting Yourself from Scams": {
        "title": "Protecting Yourself from Scams",
        "problem": "Common Scams Targeting Newcomers",
        "description": """
Scammers often impersonate government agencies like CRA or IRCC, demanding payments or threatening deportation.
Know how to detect and avoid these.
""",
        "resource": {
            "title": "Canadian Anti-Fraud Centre",
            "desc": "Learn how to spot scams and report them directly to Canada’s official anti-fraud agency.",
            "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm"
        }
    },
    "Understanding AI in Canada": {
        "title": "Understanding AI and Digital Rights in Canada",
        "problem": "Bias and Data Use in Automated Systems",
        "description": """
AI systems used in hiring, policing, or immigration decisions can reflect biases.
It's important to understand how AI can affect your data and opportunities.
""",
        "resource": {
            "title": "Responsible AI Guidelines (Canada)",
            "desc": "Outlines how AI should be developed and used fairly and transparently.",
            "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence"
        }
    }
}

st.subheader("Explore Topics")

cols = st.columns(3)
topic_names = list(topics.keys())

for i, name in enumerate(topic_names):
    if cols[i % 3].button(name):
        st.session_state["selected_topic"] = name

st.markdown("---")

if st.session_state["selected_topic"]:
    content = topics[st.session_state["selected_topic"]]
    st.subheader(content["title"])
    st.markdown(f"**{content['problem']}**")
    st.write(content["description"])

    st.markdown("#### Suggested Resource")
    st.markdown(f"**[{content['resource']['title']}]({content['resource']['url']})**")
    st.write(content["resource"]["desc"])

# --- Additional Resources section ---
st.markdown("---")
st.subheader("Additional Useful Resources")

extra_links = [
    (
        "Data Detox Kit",
        "https://datadetoxkit.org/en/home",
        "Guides about AI, digital privacy, security, health data, and more."
    ),
    (
        "Canada’s Anti-Spam Legislation (CASL)",
        "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
        "Understand five common spam types and how to avoid them."
    ),
    (
        "Ensuring Your Privacy is Protected",
        "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
        "Ways to help you safeguard your privacy."
    ),
    (
        "Digital Equity in Settlement Services",
        "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
        "Challenges and solutions for newcomers’ access to digital tools."
    ),
    (
        "YMCA Immigrant Services",
        "https://www.ymcagta.org/immigrant-services",
        "Offers free help with language, job searching, and more."
    ),
    (
        "Consent Guidelines (OPC)",
        "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
        "Organizations must ensure you truly understand data practices."
    ),
    (
        "Guide on the Use of Generative AI",
        "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
        "Ethical guidelines for AI usage, protecting people's privacy."
    ),
    (
        "Info Source: Personal Information Banks",
        "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
        "How government agencies store and use personal data."
    ),
    (
        "National Cyber Threat Assessment 2025-2026",
        "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "Outlines emerging cyber risks like AI scams or supply chain attacks."
    ),
    (
        "Newcomers & Fraud Risk Survey",
        "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
        "Highlights higher fraud targeting among newcomers."
    )
]

for title, link, desc in extra_links:
    st.markdown(f"- **[{title}]({link})** — {desc}")
