# home.py

import streamlit as st
from salesforce_connection import fetch_salesforce_data

st.set_page_config("AlmyAI - CX", layout="wide", initial_sidebar_state="collapsed")

def chunk_dataframe(dataframe, chunk_size):
    for i in range(0, len(dataframe), chunk_size):
        yield dataframe.iloc[i:i + chunk_size]

def calculate_total_pages(dataframe, limit_per_page):
    return (len(dataframe) - 1) // limit_per_page + 1

def initialize_session_state():
    if 'data_loaded' not in st.session_state:
        st.session_state.df = fetch_salesforce_data()
        st.session_state.total_pages = calculate_total_pages(st.session_state.df, 12)
        st.session_state.current_page = 1

def display_data():
    current_data = st.session_state.df.iloc[(st.session_state.current_page - 1) * 12 : st.session_state.current_page * 12]
    for chunk in chunk_dataframe(current_data, 3):
        cols = st.columns(4)
        for i, row in enumerate(chunk.itertuples()):
            with cols[i]:
                expander = st.expander(f"""Opportunity: {row.Name}
Expiration Date: {row.Delivery_Date__c}
90-Day Date: {row.CloseDate}
""")
                with expander:
                    st.write(row)
        for i in range(len(chunk), 4):
            with cols[i]:
                st.empty()

def main():
    initialize_session_state()
    st.title("Salesforce Data Display")

    st.session_state.current_page = st.number_input("Page", min_value=1, max_value=st.session_state.total_pages, value=1, step=1)

    display_data()

if __name__ == "__main__":
    main()
