import streamlit as st
from st_supabase_connection import SupabaseConnection

@st.cache_resource
def get_con_supabase():
    client_supabase = st.experimental_connection(
        name="supabase",
        type=SupabaseConnection
    )
    return client_supabase

#conn_supabase = get_con_supabase()

def get_data_users():
    conUsers = get_con_supabase()
    tblUsers = "users"
    qryUsers = "*"
    ttlUsers = None
    rowUsers = conUsers.query(qryUsers, table=tblUsers, ttl=ttlUsers).execute()
    dataUsers = rowUsers.data
    return dataUsers

def get_data_audit():
    conAudit = get_con_supabase()
    tblAudit = "auditlog"
    qryAudit = "*"
    ttlAudit = None
    rowAudit = conAudit.query(qryAudit, table=tblAudit, ttl=ttlAudit).execute()
    dataAudit = rowAudit.data
    return dataAudit

def get_data_sensors():
    conSensors = get_con_supabase()
    tblSensors = "sensors"
    qrySensors = "*"
    ttlSensors = None
    rowSensors = conSensors.query(qrySensors, table=tblSensors, ttl=ttlSensors).execute()
    dataSensors = rowSensors.data
    return dataSensors

def get_data_certs():
    conCerts = get_con_supabase()
    tblCerts = "certificates"
    qryCerts = "*"
    ttlCerts = None
    rowCerts = conCerts.query(qryCerts, table=tblCerts, ttl=ttlCerts).execute()
    dataCerts = rowCerts.data
    return dataCerts

def get_data_notifications():
    conNotifications = get_con_supabase()
    tblNotifications = "notifications"
    qryNotifications = "*"
    ttlNotifications = None
    rowNotifications = conNotifications.query(qryNotifications, table=tblNotifications, ttl=ttlNotifications).execute()
    dataNotifications = rowNotifications.data
    return dataNotifications


#https://st-supabase-connection.streamlit.app/
