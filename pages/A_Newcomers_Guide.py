import streamlit as st

import streamlit as st

st.set_page_config(page_title="A Newcomer’s Guide", layout="wide")

st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("A Newcomer’s Guide to Healthcare, Privacy, and Jobs in Canada")

# (your content continues here)

st.title("A Newcomer’s Guide to Healthcare, Privacy, and Jobs in Canada")

st.subheader("The Problem with Language Barriers")
st.write("""
People who don’t speak English or French well may get worse healthcare. When doctors and patients can’t understand each other, it can lead to mistakes. For example, a patient’s private health details might be shared with the wrong person, or a patient might agree to a treatment they don’t fully understand.
""")

st.subheader("1. Healthcare: Why Language Matters")
st.markdown("**What’s Important:**")
st.write("""
If you don’t speak English or French well, it can be hard to get good healthcare. Doctors and nurses might misunderstand your symptoms, or you might sign forms without knowing what they mean. This could lead to wrong treatments or sharing your private health details with others by accident.
""")
st.markdown("**What to Do:**")
st.write("""
- Ask for a professional interpreter at hospitals or clinics (it’s your right!).
- Learn key health words in English/French (e.g., “pain,” “allergy”).
- Use free language classes like LINC/CLIC (see resources below).
""")

st.subheader("2. Privacy Policies: Don’t Get Tricked")
st.markdown("**What’s Important:**")
st.write("""
Privacy policies (rules about how companies use your data) are often in English or French. If you sign them without understanding, you might unknowingly share your address, phone number, or financial details with strangers.
""")
st.markdown("**What to Do:**")
st.write("""
- Always ask someone you trust to translate privacy forms.
- Look for these key details before signing:
  - What data is collected? (e.g., your name, birthdate).
  - Who gets your data? (e.g., banks, advertisers).
  - What are the risks? (e.g., identity theft).
""")

st.subheader("3. Jobs: Why Language Skills Are Key")
st.markdown("**What’s Important:**")
st.write("""
Most jobs in Canada require English or French. Without these skills, you might miss job opportunities, even if you’re highly skilled in your field.
""")
st.markdown("**What to Do:**")
st.write("""
- Take free government language classes (LINC for English, CLIC for French).
- Practice job-specific terms (e.g., “customer service,” “safety training”).
- Attend workshops at newcomer centers to build résumé and interview skills.
""")

st.subheader("4. Free Language Classes: Your Path to Success")
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

st.subheader("Suggested Resources")
st.markdown("""
- [Language Barriers in Access to Health Care](https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html)  
  Explains how language gaps affect care quality and lists solutions like interpreter training.

- [Guidelines for Obtaining Meaningful Consent](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/)  
  Details how organizations must simplify privacy information to ensure people truly understand what they’re agreeing to.

- [Free Help for Newcomers](https://www.ymcagta.org/immigrant-services)  
  Offers language training and cultural orientation to ease integration.

- [Language Classes Funded by the Government of Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html)  
  Government-funded programs to help newcomers learn English/French.
""")
