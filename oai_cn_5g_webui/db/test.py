import streamlit as st

from db import DB
from models import AccessAndMobilitySubscriptionData, AuthenticationSubscription
# Assuming you have already defined your models (e.g., AccessAndMobilitySubscriptionData, Amf3GppAccessRegistration, etc.)

# Define your database URL
db_url = 'mysql+mysqlconnector://test:test@192.168.70.131/oai_db'

# Initialize the database connection
db = DB(db_url)

st.title("Authentication Subscription Management")

# Sidebar for navigation
menu = ["Insert", "Query", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# Insert
if choice == "Insert":
    st.subheader("Insert New Authentication Subscription")

    ueid = st.text_input("UEID")
    authenticationMethod = st.text_input("Authentication Method")
    encPermanentKey = st.text_input("Enc Permanent Key")
    protectionParameterId = st.text_input("Protection Parameter ID")
    sequenceNumber = st.text_input("Sequence Number")
    authenticationManagementField = st.text_input("Authentication Management Field")
    algorithmId = st.text_input("Algorithm ID")
    encOpcKey = st.text_input("Enc OPC Key")
    encTopcKey = st.text_input("Enc TOPC Key")
    vectorGenerationInHss = st.checkbox("Vector Generation in HSS")
    n5gcAuthMethod = st.text_input("N5GC Auth Method")
    rgAuthenticationInd = st.checkbox("RG Authentication Ind")
    supi = st.text_input("SUPI")

    if st.button("Insert"):
        new_auth_subscription = AuthenticationSubscription(
            ueid=ueid,
            authenticationMethod=authenticationMethod,
            encPermanentKey=encPermanentKey,
            protectionParameterId=protectionParameterId,
            sequenceNumber=sequenceNumber,
            authenticationManagementField=authenticationManagementField,
            algorithmId=algorithmId,
            encOpcKey=encOpcKey,
            encTopcKey=encTopcKey,
            vectorGenerationInHss=vectorGenerationInHss,
            n5gcAuthMethod=n5gcAuthMethod,
            rgAuthenticationInd=rgAuthenticationInd,
            supi=supi
        )
        db.insert(new_auth_subscription)
        st.success(f"Inserted {ueid}")

# Query
elif choice == "Query":
    st.subheader("Query Authentication Subscription")

    ueid = st.text_input("UEID")

    if st.button("Query"):
        result = db.query(AuthenticationSubscription, ueid=ueid)
        if result:
            for item in result:
                st.write(item.__dict__)
        else:
            st.warning(f"No record found for UEID: {ueid}")

# Update
elif choice == "Update":
    st.subheader("Update Authentication Subscription")

    ueid = st.text_input("UEID to Update")
    authenticationMethod = st.text_input("New Authentication Method")
    encPermanentKey = st.text_input("New Enc Permanent Key")
    protectionParameterId = st.text_input("New Protection Parameter ID")
    sequenceNumber = st.text_input("New Sequence Number")
    authenticationManagementField = st.text_input("New Authentication Management Field")
    algorithmId = st.text_input("New Algorithm ID")
    encOpcKey = st.text_input("New Enc OPC Key")
    encTopcKey = st.text_input("New Enc TOPC Key")
    vectorGenerationInHss = st.checkbox("New Vector Generation in HSS")
    n5gcAuthMethod = st.text_input("New N5GC Auth Method")
    rgAuthenticationInd = st.checkbox("New RG Authentication Ind")
    supi = st.text_input("New SUPI")

    if st.button("Update"):
        data = {
            'authenticationMethod': authenticationMethod,
            'encPermanentKey': encPermanentKey,
            'protectionParameterId': protectionParameterId,
            'sequenceNumber': sequenceNumber,
            'authenticationManagementField': authenticationManagementField,
            'algorithmId': algorithmId,
            'encOpcKey': encOpcKey,
            'encTopcKey': encTopcKey,
            'vectorGenerationInHss': vectorGenerationInHss,
            'n5gcAuthMethod': n5gcAuthMethod,
            'rgAuthenticationInd': rgAuthenticationInd,
            'supi': supi
        }
        data = {k: v for k, v in data.items() if v}  # Remove None or empty values
        db.update(AuthenticationSubscription, {'ueid': ueid}, data)
        st.success(f"Updated {ueid}")

# Delete
elif choice == "Delete":
    st.subheader("Delete Authentication Subscription")

    ueid = st.text_input("UEID to Delete")

    if st.button("Delete"):
        db.delete(AuthenticationSubscription, ueid=ueid)
        st.success(f"Deleted {ueid}")