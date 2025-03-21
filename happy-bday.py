import streamlit as st
import base64

# Function to play audio
def play_audio(audio_file):
    with open(audio_file, "rb") as audio:
        audio_bytes = audio.read()
        b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Streamlit UI
if st.button("Click to Celebrate! 🎶"):
    st.title("🎉 Happy Birthday App 🎂")

    # Show an image inside a box
    st.image("pandu.jpeg", caption="🎂 Have a wonderful birthday! 🎁",width=200)


    st.subheader("🎊 Happy Birthday to You! 🎊")
    play_audio("bday.mp3")
