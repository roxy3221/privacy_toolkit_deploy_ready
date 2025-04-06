import streamlit as st

# --- Global styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
        }
        body {
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .resource-card {
            background-color: #ffffff;
            border: 1px solid #d6d6d6;
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05);
            transition: 0.3s ease-in-out;
        }
        .resource-card:hover {
            border-color: #3778c2;
            box-shadow: 3px 3px 12px rgba(55, 120, 194, 0.2);
        }
        .resource-title {
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 0.3rem;
            color: #1a508b;
        }
        .resource-desc {
            font-size: 0.95rem;
            color: #333333;
        }
        .topic-card {
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: 0.2s ease-in-out;
        }
        .topic-card:hover {
            border-color: #1a508b;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        a {
            text-decoration: none;
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

# --- Main 5 resource topics as subpages ---
st.subheader("Explore Topics")

topic_links = {
    "A Newcomer's Guide": "https://privacy-toolkit-deploy-ready.streamlit.app/A_Newcomers_Guide",
    "Staying Safe Online": "https://privacy-toolkit-deploy-ready.streamlit.app/Staying_Safe_Online",
    "How Police Use Your Data": "https://privacy-toolkit-deploy-ready.streamlit.app/How_Police_Use_Your_Data",
    "Protecting Yourself from Scams": "https://privacy-toolkit-deploy-ready.streamlit.app/Protecting_Yourself_from_Scams",
    "Understanding AI in Canada": "https://privacy-toolkit-deploy-ready.streamlit.app/Understanding_AI_in_Canada",
}

cols = st.columns(2)
for i, (topic, url) in enumerate(topic_links.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <a href="{url}" target="_blank">
            <div class="topic-card">
                <strong>{topic}</strong>
            </div>
        </a>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Additional resource list ---
st.subheader("🔗 Additional Privacy Resources")

resources = [
    ("Canadian Anti-Fraud Centre", "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
     "Scam alerts, fraud reporting, and identity theft info."),
    ("Data Detox Kit", "https://datadetoxkit.org/en/home",
     "Guides on AI, digital privacy, health data, and tech wellbeing."),
    ("Privacy in Public Spaces", "https://doi.org/10.1093/ijlit/eaw007",
     "How law enforcement uses social media and public data."),
    ("CASL – Anti-Spam Law", "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
     "How to recognize and report spam or phishing."),
    ("Protect Your Privacy (IPC)", "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
     "Best practices for keeping your data private."),
    ("Digital Equity for Newcomers", "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
     "Challenges and solutions in digital access for newcomers."),
    ("YMCA: Help for Newcomers", "https://www.ymcagta.org/immigrant-services",
     "Language training and support for immigrants."),
    ("Consent Guidelines", "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
     "How companies should request and explain data consent."),
    ("Gov’t AI Use Guide", "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
     "Responsible and ethical use of generative AI."),
    ("Info Source: Data Use", "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
     "What data Canadian agencies collect and why."),
    ("Surveillance & Profiling (UofT)", "https://doi-org.myaccess.library.utoronto.ca/10.1093/ijlit/eaw007",
     "How profiling and surveillance happen with digital data."),
    ("Language Barriers in Health", "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html",
     "Healthcare access challenges for non-native speakers."),
    ("Free Language Classes (LINC)", "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
     "Find free government-funded language courses."),
    ("Responsible AI for Public", "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
     "Public education around ethical AI use."),
    ("National Cyber Threat Report", "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
     "Emerging cyber risks and prevention strategies."),
    ("Newcomer Fraud Report", "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
     "Survey: Newcomers face 2x the risk of fraud.")
]

# Render cards
for title, link, desc in resources:
    st.markdown(f"""
        <div class="resource-card">
            <div class="resource-title"><a href="{link}" target="_blank">{title}</a></div>
            <div class="resource-desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)
