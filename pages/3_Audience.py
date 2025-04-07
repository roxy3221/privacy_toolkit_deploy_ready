import streamlit as st
from sidebar import render_sidebar
from language import get_language

# --- 页面设置 ---
st.set_page_config(page_title="Audience Overview", layout="wide")

# --- 获取语言 & Sidebar ---
lang = get_language()
render_sidebar()

# --- 自定义样式：浅蓝背景 + 区块样式 ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #F0F6FB;
        font-family: 'Georgia', serif;
    }
    div[data-testid="stExpander"] > div > div > button {
        font-size: 1.5rem;
        font-weight: bold;
        color: #002145;
    }
    .goal-boxes {
        max-width: 900px;
        margin: 1rem auto 2rem auto;
        padding: 0 1rem;
    }
    .goal-boxes h2 {
        text-align: center;
        color: #002145;
        margin-bottom: 1rem;
    }
    .goal-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1rem;
        margin-top: 1.5rem;
    }
    .goal-item {
        background-color: #dceaf4;
        padding: 1rem 1.2rem;
        border-radius: 10px;
        border: 1px solid #c5dbe9;
    }
    </style>
""", unsafe_allow_html=True)

# --- 页面标题 ---
st.title("Audience Overview" if lang == "English" else "目标受众")

# --- 主受众 ---
with st.expander("Primary Audience - New Immigrants (Ages 18–55)" if lang == "English" else "主要受众：新移民（18-55岁）"):
    if lang == "English":
        st.write("""
        - Often unfamiliar with certain systems or privacy laws  
        - More likely to face scams, data misuse, or lack of informed consent  
        - Frequently asked to share sensitive data in various scenarios  
        """)
    else:
        st.write("""
        - 对加拿大隐私法规和数字系统不熟悉  
        - 更容易遭遇诈骗、数据滥用或信息误用  
        - 经常在移民、求职、银行等情境中被要求提供敏感数据  
        """)

# --- 次级 & 延伸受众 ---
with st.expander("Secondary & Tertiary Audiences" if lang == "English" else "次级和延伸受众"):
    if lang == "English":
        st.write("""
        - Professionals who provide support or digital literacy programs  
        - Educators & staff reinforcing understanding and trust  
        - Policy makers & advocates promoting inclusive, safer digital spaces  
        - Mental health professionals recognizing privacy as part of well-being  
        """)
    else:
        st.write("""
        - 提供支持或数字素养课程的工作人员  
        - 教育人员和支持人员，强化理解和信任  
        - 制定政策者和倡导者，推动更包容、安全的数字环境  
        - 关注心理健康的专业人士，将隐私纳入整体健康考量  
        """)

# --- 工具目标区块 ---
st.markdown('<div class="goal-boxes">', unsafe_allow_html=True)
st.markdown(f"<h2>{'Toolkit Goals' if lang == 'English' else '工具包目标'}</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div class="goal-grid">
  <div class="goal-item">{'Help users understand their privacy rights' if lang == 'English' else '帮助用户了解其隐私权利'}</div>
  <div class="goal-item">{'Provide tools for secure communication and online navigation' if lang == 'English' else '提供安全沟通与上网的工具'}</div>
  <div class="goal-item">{'Increase awareness of data collection and digital safety' if lang == 'English' else '增强对数据收集与数字安全的意识'}</div>
  <div class="goal-item">{'Reduce risks tied to scams, discrimination, or misinformation' if lang == 'English' else '降低诈骗、歧视或虚假信息带来的风险'}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
