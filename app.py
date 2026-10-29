# pip install streamlit  

import streamlit as st 
st.title("My First Streamlit App")

st.write("Welcome! This app calculates the square of a number.") 

st.header("Select a Number")
number = st.slider("Pick a number", 0, 100, 25)

if st.button("Calculate Square"): 
    squared_number = number * number
    st.subheader("Result")
    st.write(f"The square of *{number}* is *{squared_number}*.")
