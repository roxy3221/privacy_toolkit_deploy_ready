import streamlit as st
from sidebar import render_sidebar
from language import get_language  # ✅ 引入语言控制

# 页面设置
st.set_page_config(page_title="About Us", layout="wide")

# 获取当前语言（共享语言状态）
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
        .photo-names {
            text-align: center;
            margin-top: 0.5rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- 页面标题 ---
if lang == "English":
    st.title("About Us")
else:
    st.title("关于我们")

# --- 成员照片 ---
col1, col2 = st.columns(2)
with col1:
    st.image("Roxy.JPG", caption="Yanyue Zhang", width=250)
with col2:
    st.image("Megan.JPG", caption="Megan Luo", width=250)

# --- 介绍文本 ---
if lang == "English":
    st.write("""
    We are students from the University of Toronto’s Privacy Studies course — 
    **Yanyue Zhang**, **Megan Luo**, and **Shazad Braich** — who created this digital toolkit
    to support newcomers in Canada as they face real privacy challenges in daily life.
    """)
else:
    st.write("""
    我们是多伦多大学隐私研究课程的学生 — 
    **Yanyue Zhang**、**Megan Luo** 和 **Shazad Braich**。我们创建了这个数字工具包，
    旨在帮助在加拿大生活的新移民应对日常生活中真实存在的隐私挑战。
    """)

# --- 初衷 ---
if lang == "English":
    st.header("Why We Made This")
    st.write("""
    Many newcomers are unaware of how their personal data can be used, shared, or misused in digital spaces.
    This project is our way of sharing knowledge, promoting safety, and making privacy accessible.
    """)
else:
    st.header("为什么我们要做这个项目")
    st.write("""
    许多新移民并不了解他们的个人数据在数字空间中可能被如何使用、共享或滥用。
    这个项目是我们分享知识、促进安全并提升隐私意识的一种方式。
    """)

# --- 联系方式 ---
if lang == "English":
    st.header("Contact Us")
    st.write("Email: [yanyue.zhang@mail.utoronto.ca](mailto:yanyue.zhang@mail.utoronto.ca)")
else:
    st.header("联系我们")
    st.write("电子邮箱： [yanyue.zhang@mail.utoronto.ca](mailto:yanyue.zhang@mail.utoronto.ca)")
