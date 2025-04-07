import streamlit as st

def render_sidebar():
    menu = [
        "首页",
        "关于我们",
        "目标受众",
        "小测试",
        "资源库",
        "实用网站"
    ]

    st.sidebar.markdown("""
        <style>
        .sidebar-chinese-menu p {
            font-size: 0.91rem;
            padding: 0.25rem 1rem 0.25rem 0.75rem;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("<div class='sidebar-chinese-menu'>" + "\n".join(
        [f"<p>{item}</p>" for item in menu]
    ) + "</div>", unsafe_allow_html=True)
