import streamlit as st
import pytesseract as pt
from PIL import Image

uploaded_file = st.file_uploader("Choose a Image")

pt.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"

if uploaded_file is not None:
    st.image(uploaded_file)
    st.write(pt.image_to_string(image=Image.open(uploaded_file)))
else:
    st.write("No Image Uploaded")
