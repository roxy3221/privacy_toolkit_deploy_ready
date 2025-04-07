import streamlit as st
from sidebar import render_sidebar
from language import get_language

# --- 页面配置 ---
st.set_page_config(page_title="Useful Resources", layout="wide")
lang = get_language()
render_sidebar()

# --- 样式 ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            color: black !important;
            font-family: 'Georgia', serif;
            margin: 0; 
            padding: 0;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        a {
            text-decoration: none !important;
            color: black !important;
        }
        a:hover {
            text-decoration: underline !important;
        }
        .resource-card {
            background-color: #ffffff;
            border: 1px solid #d6d6d6;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .resource-card:hover {
            border-color: #999999;
        }
        .resource-title {
            font-size: 1rem;
            font-weight: bold;
            margin-bottom: 0.3rem;
        }
        .resource-desc {
            font-size: 0.9rem;
            line-height: 1.4;
        }
    </style>
""", unsafe_allow_html=True)

# --- 页面标题 & 简介 ---
st.title("Useful Resources" if lang == "English" else "实用网站推荐")

st.write("""
Privacy is always important to keep in mind. Newcomers to Canada are often targeted by scammers 
because of language barriers, unfamiliarity with local systems, or urgent needs like finding jobs 
or settling immigration status. Below are tips to help you protect your privacy and a list of useful resources to explore.
""" if lang == "English" else """
隐私保护无时无刻不重要。新移民往往因为语言障碍、不熟悉加拿大制度、或急需工作/移民处理，而成为诈骗目标。
下面是一些隐私提示和实用资源，帮助你更好地保护自己。
""")

st.markdown("---")

# --- 多语言资源列表 ---
resources = [
    {
        "title": {
            "English": "Canadian Anti-Fraud Centre",
            "中文": "加拿大反诈骗中心"
        },
        "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
        "desc": {
            "English": "The Canadian Anti-Fraud Centre collects information on fraud and identity theft. If you think you're a victim, report it!",
            "中文": "加拿大反诈骗中心收集关于诈骗和身份盗用的信息。如果你怀疑自己被骗，请及时举报！"
        }
    },
    {
        "title": {
            "English": "Data Detox Kit",
            "中文": "数据排毒工具包"
        },
        "url": "https://datadetoxkit.org/en/home",
        "desc": {
            "English": "Explore guides about AI, digital privacy, security, and wellbeing.",
            "中文": "探索关于人工智能、数字隐私、安全与数字健康的指南。"
        }
    },
    {
        "title": {
            "English": "Learning Together for Responsible Artificial Intelligence",
            "中文": "负责任人工智能教育平台"
        },
        "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
        "desc": {
            "English": "Teaches how to use AI ethically, like avoiding data that reflects racial biases.",
            "中文": "帮助大众了解如何以负责任的方式使用人工智能，例如避免使用带有偏见的数据。"
        }
    },
    {
        "title": {
            "English": "Free Help For Newcomers",
            "中文": "新移民免费支持服务"
        },
        "url": "https://www.ymcagta.org/immigrant-services",
        "desc": {
            "English": "Offers language training and cultural orientation to ease integration.",
            "中文": "提供语言培训与文化适应服务，帮助新移民更顺利融入。"
        }
    },
    {
        "title": {
            "English": "National Cyber Threat Assessment 2025-2026",
            "中文": "2025-2026 年国家网络威胁评估"
        },
        "url": "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "desc": {
            "English": "Outlines cyber risks like attacks on supply chains or AI-driven scams.",
            "中文": "概述了供应链攻击、AI 诈骗等主要网络安全风险。"
        }
    },
]

# --- 渲染资源卡片 ---
for r in resources:
    st.markdown(f"""
    <div class="resource-card">
        <div class="resource-title"><a href="{r['url']}" target="_blank">{r['title'][lang]}</a></div>
        <div class="resource-desc">{r['desc'][lang]}</div>
    </div>
    """, unsafe_allow_html=True)
