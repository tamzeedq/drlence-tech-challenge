import streamlit as st
import torch
from PIL import Image

st.title("Object Detection with YOLOv5")
st.markdown("Upload an image to detect objects with bounding boxes")

@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_model()

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

if st.button("Run Model") and uploaded_file:
    img = Image.open(uploaded_file)
    results = model(img)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(img, use_container_width=True)
    
    with col2:
        st.subheader("Detections")
        st.image(results.render()[0], use_container_width=True) # render results with bounding boxes
    
    st.subheader("Detection Summary:")
    detections = results.pandas().xyxy[0]
    
    if len(detections) > 0:
        st.dataframe(detections[['name', 'confidence', 'xmin', 'ymin', 'xmax', 'ymax']])
    else:
        st.warning("No objects detected in the image.")