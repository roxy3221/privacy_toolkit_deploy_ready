import streamlit as st

# --- Minimal styling with U of T-like light blue background ---
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
            max-width: 800px;
            margin: auto;
        }
        h1, h2, h3, h4, h5 {
            color: #002145;
        }
        a {
            text-decoration: none !important;
            color: black !important;
        }
        a:hover {
            text-decoration: underline !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("A Newcomer’s Guide to Healthcare, Privacy, and Jobs in Canada")

# The Problem
st.header("The Problem with Language Barriers")
st.write("""
People who don’t speak English or French well may get worse healthcare.
When doctors and patients can’t understand each other, it can lead to mistakes.
For example, a patient’s private health details might be shared with the wrong person,
or a patient might agree to a treatment they don’t fully understand.
""")

# Expander Sections
with st.expander("1. Healthcare: Why Language Matters"):
    st.markdown("**What’s Important:**")
    st.write("""
    If you don’t speak English or French well, it can be hard to get good healthcare.
    Doctors and nurses might misunderstand your symptoms, or you might sign forms 
    without knowing what they mean. This could lead to wrong treatments or sharing 
    your private health details by accident.
    """)
    st.markdown("**What to Do:**")
    st.write("""
    - Ask for a professional interpreter at hospitals or clinics (it’s your right!).
    - Learn key health words in English/French (e.g., “pain,” “allergy”).
    - Use free language classes like LINC/CLIC (see resources below).
    """)

with st.expander("2. Privacy Policies: Don’t Get Tricked"):
    st.markdown("**What’s Important:**")
    st.write("""
    Privacy policies (rules about how companies use your data) are often in English or French.
    If you sign them without understanding, you might unknowingly share your address, phone number,
    or financial details with strangers.
    """)
    st.markdown("**What to Do:**")
    st.write("""
    - Always ask someone you trust to translate privacy forms.
    - Look for these key details before signing:
      - What data is collected? (e.g., your name, birthdate)
      - Who gets your data? (e.g., banks, advertisers)
      - What are the risks? (e.g., identity theft)
    """)

with st.expander("3. Jobs: Why Language Skills Are Key"):
    st.markdown("**What’s Important:**")
    st.write("""
    Most jobs in Canada require English or French. Without these skills, 
    you might miss job opportunities, even if you’re highly skilled in your field.
    """)
    st.markdown("**What to Do:**")
    st.write("""
    - Take free government language classes (LINC for English, CLIC for French).
    - Practice job-specific terms (e.g., “customer service,” “safety training”).
    - Attend workshops at newcomer centers to build résumé and interview skills.
    """)

with st.expander("4. Free Language Classes: Your Path to Success"):
    st.markdown("**What’s Important:**")
    st.write("""
    Learning English or French helps you:
    - Understand doctors, teachers, and employers.
    - Avoid scams and protect your privacy.
    - Find better jobs and connect with your community.
    """)
    st.markdown("**What to Do:**")
    st.write("""
    - If you’re a permanent resident or protected person, you qualify for free classes.
    - Search for LINC/CLIC courses near you: Canada.ca Language Classes.
    - Contact local organizations like the YMCA for help enrolling: YMCA Newcomer Services.
    """)

st.markdown("---")

# 2.1.1 Suggested Resources
st.subheader("Suggested Resources")

suggested_resources = [
    {
        "title": "Language Barriers in Access to Health Care",
        "url": "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html",
        "desc": "Explains how language gaps affect care quality and lists solutions like interpreter training."
    },
    {
        "title": "Guidelines for obtaining meaningful consent",
        "url": "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
        "desc": "How organizations must simplify privacy information to ensure people truly understand what they're agreeing to."
    },
    {
        "title": "Free Help For Newcomers (YMCA)",
        "url": "https://www.ymcagta.org/immigrant-services",
        "desc": "Offers language training and cultural orientation to ease integration."
    },
    {
        "title": "Language Classes Funded by the Government of Canada",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
        "desc": "Government-funded programs to help newcomers learn English/French."
    }
]

for res in suggested_resources:
    st.markdown(f"**[{res['title']}]({res['url']})**  \n{res['desc']}")
    st.write("")
