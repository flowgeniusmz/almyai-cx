import streamlit as st
from config import pagesetup as ps, sfdataloader as sfdc
import pandas as pd
import json
from st_aggrid import AgGrid, GridUpdateMode, JsCode, GridOptionsBuilder




st.set_page_config(page_title="MagicBook Creator", page_icon="🌐☁️", layout="wide", initial_sidebar_state="collapsed")

if "loadsfdata" not in st.session_state:
  st.toast("Loading SF data...")
  sfdc.load_sf_data()
  st.toast("SF data loaded!")
  st.session_state.loadsfdata = True
  
ps.set_title("AlmyAI", "CX")

user = "Dominic Watson"
useremail = "dominic.watson@almalasers.com"
ps.set_blue_header(f"Welcome to AlmyAI - CX")
ps.set_green_header(f"{user} ({useremail})")
st.markdown("Use the **tabs below** to access data and contract information")
st.divider()

tab_ExpiringContracts, tab_SendEmails, tab_AskAI = st.tabs(["Expiring Contracts", "Send Emails", "Ask AI"])

with tab_ExpiringContracts:
  ps.set_blue_header("Expiring Contracts")
  df = sfdc.get_sf_contracts_df()
  #df_contracts = st.dataframe(df)
  edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic",
    key = "editeddf"
  )
  with st.expander("Edited Data"):
        st.write(f"Type: {type(edited_df)}")
        json_data = edited_df.to_json(orient='records', lines=False)
        st.json(json_data)
with tab_SendEmails:
  ps.set_blue_header("Send Emails")
  #ps.set_green_header("Data")
  df1 = sfdc.get_sf_contracts_df()
  AgGrid(df1, editable=True)
with tab_AskAI:
  ps.set_blue_header("Ask AI")
  df = sfdc.get_sf_contracts_df()
  #display = sfdc.displaycontainers(df)
  #display = sfdc.displaycontainers1(df, 4)
  display = sfdc.displaycontainers2(df)
