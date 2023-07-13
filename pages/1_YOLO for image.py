import streamlit as st
import numpy as np
from yolo_predictions1 import YOLO_Pred
from PIL import Image

st.set_page_config(page_title = "YOLO Object Detection",
                   layout='wide',
                   page_icon='../images/object.png')
st.title('YOLO for Image Detection')
st.write('Provide Image for detection')

with st.spinner('loading model...'):
    # initialize YOLO class
    yolo = YOLO_Pred(onnx_model= '../models/best.onnx',
                    data_yaml = '../data.yaml')
    st.balloons()
    
def upload_image():
        # upload image
    image_file = st.file_uploader(label="Upload Image", type=["jpg","png"])
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        file_details = {"filename":image_file.name,
                        "filetype":image_file.type,
                        "filesize": "{:,.2f} MB".format(size_mb)}
        st.image(image_file,caption=image_file.name)
        return {"file":image_file,
                "details":file_details}

def main():
    object = upload_image()
    if object:
        image_obj = Image.open(object['file'])
        st.image(image_obj)
        image_array = np.array(image_obj)
        pred_image = yolo.predictions(image_array)
        st.image(pred_image)
    
    
if __name__ == "__main__":
    main()