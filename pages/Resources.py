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

# --- Interactive Topic Buttons ---
topics = {
    "A Newcomer's Guide": {
        "title": "A Newcomer's Guide to Healthcare, Privacy, and Jobs in Canada",
        "problem": "The Problem with Language Barriers",
        "description": "People who don’t speak English or French well may get worse healthcare. When doctors and patients can’t understand each other, it can lead to mistakes. For example, a patient’s private health details might be shared with the wrong person, or a patient might agree to a treatment they don’t fully understand.",
        "resource": {
            "title": "Language Barriers in Access to Health Care",
            "desc": "Explains how language gaps affect care quality and lists solutions like interpreter training.",
            "url": "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html"
        }
    },
    "Staying Safe Online": {
        "title": "Staying Safe Online",
        "problem": "Recognizing Online Threats",
        "description": "From phishing emails to fake websites, digital threats are common. Learn how to protect your identity while accessing services online.",
        "resource": {
            "title": "Get Cyber Safe Guide",
            "desc": "Canada’s official guide for protecting yourself online from scams, fraud, and malware.",
            "url": "https://www.getcybersafe.gc.ca/en"
        }
    },
    "How Police Use Your Data": {
        "title": "How Police Use Your Personal Data in Canada",
        "problem": "Surveillance and Social Media Monitoring",
        "description": "Immigration and police services may use social media activity and other digital data to monitor individuals. Understanding your rights and what you share online is key.",
        "resource": {
            "title": "Surveillance & Social Media Intelligence",
            "desc": "Journal article exploring how law enforcement accesses and uses social media data.",
            "url": "https://doi.org/10.1093/ijlit/eaw007"
        }
    },
    "Protecting Yourself from Scams": {
        "title": "Protecting Yourself from Scams",
        "problem": "Common Scams Targeting Newcomers",
        "description": "Scammers often impersonate government agencies like CRA or IRCC, demanding payments or threatening deportation.",
        "resource": {
            "title": "Canadian Anti-Fraud Centre",
            "desc": "Learn how to spot scams and report them directly to Canada’s official anti-fraud agency.",
            "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm"
        }
    },
    "Understanding AI in Canada": {
        "title": "Understanding AI and Digital Rights in Canada",
        "problem": "Bias and Data Use in Automated Systems",
        "description": "AI systems used in hiring, policing, or immigration decisions can reflect biases. It's important to understand how AI can affect your data and opportunities.",
        "resource": {
            "title": "Responsible AI Guidelines (Canada)",
            "desc": "Outlines how AI should be developed and used fairly and transparently.",
            "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence"
        }
    }
}

st.subheader("Explore Topics")
cols = st.columns(3)
topic_keys = list(topics.keys())

for i, key in enumerate(topic_keys):
    if cols[i % 3].button(key):
        st.session_state["selected_topic"] = key

st.markdown("---")

selected_key = st.session_state.get("selected_topic")
if selected_key and selected_key in topics:
    content = topics[selected_key]
    st.subheader(content["title"])
    st.markdown(f"**{content['problem']}**")
    st.write(content["description"])
    st.markdown("#### Suggested Resource")
    st.markdown(f"**[{content['resource']['title']}]({content['resource']['url']})**")
    st.write(content["resource"]["desc"])

# --- Additional Resource List ---
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
