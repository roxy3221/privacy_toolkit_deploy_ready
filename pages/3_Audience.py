import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Audience Overview", layout="wide")

# --- 自定义样式：浅蓝背景、expander 标题字体增大 ---
st.markdown("""
    <style>
    /* 页面整体背景 & 字体 */
    html, body, .stApp {
        background-color: #F0F6FB; /* 浅蓝色背景 */
        font-family: 'Georgia', serif;
    }
    
    /* 修改下拉 section 的标题样式 */
    div[data-testid="stExpander"] > div > div > button {
        font-size: 1.5rem;   /* 增大标题字体 */
        font-weight: bold;
        color: #002145;
    }
    
    /* Goals 区域 */
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
st.title("Audience Overview")

# --- Primary Audience 下拉 ---
with st.expander("Primary Audience - New Immigrants(Ages 18–55)"):
    st.write("""
    - Often unfamiliar with certain systems or privacy laws
    - More likely to face scams, data misuse, or lack of informed consent
    - Frequently asked to share sensitive data in various scenarios
    """)

# --- Secondary Audience 下拉 ---
with st.expander("Secondary & Tertiary Audiences"):
    st.write("""
    - Professionals who provide support or digital literacy programs
    - Educators & staff reinforcing understanding and trust
    - Policy makers & advocates promoting inclusive, safer digital spaces
    - Mental health professionals recognizing privacy as part of well-being
    """)

# --- Toolkit Goals 区域 ---
st.markdown('<div class="goal-boxes">', unsafe_allow_html=True)
st.markdown("<h2>Toolkit Goals</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="goal-grid">
  <div class="goal-item">Help users understand their privacy rights</div>
  <div class="goal-item">Provide tools for secure communication and online navigation</div>
  <div class="goal-item">Increase awareness of data collection and digital safety</div>
  <div class="goal-item">Reduce risks tied to scams, discrimination, or misinformation</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
