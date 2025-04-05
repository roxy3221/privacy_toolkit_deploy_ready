import streamlit as st

# --- Page-wide CSS for styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
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
            background-color: white;
            text-align: center;
            transition: 0.3s;
        }
        .resource-card:hover {
            border-color: #3B7EA1;
            background-color: #E6F0F6;
        }
    </style>
""", unsafe_allow_html=True)

# --- Session state to manage subpage rendering ---
if "resource_page" not in st.session_state:
    st.session_state.resource_page = None

# --- Main Header ---
st.title("Resources")
st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers because of language barriers,
unfamiliarity with local systems, or urgent needs like finding jobs or settling immigration status.
Below are tips to help you protect your privacy and a list of useful resources to explore.
""")
st.markdown("---")

# --- Resource Cards Navigation ---
if st.session_state.resource_page is None:
    st.subheader("Explore Topics")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("A Newcomer's Guide"):
            st.session_state.resource_page = "newcomer"
    with col2:
        if st.button("Staying Safe Online"):
            st.session_state.resource_page = "online"
    with col3:
        if st.button("How Police Use Your Data"):
            st.session_state.resource_page = "police"

    col4, col5, _ = st.columns(3)
    with col4:
        if st.button("Protecting Yourself from Scams"):
            st.session_state.resource_page = "scams"
    with col5:
        if st.button("Understanding AI in Canada"):
            st.session_state.resource_page = "ai"

    st.markdown("---")

# --- Subpage Content ---
def back_button():
    if st.button("🔙 Back to Resources"):
        st.session_state.resource_page = None

if st.session_state.resource_page == "newcomer":
    st.header("A Newcomer’s Guide to Healthcare, Privacy, and Jobs in Canada")
    st.subheader("The Problem with Language Barriers")
    st.write("""
People who don’t speak English or French well may get worse healthcare. When doctors and patients can’t understand each other, it can lead to mistakes.

**1. Healthcare: Why Language Matters**  
- Ask for a professional interpreter  
- Learn key health words  
- Use free classes (LINC/CLIC)

**2. Privacy Policies: Don’t Get Tricked**  
- Always ask someone you trust to translate privacy forms  
- Look for what data is collected, who it's shared with, and the risks

**3. Jobs: Why Language Skills Are Key**  
- Take free government language classes  
- Practice job-specific terms  
- Attend newcomer workshops

**4. Free Language Classes: Your Path to Success**  
- Qualify for LINC/CLIC if you're a permanent resident  
- Find courses at Canada.ca or YMCA

**Suggested Resources:**  
- [Language Barriers in Access to Health Care](https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html)  
- [Meaningful Consent Guidelines](https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/)  
- [YMCA Newcomer Services](https://www.ymcagta.org/immigrant-services)  
- [Canada Language Classes](https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html)
""")
    back_button()

elif st.session_state.resource_page == "online":
    st.header("Staying Safe Online")
    st.write("Content coming soon...")
    back_button()

elif st.session_state.resource_page == "police":
    st.header("How Police Use Your Data")
    st.write("Content coming soon...")
    back_button()

elif st.session_state.resource_page == "scams":
    st.header("Protecting Yourself from Scams")
    st.write("Content coming soon...")
    back_button()

elif st.session_state.resource_page == "ai":
    st.header("Understanding AI in Canada")
    st.write("Content coming soon...")
    back_button()
