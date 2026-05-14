import streamlit as st
import time

from src.database.db import update_student_voice
from src.pipelines.voice_pipeline import get_voice_embedding


@st.dialog("Voice Profile")
def voice_enroll_dialog():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    has_voice = bool(student_data.get('voice_embedding'))

    if has_voice:
        st.success("Your voice profile is registered. Re-record below to update it.")
    else:
        st.info(
            "Add your voice so teachers can mark you present from classroom audio. "
            "Speak clearly for a few seconds."
        )

    audio_data = None
    try:
        audio_data = st.audio_input(
            "Record a short phrase like 'I am present, my name is ...'"
        )
    except Exception:
        st.error("Could not access the microphone in this browser.")

    save_disabled = audio_data is None

    if st.button(
        "Save voice profile",
        type='primary',
        width='stretch',
        icon=':material/mic:',
        disabled=save_disabled,
    ):
        with st.spinner("Analyzing your voice..."):
            voice_emb = get_voice_embedding(audio_data.read())

        if not voice_emb:
            st.error("Couldn't extract voice features. Try a longer/clearer recording.")
            return

        try:
            response_data = update_student_voice(student_id, voice_emb)
        except Exception as e:
            st.error(f"Save failed: {e}")
            return

        if not response_data:
            st.error("Save failed: no row updated. Check your Supabase RLS policy on `students`.")
            return

        st.session_state.student_data = response_data[0]
        st.toast("Voice profile saved!", icon="🎙️")
        time.sleep(1)
        st.rerun()
