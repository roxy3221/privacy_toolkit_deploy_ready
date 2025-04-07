import streamlit as st

def render_sidebar():
    # 设置语言（默认中文）
    if "lang" not in st.session_state:
        st.session_state.lang = "中文"

    # Sidebar - Language Selector
    lang = st.sidebar.selectbox("🌐 Language / 语言", ["English", "中文"], index=1 if st.session_state.lang == "中文" else 0)
    st.session_state.lang = lang

    # Sidebar - Custom Navigation
    st.sidebar.markdown("### 📂 " + ("Page Navigation" if lang == "English" else "页面导航"))

    nav = {
        "Home": "首页",
        "2_About_Us": "关于我们",
        "3_Audience": "目标受众",
        "4_Quiz": "小测试",
        "Resource Library": "资源库",
        "Useful Websites": "实用网站"
    }

    for filename, zh_name in nav.items():
        label = filename if lang == "English" else zh_name
        if st.sidebar.button(label):
            st.switch_page(f"pages/{filename}.py")

    # 隐藏原生 Sidebar 菜单
    st.markdown("""
        <style>
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    return lang
