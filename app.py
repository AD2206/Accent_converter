import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile

# Page config

st.set_page_config(
page_title="Accent Converter AI",
page_icon="",
layout="centered"
)

st.title("🎤 Accent Converter AI")

st.markdown("""

## About This Application

This AI-powered tool converts spoken language into text and then generates speech in different English accents.

You can upload an audio file
It will convert speech to text
It converts the audio into desired accent.

---

## Our Purpose

It bridges the communication gap between people hailing from different regions.
Helps users learn a new language fastly and efficiently.
Helps tourists in different countries understand smoothly what the locals are saying.
""")

st.markdown("---")

st.subheader(" Features")

st.markdown("""

1. Simple and interactive UI
2. Uses powerful and reliable API for smooth functioning of the application
3. Supports multiple accents from around the world

---

## Supported Accents

* US English
* UK English
* Indian English
* Australian English
  """)

st.markdown("---")

# -----------------------------

# 🎛 MAIN TOOL SECTION

# -----------------------------

st.subheader(" Try the Tool")

accent = st.selectbox("Choose Accent", ["US 🇺🇸", "UK 🇬🇧", "India 🇮🇳", "Australia 🇦🇺"])

accents = {
"US 🇺🇸": "com",
"UK 🇬🇧": "co.uk",
"India 🇮🇳": "co.in",
"Australia 🇦🇺": "com.au"
}

audio_file = st.file_uploader(" Upload your WAV audio file", type=["wav"])

if audio_file is not None:

```
st.success(" File uploaded successfully")
st.audio(audio_file)

r = sr.Recognizer()

with st.spinner(" Processing audio..."):
    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        text = r.recognize_google(audio)

        st.markdown("###  Transcribed Text")
        st.info(text)

        st.markdown("###  Accent Output")

        tts = gTTS(text=text, lang='en', tld=accents[accent])

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name)

        st.success(" Done!")

    except sr.UnknownValueError:
        st.error(" Could not understand audio")
    except sr.RequestError:
        st.error(" API error / no internet")
```
