import streamlit as st
from database import create_db, add_user, login_user

st.set_page_config(page_title="AI Tutor - Class 9", layout="centered")

# create database
create_db()

# session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

st.title("📘 AI Tutor – Class 9")

# SIDEBAR MENU (FIXED)
menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- LOGIN ----------------
if choice == "Login":
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(username, password)
        if result:
            st.success(f"Welcome {username} 👋")
            st.session_state.logged_in = True
            st.session_state.user = username
        else:
            st.error("Invalid username or password")

# ---------------- SIGN UP ----------------
elif choice == "Sign Up":
    st.subheader("📝 Create Account")

    new_user = st.text_input("Choose Username")
    new_pass = st.text_input("Choose Password", type="password")

    if st.button("Sign Up"):
        if new_user == "" or new_pass == "":
            st.warning("Please fill all fields")
        else:
            try:
                add_user(new_user, new_pass)
                st.success("Account created successfully!")
                st.info("Now go to Login")
            except:
                st.error("Username already exists")

# ---------------- AFTER LOGIN ----------------
if st.session_state.logged_in:
    st.success("✅ Login Successful")
    st.write("Next step: Subject & Chapter selection")
