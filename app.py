import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

st.title("MP4 to MP3 Converter")

# ファイルアップロード
uploaded_file = st.file_uploader("Upload MP4 File", type=["mp4"])

if uploaded_file is not None:
    # 一時ファイルに保存
    temp_file = "temp_video.mp4"
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File Uploaded Successfully!")
    
    # 変換処理
    try:
        st.info("Converting to MP3...")
        output_file = "output_audio.mp3"
        video = VideoFileClip(temp_file)
        video.audio.write_audiofile(output_file, codec='libmp3lame')
        
        # ダウンロードリンク表示
        with open(output_file, "rb") as f:
            st.download_button(label="Download MP3", data=f, file_name="output_audio.mp3", mime="audio/mp3")
        
        st.success("Conversion Successful!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # 一時ファイルの削除
        os.remove(temp_file)
        if os.path.exists(output_file):
            os.remove(output_file)
