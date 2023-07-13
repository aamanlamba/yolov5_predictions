import streamlit as st
import os, yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Home", layout="wide", page_icon="./images/home.png")
st.title("YOLO v5 Object Detection App")
st.caption("Web app to demonstrate YOLO V5 Object detection in images and videos")
with open('data.yaml',mode='r') as f:
    data_yaml = yaml.load(f,Loader=SafeLoader)
    
labels = data_yaml['names']

# Content
st.markdown("""YOLO Object Detection
### Detect objects from images
- Objects detected:
""")
st.write(labels)
st.markdown(
"""
- [Detect objects in image](/YOLO_for_image/)

"""
)