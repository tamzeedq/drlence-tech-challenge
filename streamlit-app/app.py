import streamlit as st
import torch
from PIL import Image

st.set_page_config(page_title="YOLO Object Detection", page_icon="🖼️", layout="wide")

st.title("Object Detection with YOLOv5")
st.write("""
            1. Upload an image to detect objects with bounding boxes
            2. Click 'Run Model' to see the detections
            3. View the detection summary below the images
            """)

@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

with st.spinner("Loading YOLOv5 model..."):
    model = load_model()

st.success("Model loaded!")

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

if st.button("Run Model", icon="🧠") and uploaded_file:
    img = Image.open(uploaded_file)
    results = model(img)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(img, width='content')
    
    with col2:
        st.subheader("Detections")
        st.image(results.render()[0], width='content') # render results with bounding boxes
    
    st.subheader("Detection Summary:")
    detections = results.pandas().xyxy[0]
    
    if len(detections) > 0:
        st.dataframe(detections[['name', 'confidence', 'xmin', 'ymin', 'xmax', 'ymax']])
    else:
        st.warning("No objects detected in the image.")