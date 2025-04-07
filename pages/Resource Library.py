import streamlit as st
from sidebar import render_sidebar
from language import get_language

# --- Page Config ---
st.set_page_config(page_title="Resource Library", layout="wide")

# --- Language & Sidebar ---
lang = get_language()
render_sidebar()

# --- Styling ---
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
            text-align: center;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #3c4f60;
            margin-bottom: 2.5rem;
            text-align: center;
        }

        .card {
            background-color: #DCEAF4;
            padding: 1.5rem 1.8rem;
            border-radius: 14px;
            font-weight: bold;
            color: #1a1a1a;
            text-decoration: none;
            font-size: 1.05rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            height: 100px;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        .card:visited, .card:link {
            color: #1a1a1a;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header & Subtitle ---
if lang == "English":
    st.markdown("<h1>Resource Library</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore key topics related to privacy, safety, AI, and digital protection in Canada.</div>", unsafe_allow_html=True)
else:
    st.markdown("<h1>资源库</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>浏览有关隐私、安全、人工智能与加拿大数字保护的核心主题。</div>", unsafe_allow_html=True)

# --- Titles & Links ---
titles = {
    "English": [
        "Newcomer’s Guide to Healthcare & Jobs",
        "How Police Use Your Data",
        "Protecting Yourself from Scams",
        "Understanding AI in Canada",
        "Staying Safe Online"
    ],
    "中文": [
        "新移民健康与就业指南",
        "警方如何使用你的数据",
        "如何防范诈骗",
        "了解加拿大的人工智能",
        "线上安全守则"
    ]
}

links = {
    "English": [
        "https://privacy-html-subpages.vercel.app/newcomer-guide.html",
        "https://privacy-html-subpages.vercel.app/how-police-use-data.html",
        "https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams.html",
        "https://privacy-html-subpages.vercel.app/understanding-ai-in-canada.html",
        "https://privacy-html-subpages.vercel.app/staying-safe-online.html"
    ],
    "中文": [
        "https://privacy-html-subpages.vercel.app/newcomer-guide-zh.html",
        "https://privacy-html-subpages.vercel.app/how-police-use-data-zh.html",
        "https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams-zh.html",
        "https://privacy-html-subpages.vercel.app/understanding-ai-in-canada-zh.html",
        "https://privacy-html-subpages.vercel.app/staying-safe-online-zh.html"
    ]
}

# --- Render in 2 columns ---
titles_list = titles["English"] if lang == "English" else titles["中文"]
links_list = links["English"] if lang == "English" else links["中文"]

num_cards = len(titles_list)

for i in range(0, num_cards, 2):
    cols = st.columns(2)
    
    # Left column
    with cols[0]:
        st.markdown(f'<a class="card" href="{links_list[i]}" target="_blank">{titles_list[i]}</a>', unsafe_allow_html=True)

    # Right column (only render if exists)
    if i + 1 < num_cards:
        with cols[1]:
            st.markdown(f'<a class="card" href="{links_list[i+1]}" target="_blank">{titles_list[i+1]}</a>', unsafe_allow_html=True)
    else:
        # If it's the last one and no right column, center it
        with cols[1]:
            st.write("")
