from simple_salesforce import Salesforce
import streamlit as st
import pandas as pd

sf = Salesforce(username=st.secrets.salesforce.sfuser, password=st.secrets.salesforce.sfcred, security_token=st.secrets.salesforce.sftoken)

query = "SELECT Id, Username, LastName, FirstName, Name, Email FROM User WHERE Subsidiary__c = 'Alma Lasers , Inc.'"

data = sf.query(query)
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

df.to_csv("users.csv")

