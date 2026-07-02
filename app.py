import streamlit as st
from roast_engine import smart_sentiment_roast
from compliment_engine import sweet_sentiment_compliment
import time

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="MoodSwing",
    page_icon="🌀",
    layout="centered",
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
<style>

/* Main content */

.block-container{
    max-width:850px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Hero */

.title{
    text-align:center;
    font-size:3rem;
    font-weight:800;
    color:#CDB4DB;
    margin-bottom:0.2rem;
}

.subtitle{
    text-align:center;
    font-size:1.05rem;
    opacity:0.85;
    margin-bottom:2rem;
}

/* Buttons */

.stButton > button{
    width:100%;
    border-radius:10px;
    font-weight:700;
    padding:0.75rem;
}

/* Inputs */

.stTextInput input{
    border-radius:10px;
}

textarea{
    border-radius:10px;
}

/* History card */

.history-card{
    border:1px solid rgba(128,128,128,.20);
    border-radius:12px;
    padding:1rem;
    margin-bottom:1rem;
}

.footer{
    text-align:center;
    opacity:.75;
    margin-top:2rem;
    font-size:.9rem;
}

</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("🧭 How It Works")

    st.markdown(
        """
1. Choose **Roast** or **Compliment**

2. Adjust the **Mood Override** slider

3. Enter your message

4. Click **Generate Response**

---

🌀 **MoodSwing** analyzes the sentiment of your text and responds with either a playful roast or a thoughtful compliment.

💡 Try different mood values to see how the response changes.

🧠 Built with **TextBlob** and **Streamlit**.

---
👨‍💻 Created by **Harsham Irfan**
"""
    )

# --------------------------------------------------
# Hero
# --------------------------------------------------

st.markdown(
    """
<div class="title">
🌀 MoodSwing
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="subtitle">
<b>Your Sass or Sweetness Bot</b><br>
Analyze the sentiment behind your text and receive either a playful roast or a thoughtful compliment.
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Interaction Area
# --------------------------------------------------

st.markdown("### 🎭 Choose Your Experience")

mode = st.radio(
    "",
    ["🔥 Roast Me", "🌸 Compliment Me"],
    horizontal=True,
)

st.markdown("")

mood = st.slider(
    "Mood Override",
    min_value=-1.0,
    max_value=1.0,
    value=0.0,
    step=0.1,
    help="Override the detected sentiment with your preferred mood."
)

user_input = st.text_area(
    "💬 What's on your mind?",
    placeholder="Type a message, thought, confession, or anything you'd like MoodSwing to react to...",
    height=140,
)

generate = st.button(
    "✨ Generate Response",
    use_container_width=True,
)

# --- Response Generation ---
def typewriter_effect(text, delay=0.03):
    """Simulate typewriter animation"""
    message = ""
    placeholder = st.empty()
    for char in text:
        message += char
        placeholder.info(message)
        time.sleep(delay)

if generate:
    if mode == "🔥 Roast Me":
        response = smart_sentiment_roast(user_input, override_sentiment=mood)
        st.markdown("## 🔥 Roast")

        response_container = st.container()

        with response_container:
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
        st.markdown("## 🌸 Compliment")

        response_container = st.container()

        with response_container:
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
st.markdown("---")

if st.session_state.history:

    st.markdown("## 📜 Interaction History")

    for mtype, mood, user_text, result in reversed(st.session_state.history):

        st.markdown(
            f"""
<div class="history-card">

### {"🔥 Roast" if mtype=="Roast" else "🌸 Compliment"}

**Mood Override:** `{mood:+.2f}`

**You**

> {user_text}

**MoodSwing**

> {result}

</div>
""",
            unsafe_allow_html=True,
        )

st.markdown(
    """
<div class="footer">

🧠 Powered by TextBlob • Built with Streamlit

</div>
""",
    unsafe_allow_html=True,
)


