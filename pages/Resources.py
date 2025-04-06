import streamlit as st
import webbrowser

# --- Global styling for full-screen light blue ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
            font-family: 'Georgia', serif;
        }
        .resource-card {
            border: 1px solid #ccc;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 12px;
            background-color: white;
        }
        .resource-card h4 {
            margin: 0;
        }
        .resource-card:hover {
            border-color: #4682B4;
            background-color: #f5faff;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Resources")
st.write("""
Newcomers to Canada are often targeted by scams or digital threats due to language barriers and unfamiliarity with local systems.
Below are categorized guides to help you stay safe and informed.
Click any topic to open more detailed guidance in a new window.
""")

# --- Cards for Topic Links ---
resources = [
    {
        "title": "A Newcomer's Guide to Healthcare, Privacy, and Jobs in Canada",
        "url": "https://privacy-toolkit-deploy-ready.streamlit.app/A_Newcomers_Guide"
    },
    {
        "title": "Staying Safe Online",
        "url": "https://privacy-toolkit-deploy-ready.streamlit.app/Staying_Safe_Online"
    },
    {
        "title": "How Police Use Your Data",
        "url": "https://privacy-toolkit-deploy-ready.streamlit.app/How_Police_Use_Your_Data"
    },
    {
        "title": "Protecting Yourself from Scams",
        "url": "https://privacy-toolkit-deploy-ready.streamlit.app/Protecting_Yourself_from_Scams"
    },
    {
        "title": "Understanding AI in Canada",
        "url": "https://privacy-toolkit-deploy-ready.streamlit.app/Understanding_AI_in_Canada"
    }
]

for res in resources:
    with st.container():
        st.markdown(f"""
        <div class='resource-card'>
            <h4><a href="{res['url']}" target="_blank">{res['title']}</a></h4>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Additional Resource List")
st.write("More trusted links and references can be found at the bottom of each topic page.")

# --- Additional Resources Section ---
st.markdown("## Additional Privacy Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers,
unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status. Below are tips to help you protect your privacy and a list of useful resources to explore.
""")

resources = [
    ("Canadian Anti-Fraud Centre", "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
     "Collects information on fraud and identity theft. Info on scams and how to report them."),
    ("Data Detox Kit", "https://datadetoxkit.org/en/home",
     "Explore guides about AI, privacy, security, wellbeing, misinformation, and more."),
    ("Privacy in Public Spaces", "https://doi.org/10.1093/ijlit/eaw007",
     "Expectations of privacy in social media intelligence and law enforcement."),
    ("CASL – Anti-Spam Law", "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
     "Understand five common types of spam and scams in Canada."),
    ("Protect Your Privacy (IPC)", "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
     "Ways to help you protect your personal data."),
    ("Digital Equity for Newcomers (Peel Region)", "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
     "Explores digital access challenges and hybrid service recommendations."),
    ("YMCA: Help for Newcomers", "https://www.ymcagta.org/immigrant-services",
     "Language training and cultural orientation support."),
    ("Meaningful Consent Guidelines", "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
     "How to simplify privacy information so people understand consent."),
    ("Generative AI: Government Guide", "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
     "Best practices for using AI while protecting privacy."),
    ("Personal Information Banks (InfoSource)", "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
     "Explains how agencies store and use your data."),
    ("Surveillance & Profiling (IJLIT)", "https://doi-org.myaccess.library.utoronto.ca/10.1093/ijlit/eaw007",
     "Understanding surveillance and profiling through data."),
    ("Language Barriers in Health Care", "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html",
     "Impact of language gaps on healthcare quality."),
    ("Free Language Classes", "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
     "Free English/French classes for newcomers."),
    ("Learning Together on AI Ethics", "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
     "How to use AI fairly and avoid bias."),
    ("Cyber Threat Assessment 2025–2026", "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
     "Latest trends in cyber risks and digital threats."),
    ("Newcomers & Fraud Risk Report", "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
     "Survey: newcomers twice as likely to be fraud targets.")
]

for title, link, desc in resources:
    st.markdown(f"**[{title}]({link})**  \n{desc}")
