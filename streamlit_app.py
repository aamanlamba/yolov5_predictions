import streamlit as st
import streamlit.web.cli as stcli
import os

st.title("Streamlit Layout")
st.header("Display image")
st.write("\n\n")
st.image("./street_image.jpg", caption="mountains", width=1024)
st.subheader("Display video")
st.write("\n\n")
video_file = open("./video.mp4", mode="rb").read()
st.video(video_file)
st.header("File Upload")
uploaded_file = st.file_uploader("Choose a File")
if uploaded_file is not None:
    details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize(bytes)": uploaded_file.size,
    }
    st.json(details)

    path = os.path.join("./uploads", uploaded_file.name)
    with open(path, mode="wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("File saved")
