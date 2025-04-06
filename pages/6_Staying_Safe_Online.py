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

# --- Styling for clean-centered layout ---
st.markdown("""
    <style>
        .centered-box {
            background-color: white;
            padding: 2rem;
            margin: 2rem auto;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
            max-width: 800px;
        }
        .centered-box h3 {
            font-size: 28px;
            margin-bottom: 1rem;
            font-family: 'Georgia', serif;
        }
        .centered-box p {
            font-size: 18px;
            line-height: 1.6;
        }
        .centered-box ol {
            padding-left: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main centered block ---
st.markdown('<div class="centered-box">', unsafe_allow_html=True)

st.markdown("### How to Protect Yourself", unsafe_allow_html=True)

st.markdown("""
<ol>
<li><b>Use Strong Passwords</b><br>
Create passwords with letters, numbers, and symbols (e.g., Sunshine2023!).<br>
Never reuse passwords for multiple accounts.</li>

<li><b>Avoid Public Wi-Fi for Sensitive Tasks</b><br>
Don’t check bank accounts or share personal info on café/airport Wi-Fi. Use mobile data instead.</li>

<li><b>Spot Scams</b><br>
Government agencies (like IRCC) will never call or email asking for money or passwords.<br>
Check website URLs: Scammers use fake links like <code>IRCC-service.ca</code> (real site: <code>Canada.ca</code>).</li>

<li><b>Keep Software Updated</b><br>
Update your phone, computer, and apps regularly to fix security gaps.</li>

<li><b>Learn About Digital Safety</b><br>
Visit <a href="https://www.getcybersafe.gc.ca/en" target="_blank">Get Cyber Safe</a> for tips in multiple languages.</li>
</ol>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

### Suggested Resources

- **[National Cyber Threat Assessment 2025–2026](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)**  
  Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams.

- **[Digital Equity in Newcomer Services – Peel Region](https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf)**  
  Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services.
""")
