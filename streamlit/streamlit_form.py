import streamlit as st
import time

st.title("User Registration")

with st.form("registration_form"):
    st.header("Personal Information")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    radio_button = st.radio("Gender", ["Male", "Female", "Other"])

    age = st.number_input("Age", min_value=1, max_value=120, step=1)

    dob = st.date_input('Date Of Birth')

    st.header("Contact Information")
    email = st.text_input("Email")
    phone = st.text_input("Phone") 

    st.header("Address")
    country = st.selectbox("Country", ["USA", "Indua", "UK", "Australia", "Other"])
    city=st.text_input("City")
    zip_code=st.text_input("Zipcode")

    st.header("Account Preferences")
    username=st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    newsletter = st.checkbox("Subscribe to newsletter")

    st.markdown('<h2 style="color:blue;">Other Details</h2>', unsafe_allow_html=True)   
    hobbies = st.multiselect("Hobbies", ["Reading", "Sports", "Gaming", "Music"])   


    submitted = st.form_submit_button("Register")

    if submitted:
        print("Submitted >>>>")

        with st.spinner("Submitting Details...."):
            time.sleep(3)

        if not first_name or not last_name:
            st.error("Firat name and Last name is required")
        else:
            st.success("Sumbmitted...")
            st.info("Sumbmitted...")
            st.warning("Sumbmitted...")
            st.json(
                {
                    "First Name" : first_name,
                    "Last Name" : last_name
                }
            )
