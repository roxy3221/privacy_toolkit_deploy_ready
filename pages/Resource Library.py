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
        }
        .subtitle {
            font-size: 1.1rem;
            color: #3c4f60;
            margin-bottom: 2.5rem;
        }
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 2.5rem 2rem;
            justify-content: center;
            margin-top: 2rem;
        }
        .card {
            background-color: #DCEAF4;
            padding: 1.5rem 2rem;
            border-radius: 14px;
            text-align: center;
            font-weight: bold;
            color: #1a1a1a;
            text-decoration: none;
            font-size: 1.1rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            width: 300px;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .card:visited, .card:link, .card:hover {
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

# --- Card Titles & Links ---
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

# 根据语言调整链接 (HTML页面的链接)
if lang == "English":
    links = [
        "https://privacy-html-subpages.vercel.app/newcomer-guide.html",
        "https://privacy-html-subpages.vercel.app/how-police-use-data.html",
        "https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams.html",
        "https://privacy-html-subpages.vercel.app/understanding-ai-in-canada.html",
        "https://privacy-html-subpages.vercel.app/staying-safe-online.html"
    ]
else:
    links = [
        "https://privacy-html-subpages.vercel.app/newcomer-guide-zh.html",
        "https://privacy-html-subpages.vercel.app/how-police-use-data-zh.html",
        "https://privacy-html-subpages.vercel.app/protecting-yourself-from-scams-zh.html",
        "https://privacy-html-subpages.vercel.app/understanding-ai-in-canada-zh.html",
        "https://privacy-html-subpages.vercel.app/staying-safe-online-zh.html"
    ]

# --- Render Cards ---
st.markdown('<div class="card-grid">', unsafe_allow_html=True)
for title, link in zip(titles["English" if lang == "English" else "中文"], links):
    st.markdown(f"""
        <a href="{link}" target="_blank" class="card">
            {title}
        </a>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
