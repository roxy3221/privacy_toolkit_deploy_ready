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

# --- 多语言资源列表（16 个）---
resources = [
    {
        "title": {"English": "Canadian Anti-Fraud Centre", "中文": "加拿大反诈骗中心"},
        "url": "https://antifraudcentre-centreantifraude.ca/index-eng.htm",
        "desc": {
            "English": "Provides info on past/current scams & lets you report fraud.",
            "中文": "提供诈骗信息及举报途径。"
        }
    },
    {
        "title": {"English": "Data Detox Kit", "中文": "数据排毒工具包"},
        "url": "https://datadetoxkit.org/en/home",
        "desc": {
            "English": "Guides on AI, privacy, security, wellbeing, health data, and misinformation.",
            "中文": "涵盖人工智能、隐私、安全、健康数据和虚假信息等主题。"
        }
    },
    {
        "title": {"English": "Privacy in Public Spaces (Edwards & Urquhart)", "中文": "公共空间隐私研究"},
        "url": "https://doi.org/10.1093/ijlit/eaw007",
        "desc": {
            "English": "Explores how social media intelligence is used by police.",
            "中文": "探讨社交媒体数据如何被警方使用。"
        }
    },
    {
        "title": {"English": "Enforcing Canada’s Anti-Spam Law (CASL)", "中文": "加拿大反垃圾邮件法"},
        "url": "https://crtc.gc.ca/eng/internet/pub/20240930.htm",
        "desc": {
            "English": "Understand 5 types of scam & spam targeting Canadians.",
            "中文": "了解 5 类常见诈骗与垃圾信息。"
        }
    },
    {
        "title": {"English": "Protecting Your Privacy (Ontario IPC)", "中文": "安省隐私专员建议"},
        "url": "https://www.ipc.on.ca/en/privacy-individuals/ensuring-your-privacy-is-protected",
        "desc": {
            "English": "Steps to take for better privacy.",
            "中文": "保护隐私的实用建议。"
        }
    },
    {
        "title": {"English": "Digital Equity in Newcomer Services", "中文": "新移民数字公平报告"},
        "url": "https://peelnewcomer.org/wp-content/uploads/sites/52/2025/01/Digital-Equity-in-Settlement-Services-Report_Final.pdf",
        "desc": {
            "English": "Highlights access gaps & recommends hybrid services.",
            "中文": "揭示新移民使用数字工具的难题，并推荐线上线下结合服务。"
        }
    },
    {
        "title": {"English": "YMCA Newcomer Support", "中文": "YMCA 新移民服务"},
        "url": "https://www.ymcagta.org/immigrant-services",
        "desc": {
            "English": "Free language training & cultural orientation.",
            "中文": "提供语言学习和文化适应服务。"
        }
    },
    {
        "title": {"English": "Meaningful Consent Guidelines", "中文": "知情同意指南"},
        "url": "https://www.priv.gc.ca/en/privacy-topics/collecting-personal-information/consent/gl_omc_201805/",
        "desc": {
            "English": "Helps you understand privacy terms before agreeing.",
            "中文": "帮助用户理解隐私政策内容再同意。"
        }
    },
    {
        "title": {"English": "Guide to Generative AI Use", "中文": "生成式 AI 使用指南"},
        "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html",
        "desc": {
            "English": "Use generative AI safely & ethically.",
            "中文": "介绍如何负责任地使用 AI 工具。"
        }
    },
    {
        "title": {"English": "Personal Information Banks (IRCC)", "中文": "个人信息数据库"},
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/access-information-privacy/info-source/personal-information-banks.html",
        "desc": {
            "English": "Shows how government stores biometrics & personal data.",
            "中文": "说明政府如何保存与使用指纹等生物数据。"
        }
    },
    {
        "title": {"English": "Data Profiling & Surveillance", "中文": "数据画像与监控"},
        "url": "https://doi-org.myaccess.library.utoronto.ca/10.1093/ijlit/eaw007",
        "desc": {
            "English": "Understanding how data can be used to track people.",
            "中文": "理解数据如何被用于监控与评估个人。"
        }
    },
    {
        "title": {"English": "Language Barriers in Healthcare", "中文": "语言障碍与医疗服务"},
        "url": "https://www.canada.ca/en/health-canada/services/health-care-system/reports-publications/health-care-accessibility/language-barriers.html",
        "desc": {
            "English": "Impact of language gaps & interpreter training.",
            "中文": "语言问题如何影响治疗质量，以及口译员的重要性。"
        }
    },
    {
        "title": {"English": "Government Language Classes (LINC/CLIC)", "中文": "政府语言培训班"},
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada/language-skills/classes.html",
        "desc": {
            "English": "Free English/French classes for newcomers.",
            "中文": "面向新移民的免费英语/法语学习资源。"
        }
    },
    {
        "title": {"English": "Learning Together for Responsible AI", "中文": "负责任 AI 教育平台"},
        "url": "https://ised-isde.canada.ca/site/advisory-council-artificial-intelligence/en/public-awareness-working-group/learning-together-responsible-artificial-intelligence",
        "desc": {
            "English": "Understand how to avoid data bias & use AI fairly.",
            "中文": "了解如何避免数据偏差并公平使用人工智能。"
        }
    },
    {
        "title": {"English": "Cyber Threat Report 2025–26", "中文": "2025–26 网络威胁报告"},
        "url": "https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026",
        "desc": {
            "English": "Covers AI scams & supply chain attacks.",
            "中文": "涵盖 AI 欺诈和供应链攻击等内容。"
        }
    },
    {
        "title": {"English": "New Canadian Media: Fraud Victim Risks", "中文": "新加拿大人易受诈骗报告"},
        "url": "https://www.newcanadianmedia.ca/new-to-canada-beware-youre-twice-as-likely-to-become-a-fraud-victim-survey-reveals/",
        "desc": {
            "English": "Explains why newcomers are more at risk.",
            "中文": "解释新移民为何更易受骗。"
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
