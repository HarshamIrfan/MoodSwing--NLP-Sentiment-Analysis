import streamlit as st
from roast_engine import smart_sentiment_roast
from compliment_engine import sweet_sentiment_compliment
import time

# --- Page Setup ---
st.set_page_config(page_title="MoodSwing", page_icon="🌀", layout="wide")

# --- Session State for History ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Theme Toggle ---
theme = st.sidebar.selectbox("🌓 Theme", ["🌚 Dark", "🌞 Light"])

if theme == "🌞 Light":
    bg_color = "linear-gradient(135deg, #fef6e4, #fce1e4, #f7cdef, #eebbee, #dcb4eb)"
    container_color = "rgba(255, 255, 255, 0.95)"
    text_color = "#1e1e1e"
    button_color = "#f7cdef"
else:
    bg_color = "linear-gradient(135deg, #1e1e2f, #2c2b3c)"
    container_color = "rgba(34, 34, 34, 0.95)"
    text_color = "#E6E6E6"
    button_color = "#3a3a5c"

# --- Custom Styling ---
st.markdown(
    f"""
<style>
.stApp {{
    background: {bg_color};
    background-attachment: fixed;
    background-size: cover;
}}

.block-container {{
    max-width: 900px;
    background: {container_color};
    padding: 2.8rem;
    border-radius: 18px;
    margin-top: 2rem;
    box-shadow: 0 12px 30px rgba(0,0,0,.18);
}}

.title-text {{
    text-align:center;
    font-size:3rem;
    font-weight:800;
    color:#CDB4DB;
    margin-bottom:0.2rem;
}}

.subtitle-text {{
    text-align:center;
    font-size:1.05rem;
    color:{text_color};
    margin-bottom:2rem;
}}

h1,h2,h3,h4,h5,h6,p,span,label,div {{
    color:{text_color} !important;
}}

section[data-testid="stSidebar"] * {{
    color:{text_color} !important;
}}

.stTextInput input {{
    border-radius:10px;
    color:{text_color} !important;
    background:{container_color} !important;
}}

.stButton>button {{
    width:100%;
    border:none;
    border-radius:12px;
    padding:.75rem;
    font-weight:700;
    background:{button_color};
    color:{text_color};
    transition:.2s;
}}

.stButton>button:hover {{
    transform:translateY(-1px);
    opacity:.95;
}}

div[role="radiogroup"] {{
    padding:0.5rem 0;
}}
</style>
""",
    unsafe_allow_html=True
)

# --- Sidebar ---
with st.sidebar:
    st.header("🧭 How It Works")
    st.markdown("""
    1. Choose your **vibe**: roast or compliment 🔥🌸
    2. Adjust your **mood slider** 😢 → 😐 → 😊
    3. Type your thoughts below ✏️
    4. Click **Generate Response** 🎭

    ---
    🌀 **MoodSwing** is an NLP-powered sass & sweetness bot for your emotional rollercoaster.

    💡 Tip: Try negative mood in compliment mode... or vice versa 😈

    🧠 Powered by TextBlob, Streamlit, and late-night debugging.
    """)
    st.markdown("👨‍💻 Created by [HarshamIrfan](https://github.com/HarshamIrfan)")

# --- Main Title ---
st.markdown("<div class='title-text'>🌀 MoodSwing</div>", unsafe_allow_html=True)
st.markdown(
    f"<div class='subtitle-text'><strong>Your Sass or Sweetness Bot</strong><br>Analyze the sentiment of your text and receive either a playful roast or a thoughtful compliment.</div>",
    unsafe_allow_html=True,
)

# --- Mode Selection ---
mode = st.radio("\nChoose your mode:", ["🔥 Roast Me", "🌸 Compliment Me"], horizontal=True)

# --- Mood Slider ---
mood = st.slider("Mood Override", -1.0, 1.0, 0.0, step=0.1, help="Override the sentiment detection with your own mood")

# --- User Input ---
user_input = st.text_input("💬 Tell MoodSwing what\'s on your mind...")

# --- Response Generation ---
def typewriter_effect(text, delay=0.03):
    """Simulate typewriter animation"""
    message = ""
    placeholder = st.empty()
    for char in text:
        message += char
        placeholder.markdown(f"```\n{message}\n```")
        time.sleep(delay)

if st.button("Generate Response 🎭"):
    if mode == "🔥 Roast Me":
        response = smart_sentiment_roast(user_input, override_sentiment=mood)
        st.markdown(f"### 🔥 Your Roast:")
        typewriter_effect(response)

        # Add to history
        st.session_state.history.append(("Roast", mood, user_input, response))

        # Roast GIFs
        if mood > 0.3:
            st.image("https://media1.tenor.com/m/PzY75riTLG0AAAAd/cat-yoongi.gif")
        elif mood < -0.1:
            st.image("https://media1.tenor.com/m/AhfDbzzEIA8AAAAd/qc-got.gif")
        else:
            st.image("https://media1.tenor.com/m/gaEpIfzxzPEAAAAd/pedro-monkey-puppet.gif")

    else:
        response = sweet_sentiment_compliment(user_input, override_sentiment=mood)
        st.markdown(f"### 🌸 Your Compliment:")
        typewriter_effect(response)

        # Add to history
        st.session_state.history.append(("Compliment", mood, user_input, response))

        # Compliment GIFs
        if mood > 0.3:
            st.image("https://media1.tenor.com/m/m98IlNDRa90AAAAd/snoop-dogg-happy.gif")
        elif mood < -0.1:
            st.image("https://media1.tenor.com/m/fQcCh4zbzDEAAAAd/thanxy.gif")
        else:
            st.image("https://media1.tenor.com/m/8zD-n1GzyUcAAAAd/sigma-detected-respect.gif")

# --- Footer ---
st.markdown("---")

# --- History Log ---
if st.session_state.history:
    st.markdown("### 📜 Interaction History")
    for i, (mtype, mood, user_text, result) in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**{mtype}** | Mood: `{mood:+.2f}` | Input: _{user_text}_")
        st.markdown(f"\> {result}")
        st.markdown("---")

st.caption("🧠 Powered by TextBlob | ✨ Designed with Streamlit | ☕ Fuelled by caffeine")
