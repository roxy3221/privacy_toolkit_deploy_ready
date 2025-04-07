import streamlit as st

def get_language():
    # 如果没有设置过语言，默认英文
    if "lang" not in st.session_state:
        st.session_state["lang"] = "English"

    # 将语言切换器放在 sidebar 顶部，并设置 key 防止状态丢失
    with st.sidebar:
        lang = st.selectbox("🌐 Language / 语言", ["English", "中文"],
                            index=0 if st.session_state["lang"] == "English" else 1,
                            key="lang_selectbox")

    st.session_state["lang"] = lang
    return lang
