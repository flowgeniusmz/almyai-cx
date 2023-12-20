# home.py

import streamlit as st
from salesforce_connection import fetch_salesforce_data
st.set_page_config("AlmyAI - CX", layout="wide", initial_sidebar_state="collapsed")

def chunk_dataframe(dataframe, chunk_size):
    for i in range(0, len(dataframe), chunk_size):
        yield dataframe.iloc[i:i + chunk_size]

def calculate_total_pages(dataframe, limit_per_page):
    return (len(dataframe) - 1) // limit_per_page + 1

def format_row_data(row):
    formatted_data = "<div>"
    for field in row._fields:
        if field not in ["Index", "attributes"]:  # Exclude specific fields
            value = getattr(row, field)
            if isinstance(value, dict) and 'Name' in value:
                value = value['Name']  # Extract 'Name' from nested objects
            elif isinstance(value, dict):
                continue  # Skip other complex nested objects
            formatted_data += f"<strong>{field.replace('_', ' ')}:</strong> {value}<br>"
    formatted_data += "</div>"
    return formatted_data

def display_data():
    current_data = st.session_state.df.iloc[(st.session_state.current_page - 1) * 12 : st.session_state.current_page * 12]
    for chunk in chunk_dataframe(current_data, 3):
        cols = st.columns(3)
        for i, row in enumerate(chunk.itertuples()):
            with cols[i]:
                expander_title = f"Opportunity: {row.Name}\nExpiration Date: {row.Delivery_Date__c}\n90-Day Date: {row.CloseDate}"
                expander = st.expander(expander_title)
                with expander:
                    st.write(format_row_data(row), unsafe_allow_html=True)
        for i in range(len(chunk), 3):
            with cols[i]:
                st.empty()

def initialize_session_state():
    if 'data_loaded' not in st.session_state:
        st.session_state.df = fetch_salesforce_data()
        st.session_state.total_pages = calculate_total_pages(st.session_state.df, 12)
        st.session_state.current_page = 1
        st.session_state.data_loaded = True

def main():
    initialize_session_state()
    st.title("Salesforce Data Display")

    st.session_state.current_page = st.number_input("Page", min_value=1, max_value=st.session_state.total_pages, value=1, step=1)

    display_data()

if __name__ == "__main__":
    main()
