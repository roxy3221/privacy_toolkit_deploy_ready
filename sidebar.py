import streamlit as st

def render_sidebar():
    # 简单中文导航目录，仅文字显示
    menu = [
        "首页",
        "关于我们",
        "目标受众",
        "小测试",
        "资源库",
        "实用网站"
    ]

    # Sidebar 样式一致，使用小字体、无交互
    st.sidebar.markdown("<br>".join(
        [f"<div style='font-size: 0.9rem; padding: 0.2rem 0;'>{item}</div>" for item in menu]
    ), unsafe_allow_html=True)
