# salesforce_connection.py

import pandas as pd
from simple_salesforce import Salesforce
import streamlit as st

@st.cache_data
def fetch_salesforce_data():
    # Connect to Salesforce
    sf = Salesforce(username=st.secrets.salesforce.sfuser,
                    password=st.secrets.salesforce.sfcred,
                    security_token=st.secrets.salesforce.sftoken)

    # Salesforce Query
    sfqueryOpportunity = """
    SELECT Id, Name, AccountId, Account.Name, OwnerId, Owner.Name, ContractId, CreatedDate, 
    Created_From_Asset_or_Contract__c, CloseDate, Amount, Amount__c, Email__c, Install_Date__c, Type, Product__c, 
    Pricebook2Id, RecordTypeId, RecordType.Name, Sales_Rep__c, StageName, Subsidiary__c, Territory2Id 
    FROM Opportunity 
    WHERE Subsidiary__c = 'Alma Lasers , Inc.' and OwnerId = '0055d00000Ccir0AAB' and Id = '0065d0000174hAxAAI'
    """

    data = sf.query(sfqueryOpportunity)
    records = data['records']

    # Creating DataFrame
    df = pd.DataFrame(columns=[
        'Id', 'Name', 'AccountId', 'AccountName', 'OwnerId', 'OwnerName', 'ContractId', 
        'CreatedDate', 'Created_From_Asset_or_Contract__c', 'CloseDate', 'Amount', 'Amount__c', 
        'Email__c', 'Install_Date__c', 'Type', 'Product__c', 'Pricebook2Id', 'RecordTypeId', 
        'RecordTypeName', 'Sales_Rep__c', 'StageName', 'Subsidiary__c', 'Territory2Id'
    ])

    for record in records:
        # ... Record processing logic ...
        df = df.append(record, ignore_index=True)

    return df
