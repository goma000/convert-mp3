from moviepy.video.io.VideoFileClip import VideoFileClip
import streamlit as st
import os

# タイトル表示
st.title("MP4/MOV to MP3 Converter")

# ファイルアップロードセクション
uploaded_file = st.file_uploader("Upload MP4 or MOV File", type=["mp4", "mov"])

# ファイルがアップロードされたら処理を実行
if uploaded_file is not None:
    # 一時ファイルとして保存
    temp_file = "temp_video." + uploaded_file.name.split(".")[-1]
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"'{uploaded_file.name} をアップロードしました!")
    
    # MP3への変換
    try:
        st.info("MP3に変換中...")
        output_file = "output_audio.mp3"
        video = VideoFileClip(temp_file)
        video.audio.write_audiofile(output_file, codec='libmp3lame')

        st.success("変換に成功しました!ダウンロードボタンからmp3ファイルをダウンロードしてください")
        # ダウンロードリンク表示
        with open(output_file, "rb") as f:
            st.download_button(label="Download MP3 File", data=f, file_name="output_audio.mp3", mime="audio/mp3")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # 一時ファイルの削除
        os.remove(temp_file)
        if os.path.exists(output_file):
            os.remove(output_file)
