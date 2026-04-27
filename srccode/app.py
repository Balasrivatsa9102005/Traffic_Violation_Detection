import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Helmet Detection", layout="centered")

st.title("Helmet Detection System")
st.caption("AI-based traffic rule enforcement")

#use your model path
@st.cache_resource
def load_model():
    return YOLO(
        r"C:\Use\your_path\yolo_traffic\helmet_detection3\weights\best.pt"
    )

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Detect Helmet"):
        with st.spinner("Running YOLO..."):
            results = model.predict(img_np, conf=0.5)

        annotated = results[0].plot()
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        st.image(
            annotated,
            caption="Detection Result",
            use_container_width=True
        )

        names = results[0].names
        boxes = results[0].boxes

        helmet = False
        no_helmet = False

        for box in boxes:
            cls = int(box.cls[0])
            label = names[cls]

            if label == "With Helmet":
                helmet = True
            elif label == "Without Helmet":
                no_helmet = True

        st.divider()

        if no_helmet and not helmet:
            st.error(" PENALTY: Rider without helmet detected")
        else:
            st.success(" SAFE: Helmet compliance detected")
