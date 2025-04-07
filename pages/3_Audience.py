import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Audience Overview", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* 整体页面背景 & 字体 */
    html, body, .stApp {
        background-color: #F0F6FB;
        font-family: 'Georgia', serif;
    }

    /* 顶部大卡片（Hero Card） */
    .hero-card {
        max-width: 700px;           /* 控制卡片宽度 */
        margin: 3rem auto 2rem;    /* 上下左右外边距 */
        background-color: #FFFFFF;  /* 白色背景 */
        border-radius: 14px;        /* 圆角 */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* 阴影 */
        padding: 2rem;             /* 内边距 */
        text-align: center;        /* 内容居中 */
        font-size: 1.4rem;         /* 文字大小 */
        font-weight: 600;          /* 文字粗细 */
        color: #000;               /* 字体颜色 */
    }

    /* 观众卡片（Primary / Secondary） */
    .audience-card {
        max-width: 800px;
        margin: 2rem auto;         /* 自动居中 */
        background-color: #FFFFFF;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        padding: 1.5rem 2rem;
    }

    /* 卡片内的标题 */
    .audience-card h2 {
        text-align: center;
        margin-bottom: 1rem;
        color: #002145;
    }

    /* 列表文字大小 & 间距 */
    .audience-card li {
        font-size: 1.02rem;
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }
    /* 加粗高亮段落 */
    .highlight {
        margin-top: 1rem;
        font-weight: bold;
        text-align: center;
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

# --- 顶部大卡片（Hero Card） ---
st.markdown("""
<div class="hero-card">
    Newcomer’s Guide to Healthcare & Jobs
</div>
""", unsafe_allow_html=True)

# --- Primary Audience Card ---
st.markdown('<div class="audience-card">', unsafe_allow_html=True)
st.markdown("<h2>Primary Audience</h2>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center"><strong>New Immigrants (Ages 18–55)</strong></p>
<ul>
    <li>Often unfamiliar with Canadian digital systems and privacy laws</li>
    <li>More likely to face scams, data misuse, or lack of informed consent</li>
    <li>Frequently asked to share sensitive data for immigration, jobs, or banking</li>
</ul>
<p class="highlight">The toolkit supports safer, more confident digital choices.</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Secondary Audience Card ---
st.markdown('<div class="audience-card">', unsafe_allow_html=True)
st.markdown("<h2>Secondary & Tertiary Audiences</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li><strong>Settlement workers & librarians:</strong> Use toolkit in digital literacy programs</li>
    <li><strong>Educators & support staff:</strong> Help reinforce understanding and trust</li>
    <li><strong>Policy makers & advocates:</strong> Promote inclusive, safer digital spaces</li>
    <li><strong>Mental health professionals:</strong> Recognize privacy as part of well-being</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Toolkit Goals Section (可按需保留或修改) ---
st.markdown('<div class="goal-boxes">', unsafe_allow_html=True)
st.markdown("<h2>Toolkit Goals</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="goal-grid">
  <div class="goal-item">Help newcomers understand their privacy rights in Canada</div>
  <div class="goal-item">Provide tools for secure communication and online navigation</div>
  <div class="goal-item">Increase awareness of data collection and digital safety</div>
  <div class="goal-item">Reduce risks tied to scams, discrimination, or misinformation</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
