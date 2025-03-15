import streamlit as st
from pydub import AudioSegment
import io

# 음높이 조절 함수
def change_pitch(audio, semitones):
    new_sample_rate = int(audio.frame_rate * (2.0 ** (semitones / 12.0)))
    return audio._spawn(audio.raw_data, overrides={"frame_rate": new_sample_rate}).set_frame_rate(44100)

# 피아노 키 설정 (C4 ~ C5)
PIANO_KEYS = [
    ("C4", 0), ("C#4", 1), ("D4", 2), ("D#4", 3), ("E4", 4), ("F4", 5),
    ("F#4", 6), ("G4", 7), ("G#4", 8), ("A4", 9), ("A#4", 10), ("B4", 11), ("C5", 12)
]

# Streamlit UI
st.title("🎹 가상 피아노 (배포 지원)")

uploaded_file = st.file_uploader("🎵 사운드 파일을 업로드하세요 (MP3, WAV)", type=["mp3", "wav"])

if uploaded_file:
    audio = AudioSegment.from_file(uploaded_file)
    st.audio(uploaded_file, format="audio/wav")

     try:
        audio = AudioSegment.from_file(uploaded_file)  # 파일 로드
        st.audio(uploaded_file, format="audio/wav")
    except Exception as e:
        st.error(f"파일을 처리하는 도중 오류가 발생했습니다: {e}")

    # 가상 피아노 UI 만들기
    st.markdown("### 🎼 피아노 건반을 클릭해보세요!")

    # 피아노 건반을 2줄로 나누기
    white_keys = [key for key in PIANO_KEYS if "#" not in key[0]]
    black_keys = [key for key in PIANO_KEYS if "#" in key[0]]

    col_white = st.columns(len(white_keys))
    col_black = st.columns(len(black_keys))

    # 흰 건반 (C, D, E, F, G, A, B, C)
    for i, (key, semitone) in enumerate(white_keys):
        with col_white[i]:
            if st.button(key):
                modified_audio = change_pitch(audio, semitone)
                st.write(f"🎵 {key} 연주 중...")
                st.audio(modified_audio.export(format="wav").read(), format="audio/wav")

    # 검은 건반 (C#, D#, F#, G#, A#)
    for i, (key, semitone) in enumerate(black_keys):
        with col_black[i]:
            if st.button(key, help=f"{key} (반음)"):
                modified_audio = change_pitch(audio, semitone)
                st.write(f"🎵 {key} 연주 중...")
                st.audio(modified_audio.export(format="wav").read(), format="audio/wav")

    # 다운로드 버튼 추가
    output_buffer = io.BytesIO()
    modified_audio.export(output_buffer, format="wav")
    st.download_button(label="🎵 변경된 오디오 다운로드", data=output_buffer.getvalue(), file_name="modified_audio.wav", mime="audio/wav")
