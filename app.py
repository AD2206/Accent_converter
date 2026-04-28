import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile

st.set_page_config(
page_title="Accent Converter AI",
layout="centered"
)

st.title("Accent Converter AI")

st.markdown("""
This application converts spoken audio into text and generates speech in different English accents.
Upload an audio file, convert speech to text, and listen to the output in a selected accent.
""")

st.subheader("Tool")

accent = st.selectbox("Choose Accent", ["US", "UK", "India", "Australia"])

accents = {
"US": "com",
"UK": "co.uk",
"India": "co.in",
"Australia": "com.au"
}

audio_file = st.file_uploader("Upload WAV audio file", type=["wav"])

if audio_file is not None:

```
st.audio(audio_file)

r = sr.Recognizer()

try:
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    text = r.recognize_google(audio)

    st.subheader("Transcribed Text")
    st.write(text)

    st.subheader("Accent Output")

    tts = gTTS(text=text, lang='en', tld=accents[accent])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name)

except sr.UnknownValueError:
    st.error("Could not understand audio")
except sr.RequestError:
    st.error("API error or no internet")
```
