import streamlit as st
from PIL import Image

img = Image.open("Foto/stralelotralala.jpg")
st.title("Grid")

# Defining no of Rows
for i in range(4):
    # Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
