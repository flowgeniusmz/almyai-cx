# initialize.py
import streamlit as st

def main():
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.authenticated = False
        st.session_state.data_loaded = False

        # Initialize session state variables for dataframes and pagination
        st.session_state.dfOpps = None
        st.session_state.dfUser = None
        st.session_state.dfContract = None
        st.session_state.dfOpps_CurrentPage = 1
        st.session_state.dfUser_CurrentPage = 1
        st.session_state.dfContract_CurrentPage = 1
        st.session_state.dfOpps_TotalPages = 0
        st.session_state.dfUser_TotalPages = 0
        st.session_state.dfContract_TotalPages = 0
