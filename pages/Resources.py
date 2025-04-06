import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            color: black;
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        a {
            text-decoration: none;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main Title ---
st.title("Resources")

st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers, unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status. Below are tips to help you protect your privacy and a list of useful resources to explore.
""")

st.markdown("---")

# --- Subpage Links as Cards ---
st.subheader("Explore Privacy Topics")

resources_cards = [
    {
        "title": "A Newcomer's Guide to Healthcare, Privacy, and Jobs in Canada",
        "desc": "Understand healthcare challenges, privacy risks, and job barriers newcomers face — and what you can do to stay protected.",
        "url": "https://privacy-toolkit.streamlit.app/A_Newcomers_Guide"
    },
    {
        "title": "Staying Safe Online",
        "desc": "Learn how to avoid phishing, scams, and digital threats in daily life.",
        "url": "https://privacy-toolkit.streamlit.app/Staying_Safe_Online"
    },
    {
        "title": "How Police Use Your Data",
        "desc": "Explore how authorities may access digital data and social media information.",
        "url": "https://privacy-toolkit.streamlit.app/How_Police_Use_Your_Data"
    },
    {
        "title": "Protecting Yourself from Scams",
        "desc": "Recognize and avoid fraud schemes targeting newcomers.",
        "url": "https://privacy-toolkit.streamlit.app/Protecting_Yourself_from_Scams"
    },
    {
        "title": "Understanding AI in Canada",
        "desc": "Learn how artificial intelligence affects your data and digital rights.",
        "url": "https://privacy-toolkit.streamlit.app/Understanding_AI_in_Canada"
    }
]

for res in resources_cards:
    st.markdown(f"""
    <div style='border:1px solid #ccc; border-radius:10px; padding:1rem; margin-bottom:1rem; background:#fff'>
        <a href="{res['url']}" target="_blank">
            <h4>{res['title']}</h4>
            <p>{res['desc']}</p>
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- Additional Resources Section ---
st.subheader("Additional Useful Resources")

additional_resources = [
    ("Canadian Anti-Fraud Centre", "The Canadian Anti-Fraud Centre collects information on fraud and identity theft. Report scams here.", "https://antifraudcentre-centreantifraude.ca/index-eng.htm"),
    ("Data Detox Kit", "Explore guides on AI, digital privacy, misinformation, and tech health.", "https://datadetoxkit.org/en/home"),
    ("Enforcing Canada's Anti-Spam Legislation (CASL)", "Understand five common types of spam and how to report them.", "https://crtc.gc.ca/eng/internet/pub/20240930.htm"),
    ("Ensuring Your Privacy is Protected", "Learn simple strategies to protect your personal information.", "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected"),
    ("Exploring Digital Equity for Newcomer Services", "A report highlighting digital barriers and hybrid service solutions.", "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf"),
    ("Free Help for Newcomers - YMCA", "Offers free language training and orientation support.", "https://www.ymcagta.org/immigrant-services"),
    ("Meaningful Consent Guidelines", "Guidelines to ensure you understand what you're agreeing to.", "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/"),
    ("Generative AI: Government Guide", "How to use AI tools ethically while protecting privacy.", "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html"),
    ("Personal Information Banks", "See how the Canadian government stores and uses personal data.", "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html"),
    ("National Cyber Threat Assessment 2025-2026", "Learn about top emerging digital threats in Canada.", "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026"),
    ("Newcomer Fraud Risk Article", "Why newcomers are twice as likely to be scammed and how to stay safe.", "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/")
]

for title, desc, url in additional_resources:
    st.markdown(f"""
    <div style='border-left:4px solid #337ab7; padding:0.5rem 1rem; margin-bottom:1rem;'>
        <b>{title}</b><br>
        <span style='font-size: 0.9rem'>{desc}</span><br>
        <span style='font-size: 0.9rem; color:#555'>{url}</span>
    </div>
    """, unsafe_allow_html=True)
