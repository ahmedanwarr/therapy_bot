import streamlit as st

# Streamlit UI for audio input and output
st.title('Therapy AI Bot')

# Audio input
st.header('Audio Input')
audio_file = st.audio_input()

# Text-based response
st.header('Text-based Response')
response = st.text_area('Response from the AI')

# Audio output
st.header('Audio Output')
if audio_file is not None:
    st.audio(audio_file, format='audio/wav') 