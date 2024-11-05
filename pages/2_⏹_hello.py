import time

import streamlit as st

st.header("Shapes Calculations")
st.sidebar.title("Configuration")
with st.sidebar:
    shape = st.selectbox("Choose a shape : ", ("Circle", "Rectangle"))
    print(shape)

area = None
perimeter = None
if shape == "Circle":
    radius = st.number_input("Radius :",min_value=0,max_value=100, step=1)
    area = radius * radius * 3.14
    perimeter = 2 * 3.14 * radius

if shape == "Rectangle":
    width = st.number_input("width :",0., step=0.1)
    heigth = st.number_input("heigth :",0., step=0.1)
    area = width * heigth
    perimeter = 2 * (width + heigth)

compute_btn = st.button("Compute Area and Perimeter")
if compute_btn:
    with st.spinner("Computing ..."):
        time.sleep(2)
        st.write("Area :",area)
        st.write("Perimeter :",perimeter)