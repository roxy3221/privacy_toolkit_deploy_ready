import streamlit as st

def render_sidebar():
    # 自定义导航栏（仅中文，不再需要语言切换器）
    nav_items = {
        "Home": "首页",
        "2_About_Us": "关于我们",
        "3_Audience": "目标受众",
        "4_Quiz": "小测试",
        "Resource Library": "资源库",
        "Useful Websites": "实用网站"
    }

    # 添加自定义导航项，外观跟默认 Sidebar 一致
    for filename, zh_title in nav_items.items():
        st.sidebar.markdown(f"""
            <a href="/{filename.replace(' ', '%20')}" target="_self" style="
                display: block;
                padding: 0.4rem 0.75rem;
                border-radius: 0.5rem;
                color: #31333F;
                font-weight: 500;
                text-decoration: none;
                margin-bottom: 0.2rem;
            ">
                {zh_title}
            </a>
        """, unsafe_allow_html=True)

    # 隐藏默认 Sidebar 页面导航
    st.markdown("""
        <style>
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 可选：返回语言常量，方便页面中继续写中文内容（但也可以删掉）
    return "中文"
