import streamlit as st
import login
import data
import initialize

st.set_page_config(page_title="AlmyAI-CX", page_icon="🌐☁️", layout="wide", initial_sidebar_state="collapsed")

### LOGIN
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login.main()
else:
### DATA
    dfOpps, dfUser, dfContract = data.main()



