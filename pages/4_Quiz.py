import streamlit as st
from sidebar import render_sidebar
from language import get_language

# 页面设置
st.set_page_config(page_title="Privacy Quiz", layout="wide")
lang = get_language()
render_sidebar()

# --- 样式 ---
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #F0F6FB !important;
        }
        body {
            font-family: 'Georgia', serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stRadio > div {
            background-color: #F0F6FB;
        }
    </style>
""", unsafe_allow_html=True)

# --- 标题 ---
if lang == "English":
    st.title("Privacy Knowledge Quiz")
    st.write("Answer the following 10 questions to test your understanding of privacy in Canada:")
else:
    st.title("隐私知识小测试")
    st.write("请回答以下 10 个问题，测试你对加拿大隐私知识的了解：")

# --- Quiz 内容（中英文） ---
quiz = [
    {
        "en": {
            "question": "Is it safe to share your SIN over email?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        "zh": {
            "question": "通过电子邮件分享你的社会保险号（SIN）安全吗？",
            "options": ["是", "否"],
            "answer": "否"
        }
    },
    {
        "en": {
            "question": "What does PIPEDA stand for?",
            "options": ["Personal Information Protection and Electronic Documents Act", "Privacy Info Policy for E-Docs"],
            "answer": "Personal Information Protection and Electronic Documents Act"
        },
        "zh": {
            "question": "PIPEDA 是什么的缩写？",
            "options": ["个人信息保护与电子文件法案", "电子隐私政策指南"],
            "answer": "个人信息保护与电子文件法案"
        }
    },
    {
        "en": {
            "question": "You receive a call from CRA asking for immediate payment. What should you do?",
            "options": ["Pay immediately", "Ignore and report the call"],
            "answer": "Ignore and report the call"
        },
        "zh": {
            "question": "你接到一个声称来自税局（CRA）要求立刻付款的电话，你该怎么办？",
            "options": ["立刻付款", "忽略并举报该电话"],
            "answer": "忽略并举报该电话"
        }
    },
    {
        "en": {
            "question": "Can companies collect personal data without consent?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        "zh": {
            "question": "公司可以在未经同意的情况下收集你的个人数据吗？",
            "options": ["是", "否"],
            "answer": "否"
        }
    },
    {
        "en": {
            "question": "Which is considered sensitive personal information?",
            "options": ["Favorite food", "Medical history"],
            "answer": "Medical history"
        },
        "zh": {
            "question": "下列哪项属于敏感的个人信息？",
            "options": ["最喜欢的食物", "病史"],
            "answer": "病史"
        }
    },
    {
        "en": {
            "question": "How should you manage multiple strong passwords?",
            "options": ["Use one strong password", "Use a password manager"],
            "answer": "Use a password manager"
        },
        "zh": {
            "question": "你应该如何管理多个强密码？",
            "options": ["使用一个通用的强密码", "使用密码管理器"],
            "answer": "使用密码管理器"
        }
    },
    {
        "en": {
            "question": "Which is a real Canadian fraud reporting agency?",
            "options": ["Canada Digital Safety Board", "Canadian Anti-Fraud Centre"],
            "answer": "Canadian Anti-Fraud Centre"
        },
        "zh": {
            "question": "下列哪个是真实存在的加拿大反诈骗机构？",
            "options": ["加拿大数字安全委员会", "加拿大反诈骗中心"],
            "answer": "加拿大反诈骗中心"
        }
    },
    {
        "en": {
            "question": "Is public Wi-Fi safe for banking?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        "zh": {
            "question": "使用公共 Wi-Fi 进行网银操作安全吗？",
            "options": ["是", "否"],
            "answer": "否"
        }
    },
    {
        "en": {
            "question": "Can you ask a company to delete your data in Canada?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },
        "zh": {
            "question": "你可以要求公司删除你在加拿大的数据吗？",
            "options": ["是", "否"],
            "answer": "是"
        }
    },
    {
        "en": {
            "question": "What does 2FA help with?",
            "options": ["Faster login", "Stronger security"],
            "answer": "Stronger security"
        },
        "zh": {
            "question": "双重验证（2FA）能带来什么好处？",
            "options": ["更快的登录", "更强的安全性"],
            "answer": "更强的安全性"
        }
    }
]

# --- Quiz 表单 ---
user_answers = []
score = 0

with st.form("quiz_form"):
    all_answered = True
    for i, q in enumerate(quiz):
        qdata = q["en"] if lang == "English" else q["zh"]
        user_answer = st.radio(
            f"{i+1}. {qdata['question']}",
            qdata["options"],
            index=None,
            key=f"question_{i}"
        )
        user_answers.append(user_answer)
        if user_answer is None:
            all_answered = False

    submit_label = "Submit Answers" if lang == "English" else "提交答案"
    submitted = st.form_submit_button(submit_label)

# --- 结果评估 ---
if submitted:
    if not all_answered:
        warning_text = "Please answer all questions before submitting." if lang == "English" else "请在提交前回答所有问题。"
        st.warning(warning_text)
    else:
        for i, q in enumerate(quiz):
            correct = q["en"]["answer"] if lang == "English" else q["zh"]["answer"]
            if user_answers[i] == correct:
                score += 1

        percent = (score / len(quiz)) * 100
        score_label = f"### Your Score: {score}/10 ({percent:.0f}%)" if lang == "English" else f"### 你的得分：{score}/10（{percent:.0f}%）"
        st.markdown(score_label)

        if percent < 50:
            msg = "Consider reviewing key privacy concepts and checking our resources." if lang == "English" else "建议你回顾一下核心隐私概念并查阅我们的资源。"
            st.warning(msg)
        elif percent < 80:
            msg = "Good start! You have a solid understanding, but there’s more to explore." if lang == "English" else "不错的开始！你已有一定了解，但还有进步空间。"
            st.info(msg)
        else:
            msg = "Excellent! You have a strong grasp of privacy and safety in Canada." if lang == "English" else "太棒了！你对加拿大的隐私与安全有很强的理解。"
            st.success(msg)
