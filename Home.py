import streamlit as st
import base64
from sidebar import render_sidebar
from language import get_language

# 页面配置
st.set_page_config(page_title="Privacy Toolkit", layout="wide")

# 获取当前语言
lang = get_language()
render_sidebar()

# --- 样式 ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Georgia', serif;
        }
        .fixed-logo {
            position: absolute;
            top: 20px;
            left: 30px;
            z-index: 999;
        }
        .typewriter {
            font-size: 2.75em;
            color: #002145;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #002145;
            width: 0;
            animation: typing 3s steps(40, end) forwards, blink 1s infinite;
            margin-top: 0.5rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        @keyframes blink {
            50% { border-color: transparent }
        }
        .section-box {
            border: 1px solid #e0e0e0;
            border-radius: 14px;
            padding: 1rem;
            background-color: #ffffff;
            height: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# --- 左上角 Logo ---
logo_base64 = base64.b64encode(open("uoft_logo.png", "rb").read()).decode()
st.markdown(
    f"""
    <div class='fixed-logo'>
        <img src='data:image/png;base64,{logo_base64}' width='100'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 动画标题 ---
st.markdown(
    "<div class='typewriter'>欢迎使用隐私工具包</div>" if lang == "中文"
    else "<div class='typewriter'>Welcome to the Privacy Toolkit</div>",
    unsafe_allow_html=True
)

# --- 简介段落 ---
intro = (
    "本工具包帮助新移民了解隐私权，保护个人数据，避免诈骗，并安全使用加拿大的数字服务。"
    if lang == "中文"
    else "This toolkit helps newcomers to Canada understand privacy rights, protect their personal data, avoid scams, and safely use digital services in their new life in Canada."
)
st.write(intro)

st.markdown("---")

# --- 子栏目标题 ---
st.subheader("你将在这里找到" if lang == "中文" else "What You’ll Find Here")

# --- 卡片三栏布局 ---
cols = st.columns(3)

with cols[0]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'隐私小测试' if lang == '中文' else 'Privacy Quiz'}</strong><br/>
            {'通过真实情境测试你的隐私意识并获取实用建议。' if lang == '中文' else 'Test your knowledge with real-life scenarios and tips.'}
        </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'资源库' if lang == '中文' else 'Resource Library'}</strong><br/>
            {'了解隐私法律、数字安全及医疗同意制度。' if lang == '中文' else 'Explore privacy laws, digital safety, and healthcare consent.'}
        </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'关于本项目' if lang == '中文' else 'About the Project'}</strong><br/>
            {'了解我们是谁，以及创建本工具包的初衷。' if lang == '中文' else 'Learn who we are and what inspired this toolkit.'}
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 底部蓝色提醒框 ---
if lang == "English":
    st.info("Please use the sidebar on the left to navigate between sections. 中文用户：请切换导航栏中的语言为中文以查看内容（中文导航栏仅供参考，请点击英文导航项浏览）。")
else:
    st.info("中文用户请切换左侧导航栏语言为中文浏览内容，中文导航栏仅供参考，请点击英文项目以正常跳转页面。")
