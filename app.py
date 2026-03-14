import streamlit as st
from groq import Groq

# -------------------------
# AI Persona
# -------------------------

AI_PERSONA = """
You are an elite AI technical mentor teaching someone named Dheebu.

Communication style:
• Address the learner as "Dheebu"
• Friendly, intelligent, slightly charismatic
• Encourage curiosity
• Explain deeply but intuitively

Structure responses:

1. Concept Explanation
2. Intuition
3. Technical Breakdown
4. Practical Example
5. Interview Insight
"""

# -------------------------
# Streamlit Config
# -------------------------

st.set_page_config(page_title="You got it, dear", layout="wide")

import random

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Lato:wght@300;400&display=swap');

/* ── BASE ── */
.stApp {
    background: linear-gradient(160deg, #130008 0%, #0a0005 55%, #150009 100%);
    font-family: 'Lato', sans-serif;
    color: #f2d4dc;
}

/* ── FLOATING HEART ANIMATION ── */
@keyframes riseUp {
    0%   { transform: translateY(0) rotate(45deg) scale(1);    opacity: 0.55; }
    60%  { opacity: 0.35; }
    100% { transform: translateY(-105vh) rotate(45deg) scale(0.7); opacity: 0; }
}
.heart-float {
    position: fixed;
    bottom: -40px;
    z-index: 0;
    pointer-events: none;
    animation: riseUp linear infinite;
}
.heart-float::before, .heart-float::after {
    content: "";
    position: absolute;
    border-radius: 50%;
}

/* ── TYPOGRAPHY ── */
h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.6rem !important;
    font-weight: 300 !important;
    color: #ffc8d4 !important;
    letter-spacing: 3px !important;
    text-align: center !important;
    margin-bottom: 0 !important;
}
h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 400 !important;
    color: #ffb3c1 !important;
    letter-spacing: 1.5px !important;
}
h4, h5, h6 { color: #f2d4dc !important; }
p, span, label, div { color: #f2d4dc !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1c0010 0%, #0d0008 100%) !important;
    border-right: 1px solid rgba(255,120,145,0.18) !important;
}
[data-testid="stSidebar"] * { color: #f2d4dc !important; }
[data-testid="stSidebar"] label {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1rem !important;
    letter-spacing: 1px !important;
    color: #ffc8d4 !important;
}

/* ── INPUTS ── */
input, textarea {
    background: rgba(255, 90, 120, 0.07) !important;
    border: 1px solid rgba(255, 110, 140, 0.3) !important;
    border-radius: 10px !important;
    color: #f2d4dc !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255, 90, 120, 0.07) !important;
    border: 1px solid rgba(255, 110, 140, 0.3) !important;
    border-radius: 10px !important;
    color: #f2d4dc !important;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: rgba(255, 60, 90, 0.06) !important;
    border: 1px solid rgba(255, 110, 140, 0.14) !important;
    border-radius: 14px !important;
    padding: 0.5rem 1rem !important;
    margin: 5px 0 !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"], [data-testid="stChatInput"] > div {
    background: rgba(255, 60, 90, 0.07) !important;
    border: 1px solid rgba(255, 110, 140, 0.28) !important;
    border-radius: 30px !important;
}
[data-testid="stChatInput"] textarea { border: none !important; background: transparent !important; }

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, rgba(185,25,60,0.75), rgba(130,8,40,0.85)) !important;
    border: 1px solid rgba(255, 110, 140, 0.4) !important;
    border-radius: 30px !important;
    color: #ffe4eb !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1rem !important;
    letter-spacing: 0.6px !important;
    padding: 0.4rem 1.8rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 0 0 rgba(255,80,110,0) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(215,40,75,0.9), rgba(160,15,50,0.95)) !important;
    box-shadow: 0 0 18px rgba(255, 80, 110, 0.38) !important;
    transform: translateY(-1px) !important;
}

/* ── DIVIDER ── */
hr { border-color: rgba(255, 110, 140, 0.18) !important; margin: 1.6rem 0 !important; }

/* ── ALERT / INFO BOX ── */
.stAlert {
    background: rgba(255, 60, 90, 0.08) !important;
    border: 1px solid rgba(255, 110, 140, 0.22) !important;
    border-radius: 12px !important;
    color: #f2d4dc !important;
}

/* ── SPINNER ── */
.stSpinner > div { border-top-color: #ff6080 !important; }

/* ── CAPTION ── */
[data-testid="stCaptionContainer"] p {
    color: rgba(242, 212, 220, 0.55) !important;
    font-style: italic !important;
    text-align: center !important;
    letter-spacing: 1.5px !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,100,130,0.25); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Animated floating hearts ──

hearts_html = ""

for i in range(14):
    size   = random.randint(10, 28)
    left   = random.randint(0, 100)
    dur    = random.uniform(10, 22)
    delay  = random.uniform(0, 12)
    op     = random.uniform(0.18, 0.45)

    hearts_html += f"""
    <div class="heart-float" style="
        width:{size}px; height:{size}px;
        left:{left}vw;
        animation-duration:{dur:.1f}s;
        animation-delay:-{delay:.1f}s;
        background:linear-gradient(145deg,#ff3358,#ff7090);
        box-shadow:0 0 {size}px rgba(255,50,80,0.35);
        opacity:{op:.2f};
    ">
    <style>
    .heart-float:nth-child({i+1})::before,
    .heart-float:nth-child({i+1})::after {{
        width:{size}px; height:{size}px;
        background:linear-gradient(145deg,#ff3358,#ff7090);
    }}
    .heart-float:nth-child({i+1})::before {{ top:-{size//2}px; left:0; }}
    .heart-float:nth-child({i+1})::after  {{ left:-{size//2}px; top:0; }}
    </style>
    </div>"""

st.markdown(hearts_html, unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; padding: 1.2rem 0 0.2rem;'>
    <span style='font-size:1.4rem; color:rgba(255,140,160,0.5); letter-spacing:8px;'>♡ &nbsp; ♡ &nbsp; ♡</span>
</div>
""", unsafe_allow_html=True)

st.title("Your AI Learning Companion")
st.caption("crafted with love, just for you, Dheebu")

# -------------------------
# Session State
# -------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "quiz_history" not in st.session_state:
    st.session_state.quiz_history = []

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Beginner"

if "last_ai_answer" not in st.session_state:
    st.session_state.last_ai_answer = ""

# -------------------------
# Topics
# -------------------------

topics = {
    "Python Fundamentals": [
        "Variables",
        "Control Flow",
        "Functions",
        "OOP",
        "File Handling"
    ],
    "FastAPI": [
        "Routing",
        "Pydantic Models",
        "Dependency Injection",
        "Authentication"
    ],
    "React": [
        "Components",
        "Hooks",
        "State",
        "API Calls"
    ],
    "Machine Learning": [
        "Regression",
        "Classification",
        "Model Evaluation"
    ],
}

# -------------------------
# Sidebar
# -------------------------

api_key = st.sidebar.text_input("Groq API Key", type="password")

if not api_key:
    st.info("Enter Groq API Key to start")
    st.stop()

client = Groq(api_key=api_key)

topic = st.sidebar.selectbox("Choose Topic", list(topics.keys()))

st.markdown(f"""
<div style='margin-top:1rem;'>
    <p style='font-family:Cormorant Garamond,serif; font-size:1.1rem; letter-spacing:1.5px;
              color:#ffc8d4; border-bottom:1px solid rgba(255,110,140,0.2); padding-bottom:6px;
              margin-bottom:10px;'>✦ {topic}</p>
    {''.join(f"""<div style='padding:4px 12px; margin:4px 0; border-left:2px solid rgba(255,110,140,0.4);
        border-radius:0 8px 8px 0; background:rgba(255,60,90,0.06); font-size:0.9rem;'>{i}. {item}</div>"""
        for i, item in enumerate(topics[topic], 1))}
</div>
""", unsafe_allow_html=True)

# -------------------------
# AI Tutor Chat
# -------------------------

st.divider()
st.header("✦ Chat with your Tutor")

# Show previous messages

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input

user_message = st.chat_input("Ask anything, Dheebu...")

if user_message:

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_message
    })

    with st.spinner("thinking for you..."):

        prompt = f"""
Topic: {topic}

Question from Dheebu:
{user_message}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": AI_PERSONA},
                *st.session_state.chat_history,
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        answer = response.choices[0].message.content

    st.session_state.last_ai_answer = answer

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

# -------------------------
# Quiz Me On This Feature
# -------------------------

st.divider()
st.header("✦ Quiz Me On This")

if st.session_state.last_ai_answer != "":

    if st.button("Quiz me on what I just learned  ♡"):

        prompt = f"""
Dheebu just learned this concept:

{st.session_state.last_ai_answer}

Create ONE quiz question that tests Dheebu's understanding.

Rules:
- Multiple choice
- 4 options
- Include correct answer
- Include explanation
"""

        with st.spinner("crafting a challenge just for you..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": AI_PERSONA},
                    {"role": "user", "content": prompt}
                ]
            )

            quiz = response.choices[0].message.content

        st.markdown("### ✦ Your Challenge, Dheebu")
        st.markdown(quiz)

# -------------------------
# Adaptive Quiz
# -------------------------

st.divider()
st.header("✦ Adaptive Quiz")

st.markdown(f"<p style='color:rgba(242,212,220,0.7); font-style:italic;'>difficulty · <strong style='color:#ffc8d4;'>{st.session_state.difficulty}</strong></p>", unsafe_allow_html=True)

if st.button("Generate a question for me  ♡"):

    prompt = f"""
Generate ONE quiz question about {topic}.

Difficulty: {st.session_state.difficulty}

Format:

Question
A
B
C
D
Correct Answer
Explanation to Dheebu
"""

    with st.spinner("preparing something special for you..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": AI_PERSONA},
                {"role": "user", "content": prompt}
            ]
        )

        question = response.choices[0].message.content

    st.session_state.quiz_history.append(question)

# Display last quizzes

for q in st.session_state.quiz_history[-3:]:
    st.markdown("---")
    st.markdown(q)

# -------------------------
# Adaptive Difficulty Logic
# -------------------------

if len(st.session_state.quiz_history) > 3:

    if st.session_state.difficulty == "Beginner":
        st.session_state.difficulty = "Intermediate"

    elif st.session_state.difficulty == "Intermediate":
        st.session_state.difficulty = "Advanced"