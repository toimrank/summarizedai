import streamlit as st
import requests
import random

API_URL="http://127.0.0.1:8000/users"
API_URL_USER="http://127.0.0.1:8000/user"

st.title("User Management (API + Streamlit)")

def load_users():
    try:
        res = requests.get(API_URL)
        return res.json() if res.status_code == 200 else []
    except:
        return []

def update_user(user_id, data):
    res = requests.put(f"{API_URL_USER}/{user_id}", json=data)
    return res

def delete_user(user_id):
    res = requests.delete(f"{API_URL_USER}/{user_id}")
    return res

def create_user(data):
    data["id"] = random.randint(1000, 999999)
    res=requests.post(f"{API_URL_USER}", json=data)
    return res

users = load_users()
print(users)

if users:
    for index, u in enumerate(users):
        with st.expander(f"{u['name']} ({u['city']})"):
            st.write("**Name:**", u["name"])
            st.write("**Age:**", u["age"])
            st.write("**City:**", u["city"])
            st.write("**Password:**", u["password"])

            col1, col2 = st.columns(2)

            if col1.button("Edit", key=f"edit_btn_{u['id']}"):
                st.session_state["edit_user"] = u
                st.rerun()

            if col2.button("Delete", key=f"delete_btn_{u['id']}"):
                delete_user(u["id"])
                st.rerun()    

if "edit_user" in st.session_state:
    user = st.session_state["edit_user"]

    st.subheader(f"Edit Use: {user['name']}")

    name = st.text_input("Name", user['name'])
    age = st.number_input("Age", user['age'])
    city = st.text_input("city", user['city'])
    password = st.text_input("Password", user['password'])

    if st.button("Update User"):
        payload = {
            "name": name,
            "age": age,
            "city": city,
            "password": password
        }
        
        update_user(user["id"], payload)
        del st.session_state["edit_user"]
        st.success("User Updatd!")
        st.rerun()

st.subheader("Add New User")

with st.form("add_user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    city = st.text_input("City")
    password = st.text_input("Password")

    submitted = st.form_submit_button("Add User")

    if submitted:
        payload = {
            "name": name,
            "age": age,
            "city": city,
            "password": password
        }
        create_user(payload)
        st.success("User Created!")
        st.rerun()