import streamlit as st

st.set_page_config(page_title="Resource Library", layout="wide")

st.markdown("""
    <style>
        body, .stApp {
            background-color: #F0F6FB;
            font-family: 'Georgia', serif;
        }
        .resource-title {
            font-size: 2.4rem;
            font-weight: 700;
            color: #002145;
            margin-bottom: 0.2rem;
        }
        .resource-subtitle {
            font-size: 1.1rem;
            color: #34495e;
            margin-bottom: 2rem;
        }
        .card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.07);
            text-align: center;
            transition: transform 0.2s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card-title {
            font-weight: bold;
            color: #1a2e3b;
            font-size: 1.1rem;
        }
        a {
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='resource-title'>📚 Resource Library</div>", unsafe_allow_html=True)
st.markdown("<div class='resource-subtitle'>Explore key topics related to privacy, safety, AI, and digital protection in Canada.</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """<a href="https://privacy-html-subpages.vercel.app/newcomer-guide.html" target="_blank">
        <div class="card"><div class="card-title">Newcomer’s Guide to Healthcare & Jobs</div></div></a>""",
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """<a href="https://privacy-html-subpages.vercel.app/how-police-use-data.html" target="_blank">
        <div class="card"><div class="card-title">How Police Use Your Data</div></div></a>""",
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        """<a href="https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams.html" target="_blank">
        <div class="card"><div class="card-title">Protecting Yourself from Scams</div></div></a>""",
        unsafe_allow_html=True
    )

col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(
        """<a href="https://privacy-html-subpages.vercel.app/understanding-ai-in-canada.html" target="_blank">
        <div class="card"><div class="card-title">Understanding AI in Canada</div></div></a>""",
        unsafe_allow_html=True
    )
with col5:
    st.markdown(
        """<a href="https://privacy-html-subpages.vercel.app/staying-safe-online.html" target="_blank">
        <div class="card"><div class="card-title">Staying Safe Online</div></div></a>""",
        unsafe_allow_html=True
    )
with col6:
    st.markdown("")  # empty for symmetry
