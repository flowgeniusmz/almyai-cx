import streamtlit as st
from config import pagesetup as ps


st.set_page_config(page_title="MagicBook Creator", page_icon="🌐☁️", layout="wide", initial_sidebar_state="collapsed")
ps.set_title("AlmyAI", "CX")

user = "Dominic Watson"
ps.get_blue_header(f"Welcome to AlmyAI - CX {user}")
st.markdown("Use the **tabs below** to access data and contract information")
st.divider()

tab_ExpiringContracts, tab_SendEmails, tab_AskAI = st.tabs(["Expiring Contracts", "Send Emails", "Ask AI"])

with tab_ExpiringContracts:
  ps.get_blue_header("Expiring Contracts")

with tab_SendEmails:
  ps.get_blue_header("Send Emails")

with tab_AskAI:
  ps.get_blue_header("Ask AI")
