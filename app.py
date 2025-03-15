import streamlit as st
from pydub import AudioSegment
import io

# 음높이 조절 함수
def change_pitch(audio, semitones):
    new_sample_rate = int(audio.frame_rate * (2.0 ** (semitones / 12.0)))
    return audio._spawn(audio.raw_data, overrides={"frame_rate": new_sample_rate}).set_frame_rate(44100)

# 피아노 키 설정 (C4 ~ C5)
PIANO_KEYS = {
    "C4": 0, "C#4": 1, "D4": 2, "D#4": 3, "E4": 4, "F4": 5,
    "F#4": 6, "G4": 7, "G#4": 8, "A4": 9, "A#4": 10, "B4": 11, "C5": 12
}

# UI 구성
st.title("🎹 가상 피아노 (음높이 조절)")
uploaded_file = st.file_uploader("사운드 파일을 업로드하세요 (MP3, WAV)", type=["mp3", "wav"])

if uploaded_file:
    audio = AudioSegment.from_file(uploaded_file)
    st.audio(uploaded_file, format="audio/wav")

    # 피아노 건반 UI 생성
    st.markdown("### 🏴‍☠️ 피아노 건반을 눌러보세요!")

    # 건반 배치 (Streamlit columns 활용)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

    # 피아노 키 버튼 생성
    for key, semitone in PIANO_KEYS.items():
        with locals()[f"col{semitone + 1}"]:
            if st.button(key):
                audio = change_pitch(audio, semitone)
                st.write(f"🎵 {key} (음높이 {semitone} 반음 조절)")
                st.audio(audio.export(format="wav").read(), format="audio/wav")

    # 다운로드 버튼 추가
    output_buffer = io.BytesIO()
    audio.export(output_buffer, format="wav")
    st.download_button(label="🎵 변경된 오디오 다운로드", data=output_buffer.getvalue(), file_name="modified_audio.wav", mime="audio/wav")
