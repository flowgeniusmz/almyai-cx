import streamlit as st
from master.login import login_form

client = login_form()

if st.session_state.authenticated:
    if st.session_state.username:
        st.success("Welcome")
        st.write("Hi")