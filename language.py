import streamlit as st

def get_language():
    # 如果没有设置过语言，默认英文
    if "lang" not in st.session_state:
        st.session_state["lang"] = "English"

    # 顶部语言切换器（每页都可调用）
    lang = st.selectbox("🌐 Language / 语言", ["English", "中文"],
                        index=0 if st.session_state["lang"] == "English" else 1)
    st.session_state["lang"] = lang
    return lang
