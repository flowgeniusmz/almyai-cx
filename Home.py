import streamtlit as st
from config import pagesetup as ps, sfdataloader as sfdc
import pandas as pd



st.set_page_config(page_title="MagicBook Creator", page_icon="🌐☁️", layout="wide", initial_sidebar_state="collapsed")

if "loadsfdata" not in st.session_state:
  st.toast("Loading SF data...")
  sfdc.get_sf_data()
  sfdata = sfdc.get_selected_dataset()
  st.toast("SF data loaded!")
  st.session_state.loadsfdata = True
  
ps.set_title("AlmyAI", "CX")

user = "Dominic Watson"
ps.get_blue_header(f"Welcome to AlmyAI - CX {user}")
st.markdown("Use the **tabs below** to access data and contract information")
st.divider()

tab_ExpiringContracts, tab_SendEmails, tab_AskAI = st.tabs(["Expiring Contracts", "Send Emails", "Ask AI"])

with tab_ExpiringContracts:
  ps.get_blue_header("Expiring Contracts")
  st.dataframe(sfdata)
with tab_SendEmails:
  ps.get_blue_header("Send Emails")

with tab_AskAI:
  ps.get_blue_header("Ask AI")
