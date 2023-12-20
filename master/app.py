# app.py
import streamlit as st
import data

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

def display_data(dataframe):
    current_data = dataframe.iloc[(st.session_state.current_page - 1) * 12 : st.session_state.current_page * 12]
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

def main():
    st.title("Salesforce Data Display")

    # Display tabs for different dataframes
    tab_titles = ["Opportunities", "Users", "Contracts"]
    dataframes = [st.session_state.dfOpps, st.session_state.dfUser, st.session_state.dfContract]
    tabs = st.tabs(tab_titles)
    
    for i, tab in enumerate(tabs):
        with tab:
            st.session_state.current_page = st.number_input(f"Page {i+1}", min_value=1, max_value=calculate_total_pages(dataframes[i], 12), value=1, step=1)
            display_data(dataframes[i])

if __name__ == "__main__":
    main()
