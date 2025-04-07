import streamlit as st

def render_sidebar():
    # 当前页面名（用于避免跳转到自己）
    current_page = st.session_state.get("_page_current", None)

    # 中文菜单映射（键是文件名，值是显示名）
    nav_items = {
        "Home.py": "首页",
        "2_About_Us.py": "关于我们",
        "3_Audience.py": "目标受众",
        "4_Quiz.py": "小测试",
        "Resource Library.py": "资源库",
        "Useful Websites.py": "实用网站"
    }

    # 菜单渲染（排除当前页面，避免重复跳转）
    for filename, label in nav_items.items():
        if current_page != filename and st.sidebar.button(label):
            st.switch_page(f"pages/{filename}")

    # 隐藏默认英文菜单
    st.markdown("""
        <style>
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    return "中文"
