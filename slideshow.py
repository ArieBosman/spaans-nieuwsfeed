import streamlit as st

st.set_page_config(layout="wide")
st.title("Slideshow: Sequence 01")

# Correcte URL met spatie als %20
video_url = "https://raw.githubusercontent.com/ArieBosman/spaans-nieuwsfeed/main/Sequence%2001.mp4"

# HTML-video embed met autoplay en loop
video_html = f"""
<video width="100%" autoplay loop muted controls>
  <source src="{video_url}" type="video/mp4">
  Je browser ondersteunt geen video.
</video>
"""

st.markdown(video_html, unsafe_allow_html=True)