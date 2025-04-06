import streamlit as st

# --- Styling ---
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
            max-width: 900px;
            margin: auto;
        }
        h1, h2, h3, h4, h5 {
            color: #002145;
        }
        .card {
            background-color: white;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Staying Safe Online")

st.header("Why Digital Safety Matters for Newcomers")
st.write("""
Canada faces growing cyber threats, like hackers attacking banks, hospitals, or government services.
These attacks can disrupt daily life — for example, freezing online banking or shutting down hospital systems.

As a newcomer, you may rely heavily on the internet for jobs, healthcare, and staying connected. 
But not all websites or apps are safe, and your personal data (like passwords or bank details) could be stolen if you’re not careful.
""")

# --- Card-like sections ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>Key Risks</h4>
        <ul>
            <li><strong>Unsecured networks:</strong> Public Wi-Fi can expose your personal data.</li>
            <li><strong>Fake websites/emails:</strong> Scammers may pose as IRCC or banks.</li>
            <li><strong>Data leaks:</strong> Poorly secured apps may expose your info.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>Digital Equity & Inclusion</h4>
        <p><strong>Digital Equity</strong> means everyone has access to key technology and internet.</p>
        <p><strong>Digital Inclusion</strong> ensures that disadvantaged communities — like newcomers — can use digital services safely.</p>
        <p><strong>Why This Matters:</strong></p>
        <ul>
            <li>Missing job opportunities</li>
            <li>Losing immigration updates</li>
            <li>Not accessing online healthcare</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h4>How to Protect Yourself</h4>
    <ul>
        <li><strong>Use Strong Passwords:</strong> Mix letters, numbers, and symbols (e.g., Sunshine2023!).</li>
        <li><strong>Avoid Public Wi-Fi:</strong> Don’t check banking or share info on open networks.</li>
        <li><strong>Spot Scams:</strong> IRCC will never email or call asking for money or passwords.</li>
        <li><strong>Keep Software Updated:</strong> Regular updates prevent hacking.</li>
        <li><strong>Learn More:</strong> Explore <a href="https://www.getcybersafe.gc.ca/en" target="_blank">Get Cyber Safe</a> for multilingual tips.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("2.2.1 Suggested Resources")

resources = [
    {
        "title": "National Cyber Threat Assessment 2025-2026",
        "url": "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "desc": "Outlines emerging cyber risks, like attacks on supply chains or AI-driven scams."
    },
    {
        "title": "Exploring Digital Equity for Newcomer Services",
        "url": "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
        "desc": "Highlights challenges newcomers face in accessing digital tools and recommends hybrid (online + in-person) services."
    }
]

for res in resources:
    st.markdown(f"**[{res['title']}]({res['url']})**  \n{res['desc']}")
    st.write("")
