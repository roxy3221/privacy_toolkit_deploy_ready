import streamlit as st
import base64
from sidebar import render_sidebar
from language import get_language  # 全站语言控制函数

# --- 页面设置 ---
st.set_page_config(page_title="Privacy Toolkit", layout="wide")

# --- 获取语言 + 渲染静态中文 Sidebar ---
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
        .typewriter {
            font-size: 2.75em;
            color: #002145;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #002145;
            width: 0;
            animation: typing 3s steps(40, end) forwards, blink 1s infinite;
            margin-top: 1rem;
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

# --- Logo ---
logo_base64 = base64.b64encode(open("uoft_logo.png", "rb").read()).decode()
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='180'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 标题动画 ---
if lang == "English":
    st.markdown("<div class='typewriter'>Welcome to the Privacy Toolkit</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='typewriter'>欢迎使用隐私工具包</div>", unsafe_allow_html=True)

# --- 简介内容 ---
if lang == "English":
    st.write("""
    This toolkit helps newcomers to Canada understand privacy rights, protect their personal data,
    avoid scams, and safely use digital services in their new life in Canada.
    """)
else:
    st.write("""
    本工具包帮助新移民了解隐私权，保护个人数据，避免诈骗，并安全使用加拿大的数字服务。
    """)

st.markdown("---")

# --- 页面内容预览标题 ---
if lang == "English":
    st.subheader("What You’ll Find Here")
else:
    st.subheader("你将在这里找到")

# --- 三个板块预览卡片 ---
cols = st.columns(3)
with cols[0]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'Privacy Quiz' if lang == 'English' else '隐私小测试'}</strong><br/>
            {'Test your knowledge with real-life scenarios and tips.' if lang == 'English' else '通过真实情境测试你的隐私意识并获取实用建议。'}
        </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'Resource Library' if lang == 'English' else '资源库'}</strong><br/>
            {'Explore privacy laws, digital safety, and healthcare consent.' if lang == 'English' else '了解隐私法律、数字安全及医疗同意制度。'}
        </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown(f"""
        <div class='section-box'>
            <strong>{'About the Project' if lang == 'English' else '关于本项目'}</strong><br/>
            {'Learn who we are and what inspired this toolkit.' if lang == 'English' else '了解我们是谁，以及创建本工具包的初衷。'}
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 底部提示 ---
if lang == "English":
    st.info("Use the sidebar on the left to view each section.")
else:
    st.markdown("""
        <p style='font-size: 0.95rem; color: #444;'>
            当前页面为中文显示，但左侧的导航栏为静态中文目录，<br>
            实际跳转仍需点击英文页面标题，或使用顶部语言选择切换页面语言。
        </p>
    """, unsafe_allow_html=True)
