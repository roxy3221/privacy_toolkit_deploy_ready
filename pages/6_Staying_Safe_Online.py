import streamlit as st

# --- Styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }

        .protect-card {
            background-color: white;
            padding: 1rem 1.5rem;
            margin-bottom: 1rem;
            border-radius: 1.5rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        }

        .step-title {
            font-weight: bold;
            margin-bottom: 0.25rem;
            font-size: 1.1rem;
        }

        .step-body {
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page content ---
st.title("Staying Safe Online")

st.subheader("Why Digital Safety Matters for Newcomers")
st.write("""
Canada faces growing cyber threats, like hackers attacking banks, hospitals, or government services.
These attacks can disrupt daily life—for example, freezing online banking or shutting down hospital systems.
As a newcomer, you may rely heavily on the internet for jobs, healthcare, and staying connected.
But not all websites or apps are safe, and your personal data (like passwords or bank details) could be stolen if you’re not careful.
""")

st.subheader("Key Risks")
st.markdown("""
- **Unsecured networks**: Public Wi-Fi (e.g., in cafes) can let hackers steal your data.  
- **Fake websites/emails**: Scammers might pretend to be the government (like IRCC) to trick you into sharing personal info.  
- **Data leaks**: Apps or services you use might accidentally expose your private information.
""")

st.subheader("Digital Equity & Inclusion: What It Means for You")
st.markdown("""
**Digital Equity** means everyone can access technology needed for jobs, education, and services.  
**Digital Inclusion** means ensuring even disadvantaged groups (like newcomers) can use the internet safely.

**Why This Matters:**
- Job opportunities posted online  
- Important updates about your immigration status  
- Virtual healthcare appointments
""")

st.subheader("How to Protect Yourself")

# --- Step Cards ---
tips = [
    {
        "title": "1. Use Strong Passwords",
        "details": [
            "Create passwords with letters, numbers, and symbols (e.g., Sunshine2023!).",
            "Never reuse passwords for multiple accounts."
        ]
    },
    {
        "title": "2. Avoid Public Wi-Fi for Sensitive Tasks",
        "details": [
            "Don’t check bank accounts or share personal info on café/airport Wi-Fi.",
            "Use mobile data instead."
        ]
    },
    {
        "title": "3. Spot Scams",
        "details": [
            "Government agencies (like IRCC) will never call or email asking for money or passwords.",
            "Scammers use fake links like `IRCC-service.ca` (real site: `Canada.ca`)."
        ]
    },
    {
        "title": "4. Keep Software Updated",
        "details": [
            "Update your phone, computer, and apps regularly to fix security gaps."
        ]
    },
    {
        "title": "5. Learn About Digital Safety",
        "details": [
            "Visit [Get Cyber Safe](https://www.getcybersafe.gc.ca/en) for tips in multiple languages."
        ]
    }
]

for tip in tips:
    st.markdown(f"""
    <div class="protect-card">
        <div class="step-title">{tip['title']}</div>
        <div class="step-body">{'<br>'.join(tip['details'])}</div>
    </div>
    """, unsafe_allow_html=True)

# Optional: Resources section below
st.markdown("#### 2.2.1 Suggested Resources")
st.markdown("""
- [National Cyber Threat Assessment 2025-2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026): Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams.  
- [Exploring Digital Equity for Newcomer Services](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf): Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services.
""")
