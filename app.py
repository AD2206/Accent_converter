import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile

# Page config
st.set_page_config(
    page_title="Accent Converter AI",
    page_icon="🎤",
    layout="centered"
)


st.title("Accent Converter AI")

st.markdown("""
##  Our Purpose
This AI-powered tool converts spoken language into text and then generates speech in different English accents.

 Upload an audio file
 It converts speech to text 
 Play the audio in your desired accent

---

##  How can this tool be used?
 Our ai-powered tool can be used for learning new english accents.It also helps tourists visiting foreign
 countries.It bridges the communication gap between people hailing from different regions.

""")

st.markdown("---")


st.subheader(" Features")

st.markdown("""
 Speech-to-Text conversion using AI  
 Accent-based voice generation  
 Supports multiple English accents  
 Simple and interactive UI  

---

##  Supported Accents
 🇺🇸 US English  
 🇬🇧 UK English  
 🇮🇳 Indian English  
 🇦🇺 Australian English  
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

audio_file = st.file_uploader("Upload your WAV audio file", type=["wav"])

if audio_file is not None:

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
