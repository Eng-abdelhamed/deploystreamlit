import streamlit as st


if "text_list" not in st.session_state:
    st.session_state.text_list =[]


user_in = st.text_input("Enter String : ")
if st.button("Append"):
    st.session_state.text_list.append(user_in)
if st.button("Clear"):
    st.session_state.text_list=[]


st.write("TextList",st.session_state.text_list)