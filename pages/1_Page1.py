import streamlit as st
from config import pagesetup as ps
from simple_salesforce import Salesforce 
import pandas as pd

user = "Dominic Watson"
useremail = "dominic.watson@almalasers.com"
usersfid = "0055d00000Ccir0AAB"
sf = Salesforce(username=st.secrets.salesforce.sfuser, password=st.secrets.salesforce.sfcred, security_token=st.secrets.salesforce.sftoken)
sfqueryContracts = "SELECT Id, AccountId, Account.Name, StartDate, EndDate, BillingStreet, BillingCity, BillingState, BillingPostalCode, BillingCountry, BillingStateCode, BillingCountryCode, BillingLatitude, BillingLongitude, BillingGeocodeAccuracy, BillingAddress, ShippingStreet, ShippingCity, ShippingState, ShippingPostalCode, ShippingCountry, ShippingStateCode, ShippingCountryCode, ShippingLatitude, ShippingLongitude, ShippingGeocodeAccuracy, ShippingAddress, ContractTerm, OwnerId, Owner.Name, Status, Asset__c, Serial_Number__c, BP__c, Product_Name__c, Sales_Order__c, Contract_Price__c, Type__c, Opportunity_Opend__c, Product__c, Subsidiary__c FROM Contract WHERE Subsidiary__c = 'Alma Lasers , Inc.'"
sfqueryOpportunity = f"SELECT Id, Name, AccountId, Account.Name, OwnerId, Owner.Name, ContractId, CreatedDate, Created_From_Asset_or_Contract__c, CloseDate, Amount, Amount__c, Email__c, Install_Date__c, Type, Product__c, Pricebook2Id, RecordTypeId, Sales_Rep__c, StageName, Subsidiary__c, Territory2Id FROM Opportunity WHERE Subisdiary__c = 'Alma Lasers , Inc.' and OwnerId = '{usersfid}'"

ps.set_title("AlmyAI", "CX")
ps.set_blue_header("Expiring Contracts View")
ps.set_green_header("Dominic Watson (dominic.watson@almalasers.com)")
st.divider()


def get_sf_user_id(varSF, varEmail):
  query = f"SELECT Id FROM User WHERE Email = '{varEmail}'"
  data = varSF.query(query)
  records=data['records']
  numrecords = len(records)
  try:
    record = records[0]
    id = record['Id']
    return id
  except Exception as e:
    print(e)
    return None