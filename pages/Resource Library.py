import streamlit as st

# Set page config
st.set_page_config(page_title="Resource Library", layout="wide")

# Styling
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        h1 {
            font-size: 2.6rem;
            color: #002145;
            margin-bottom: 0.3rem;
        }
        .subtitle {
            font-size: 1.1rem;
            color: #3c4f60;
            margin-bottom: 2.5rem;
        }
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem 1.5rem; /* vertical gap first, horizontal second */
            justify-content: center;
            margin-top: 2rem;
        }
        .card {
            background-color: white;
            padding: 1.5rem 2rem;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            color: #0d2b3e;
            text-decoration: none;
            font-size: 1.1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            width: 300px;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        }
        .card:visited {
            color: #0d2b3e;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>Resource Library</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore key topics related to privacy, safety, AI, and digital protection in Canada.</div>", unsafe_allow_html=True)

# Card Grid
st.markdown("""
    <div class="card-grid">
        <a href="https://privacy-html-subpages.vercel.app/newcomer-guide.html" target="_blank" class="card">
            Newcomer’s Guide to Healthcare & Jobs
        </a>
        <a href="https://privacy-html-subpages.vercel.app/how-police-use-data.html" target="_blank" class="card">
            How Police Use Your Data
        </a>
        <a href="https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams.html" target="_blank" class="card">
            Protecting Yourself from Scams
        </a>
        <a href="https://privacy-html-subpages.vercel.app/understanding-ai-in-canada.html" target="_blank" class="card">
            Understanding AI in Canada
        </a>
        <a href="https://privacy-html-subpages.vercel.app/staying-safe-online.html" target="_blank" class="card">
            Staying Safe Online
        </a>
    </div>
""", unsafe_allow_html=True)
