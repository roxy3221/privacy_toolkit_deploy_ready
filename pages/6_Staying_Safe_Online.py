import streamlit as st

# --- Page styling ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1, h2, h3 {
            color: #1C1C1C;
        }
        .section {
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Staying Safe Online")

st.markdown("""
### Why Digital Safety Matters for Newcomers

**What’s Important:**  
Canada faces growing cyber threats, like hackers attacking banks, hospitals, or government services. These attacks can disrupt daily life—for example, freezing online banking or shutting down hospital systems. As a newcomer, you may rely heavily on the internet for jobs, healthcare, and staying connected. But not all websites or apps are safe, and your personal data (like passwords or bank details) could be stolen if you’re not careful.

### Key Risks
- **Unsecured networks:** Public Wi-Fi (e.g., in cafes) can let hackers steal your data.
- **Fake websites/emails:** Scammers might pretend to be the government (like IRCC) to trick you into sharing personal info.
- **Data leaks:** Apps or services you use might accidentally expose your private information.

### Digital Equity and Inclusion: What It Means for You
**Digital Equity** means everyone can access technology needed for jobs, education, and services.  
**Digital Inclusion** means ensuring even disadvantaged groups (like newcomers) can use the internet safely.

**Why This Matters:**
- Job opportunities posted online.
- Important updates about your immigration status.
- Virtual healthcare appointments.

---

### How to Protect Yourself

**1. Use Strong Passwords**  
Create passwords with letters, numbers, and symbols (e.g., Sunshine2023!).  
Never reuse passwords for multiple accounts.

**2. Avoid Public Wi-Fi for Sensitive Tasks**  
Don’t check bank accounts or share personal info on café/airport Wi-Fi. Use mobile data instead.

**3. Spot Scams**  
Government agencies (like IRCC) will never call or email asking for money or passwords.  
Check website URLs: Scammers use fake links like `IRCC-service.ca` (real site: `Canada.ca`).

**4. Keep Software Updated**  
Update your phone, computer, and apps regularly to fix security gaps.

**5. Learn About Digital Safety**  
Visit [Get Cyber Safe](https://www.getcybersafe.gc.ca/en) for tips in multiple languages.

---

### Suggested Resources

- **[National Cyber Threat Assessment 2025–2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)**  
  Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams.

- **[Digital Equity in Newcomer Services – Peel Region](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)**  
  Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services.
""")
