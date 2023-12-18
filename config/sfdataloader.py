import streamlit as st
from simple_salesforce import Salesforce 
import pandas as pd

@st.cache_resource
def get_sf_connection():
  sfUser = st.secrets.salesforce.sfuser
  sfpw = st.secrets.salesforce.sfcred
  sftoken = st.secrets.salesforce.sftoken
  sf = Salesforce(username=sfUser, password=sfpw, security_token=sftoken)
  return sf

@st.cache_data
def get_sf_users_df():
    varSF = get_sf_connection()
    query = "SELECT Id, Username, LastName, FirstName, Name, Email FROM User WHERE Subsidiary__c = 'Alma Lasers , Inc.'"
    data = varSF.query(query)
    records = data['records']
    df = pd.DataFrame(columns=['Id', 'Username', 'LastName', 'FirstName', 'Name', 'Email'])
    for record in records:
        row_data = {
            'Id': record['Id'],
            'Username': record['Username'],
            'LastName': record['LastName'],
            'FirstName': record['FirstName'],
            'Name': record['Name'],
            'Email': record['Email']
        }
        df = df.append(row_data, ignore_index=True)
    return df

@st.cache_data
def get_sf_contracts_df():
  varSF = get_sf_connection()
  query = "SELECT Id, AccountId, Account.Name, StartDate, EndDate, BillingStreet, BillingCity, BillingState, BillingPostalCode, BillingCountry, BillingStateCode, BillingCountryCode, BillingLatitude, BillingLongitude, BillingGeocodeAccuracy, BillingAddress, ShippingStreet, ShippingCity, ShippingState, ShippingPostalCode, ShippingCountry, ShippingStateCode, ShippingCountryCode, ShippingLatitude, ShippingLongitude, ShippingGeocodeAccuracy, ShippingAddress, ContractTerm, OwnerId, Owner.Name, Status, Asset__c, Serial_Number__c, BP__c, Product_Name__c, Sales_Order__c, Contract_Price__c, Type__c, Opportunity_Opend__c, Product__c, Subsidiary__c FROM Contract WHERE Subsidiary__c = 'Alma Lasers , Inc.'"
  data = varSF.query(query)
  records = data['records']

  df = pd.DataFrame(columns=['Id', 'AccountId', 'AccountName', 'StartDate', 'EndDate', 'BillingStreet', 'BillingCity', 'BillingState', 'BillingPostalCode', 'BillingCountry', 'BillingStateCode', 'BillingCountryCode', 'BillingLatitude', 'BillingLongitude', 'BillingGeocodeAccuracy', 'BillingAddress', 'ShippingStreet', 'ShippingCity', 'ShippingState', 'ShippingPostalCode', 'ShippingCountry', 'ShippingStateCode', 'ShippingCountryCode', 'ShippingLatitude', 'ShippingLongitude', 'ShippingGeocodeAccuracy', 'ShippingAddress', 'ContractTerm', 'OwnerId', 'OwnerName', 'Status', 'Asset__c', 'Serial_Number__c', 'BP__c', 'Product_Name__c', 'Sales_Order__c', 'Contract_Price__c', 'Type__c', 'Opportunity_Opend__c', 'Product__c', 'Subsidiary__c'])

  for record in records:
    row_data = {
        'Id': record['Id'],
        'AccountId': record['AccountId'],
        'AccountName': record['Account']['Name'],
        'StartDate': record['StartDate'],
        'EndDate': record['EndDate'],
        'BillingStreet': record['BillingStreet'],
        'BillingCity': record['BillingCity'],
        'BillingState': record['BillingState'],
        'BillingPostalCode': record['BillingPostalCode'],
        'BillingCountry': record['BillingCountry'],
        'BillingStateCode': record['BillingStateCode'],
        'BillingCountryCode': record['BillingCountryCode'],
        'BillingLatitude': record['BillingLatitude'],
        'BillingLongitude': record['BillingLongitude'],
        'BillingGeocodeAccuracy': record['BillingGeocodeAccuracy'],
        'BillingAddress': record['BillingAddress'],
        'ShippingStreet': record['ShippingStreet'],
        'ShippingCity': record['ShippingCity'],
        'ShippingState': record['ShippingState'],
        'ShippingPostalCode': record['ShippingPostalCode'],
        'ShippingCountry': record['ShippingCountry'],
        'ShippingStateCode': record['ShippingStateCode'],
        'ShippingCountryCode': record['ShippingCountryCode'],
        'ShippingLatitude': record['ShippingLatitude'],
        'ShippingLongitude': record['ShippingLongitude'],
        'ShippingGeocodeAccuracy': record['ShippingGeocodeAccuracy'],
        'ShippingAddress': record['ShippingAddress'],
        'ContractTerm': record['ContractTerm'],
        'OwnerId': record['OwnerId'],
        'OwnerName': record['Owner']['Name'],
        'Status': record['Status'],
        'Asset__c': record['Asset__c'],
        'Serial_Number__c': record['Serial_Number__c'],
        'BP__c': record['BP__c'],
        'Product_Name__c': record['Product_Name__c'],
        'Sales_Order__c': record['Sales_Order__c'],
        'Contract_Price__c': record['Contract_Price__c'],
        'Type__c': record['Type__c'],
        'Opportunity_Opend__c': record['Opportunity_Opend__c'],
        'Product__c': record['Product__c'],
        'Subsidiary__c': record['Subsidiary__c']
    }

    df = df.append(row_data, ignore_index=True)

  return df


def load_sf_data():
  sf = get_sf_connection()
  dfUser = get_sf_users_df()
  if "dfUser" not in st.session_state:
    st.session_state.dfUser = dfUser
  dfContracts = get_sf_contracts_df()
  if dfContracts not in st.session_state:
    st.session_state.dfContracts = dfContracts


def datasetselector():
  if st.session_state.selecteddataset == "Contracts":
    df = get_sf_contracts_df()
  elif st.session_state.selecteddataset == "Users":
    df = get_sf_users_df()
  else:
    df = get_sf_contracts_df()

  st.session_state.selecteddf = df
  return df


def displaycontainers(df):

    # Generate containers for each row
    for index, row in df.iterrows():
        with st.container():
            expander = st.expander(f"AccountId: {row['AccountId']}")
            with expander:
                st.write(row)

    # Add empty containers if there are less than 12 rows
    for _ in range(12 - len(df)):
        st.empty()

def chunk_dataframe(dataframe, chunk_size):
    for i in range(0, len(dataframe), chunk_size):
        yield dataframe.iloc[i:i + chunk_size]


def displaycontainers1(dataframe, chunksize):
   for chunk in chunk_dataframe(dataframe, 4):
        cols = st.columns(4)
        for i, row in enumerate(chunk.itertuples()):
            with cols[i]:
                expander = st.expander(f"AccountId: {row.AccountId}")
                with expander:
                    st.write(row)

        for i in range(len(chunk), 4):
            with cols[i]:
                st.empty()




def calculate_total_pages(dataframe, limit_per_page):
    return (len(dataframe) - 1) // limit_per_page + 1

def get_current_page_data(dataframe, page, limit_per_page):
    start = (page - 1) * limit_per_page
    end = start + limit_per_page
    return dataframe.iloc[start:end]

def displaycontainers2(df):
    total_pages = calculate_total_pages(df, 12)
    current_page = st.sidebar.number_input("Page", min_value=1, max_value=total_pages, value=1)

    current_data = get_current_page_data(df, current_page, 12)

    for chunk in chunk_dataframe(current_data, 4):
        cols = st.columns(4)
        for i, row in enumerate(chunk.itertuples()):
            with cols[i]:
                expander = st.expander(f"AccountId: {row.AccountId}")
                with expander:
                    st.write(row)

        for i in range(len(chunk), 4):
            with cols[i]:
                st.empty()