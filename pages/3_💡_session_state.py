import streamlit as st

if 'text_list' not in st.session_state:
    st.session_state.text_list = []

#text input
user_input = st.text_input("Enter some text")

#buttons
if st.button('Append'):
    st.session_state.text_list.append(user_input)
if st.button('Clear'):
    st.session_state.text_list = []

#display
st.write('Text List:', st.session_state.text_list)
st.write('session state:', st.session_state)


