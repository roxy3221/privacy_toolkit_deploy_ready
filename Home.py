import streamlit as st
import base64
from sidebar import render_sidebar
from language import get_language

# --- 页面配置 ---
st.set_page_config(page_title="Privacy Toolkit", layout="wide")

# --- 获取语言并渲染 Sidebar ---
lang = get_language()
render_sidebar()

# --- 样式设置 ---
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
        .logo-small {
            position: absolute;
            top: 15px;
            left: 30px;
        }
        .typewriter {
            font-size: 2.75em;
            color: #002145;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #002145;
            width: 0;
            animation: typing 3s steps(40, end) forwards, blink 1s infinite;
            margin: 5rem auto 1.5rem auto;
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
        .intro-text {
            text-align: center;
            font-size: 1.1rem;
            color: #2c3e50;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- 缩小 Logo 左上角 ---
logo_base64 = base64.b64encode(open("uoft_logo.png", "rb").read()).decode()
st.markdown(f"""
    <div class="logo-small">
        <img src="data:image/png;base64,{logo_base64}" width="80">
    </div>
""", unsafe_allow_html=True)

# --- 打字欢迎动画标题 ---
st.markdown(
    "<div class='typewriter'>欢迎使用隐私工具包</div>" if lang == "中文"
    else "<div class='typewriter'>Welcome to the Privacy Toolkit</div>",
    unsafe_allow_html=True
)

# --- 简介段落 ---
intro = (
    "This toolkit helps newcomers to Canada understand privacy rights, protect their personal data, avoid scams, and safely use digital services in their new life in Canada."
    if lang == "English"
    else "本工具包帮助新移民了解隐私权，保护个人数据，避免诈骗，并安全使用加拿大的数字服务。"
)
st.markdown(f"<div class='intro-text'>{intro}</div>", unsafe_allow_html=True)

st.markdown("---")

# --- 子栏目标题 ---
st.subheader("What You’ll Find Here" if lang == "English" else "你将在这里找到")

# --- 三个内容板块卡片 ---
cols = st.columns(3)
with cols[0]:
    st.markdown(
        f"""
        <div class='section-box'>
            <strong>{'Privacy Quiz' if lang == 'English' else '隐私小测试'}</strong><br/>
            {'Test your knowledge with real-life scenarios and tips.' if lang == 'English' else '通过真实情境测试你的隐私意识并获取实用建议。'}
        </div>
        """,
        unsafe_allow_html=True
    )
with cols[1]:
    st.markdown(
        f"""
        <div class='section-box'>
            <strong>{'Resource Library' if lang == 'English' else '资源库'}</strong><br/>
            {'Explore privacy laws, digital safety, and healthcare consent.' if lang == 'English' else '了解隐私法律、数字安全及医疗同意制度。'}
        </div>
        """,
        unsafe_allow_html=True
    )
with cols[2]:
    st.markdown(
        f"""
        <div class='section-box'>
            <strong>{'About the Project' if lang == 'English' else '关于本项目'}</strong><br/>
            {'Learn who we are and what inspired this toolkit.' if lang == 'English' else '了解我们是谁，以及创建本工具包的初衷。'}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- 蓝色提示框 ---
if lang == "English":
    st.info("Please use the sidebar on the left to navigate between sections. 
    中文用户请切换左侧导航栏语言为中文浏览内容。注意：中文导航仅供参考，体验完整内容请点选英文导航")
else:
    st.info("中文用户请选择左侧导航栏中的中文以阅读中文版本。注意：中文导航仅供参考，实际导航请点击英文。")
