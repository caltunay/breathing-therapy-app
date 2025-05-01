import streamlit as st
import time

st.set_page_config(page_title="Nefes Terapisi", layout="centered")
st.title("🧘‍♀️ Nefes Egzersizi")

col1, col2 = st.columns(2)
breath_duration = col1.slider("Nefes alma/verme süresi (saniye)", 1, 10, 1)
hold_duration = col2.slider("Nefesi tutma süresi (saniye)", 0, 5, 0)

circle = st.empty()
label = st.empty()

st.markdown("---")  # layout

# Animation frames
frame_rate = 60

# Total frames for the animation
total_frames = int(breath_duration * frame_rate)

# Generate smooth size steps
steps = [50 + (150 * i / total_frames) for i in range(total_frames)]  # from 50 to 200 px
delay = 1 / frame_rate  # Delay per frame

while True:
    # Nefes Al
    label.markdown("### 🌬️ Nefes Al...")
    for size in steps:
        circle.markdown(f"""
        <div style='width:{size}px;height:{size}px;
        border-radius:50%;background-color:#4CAF50;
        margin:auto;'></div>""", unsafe_allow_html=True)
        time.sleep(delay)
    time.sleep(hold_duration)

    # Nefes Ver
    label.markdown("### 😮‍💨 Nefes Ver...")
    for size in reversed(steps):
        circle.markdown(f"""
        <div style='width:{size}px;height:{size}px;
        border-radius:50%;background-color:#2196F3;
        margin:auto;'></div>""", unsafe_allow_html=True)
        time.sleep(delay)
    time.sleep(hold_duration)
