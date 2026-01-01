import streamlit as st
from database import create_db, add_user, login_user

st.set_page_config(page_title="AI Tutor - Class 9", layout="centered")

create_db()

if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = None

st.title("📘 AI Tutor - Class 9")

menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

# ---------------- SIGN UP ----------------
if menu == "Sign Up":
    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if new_user == "" or new_pass == "":
            st.warning("Please fill all fields")
        else:
            success = add_user(new_user, new_pass)
            if success:
                st.success("Signup successful! Now login.")
            else:
                st.error("Username already exists")

# ---------------- LOGIN ----------------
if menu == "Login":
    st.subheader("Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(user, pwd)
        if result:
            st.session_state.login = True
            st.session_state.user = user
            st.success(f"Welcome {user} 👋")
        else:
            st.error("Invalid username or password")

# ---------------- AFTER LOGIN ----------------
if st.session_state.login:
    st.success(f"Logged in as {st.session_state.user}")
