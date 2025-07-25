import streamlit as st

# Menampilkan gambar, audio, dan video
st.image("unsada_logo.jpg")
st.audio("my_audio.mp3")
st.video("my_video.mp4")

# Menampilkan video loop dari URL menggunakan HTML
video_html = """
<video controls width="700" autoplay muted loop>
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/mp4" />
</video>
"""
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(video_html, unsafe_allow_html=True)

# Menampilkan gambar di tengah menggunakan tiga kolom
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("unsada_logo.jpg")
with col3:
    st.write(" ")
