import streamlit as st
from database import create_db, add_user, login_user, save_current_chapter

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Tutor - Class 9", layout="centered")

# ---------------- CREATE DB ----------------
create_db()

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- TITLE ----------------
st.title("📘 AI Tutor – Class 9")

menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

# ---------------- SIGNUP ----------------
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
                st.success("Signup successful! Please go to Login")
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
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success(f"Welcome {user} 👋")
        else:
            st.error("Invalid username or password")

# ---------------- DASHBOARD ----------------
if st.session_state.logged_in:
    st.success(f"Logged in as {st.session_state.user}")

    # Subject & Chapter Selection
    st.subheader("📘 Select Subject & Chapter")
    subjects = {
        "Physics": ["Motion", "Force and Laws of Motion", "Gravitation", "Work and Energy"],
        "Chemistry": ["Matter in Our Surroundings", "Is Matter Around Us Pure?"],
        "Biology": ["The Fundamental Unit of Life", "Tissues"],
        "Mathematics": ["Number Systems", "Polynomials", "Linear Equations in Two Variables"]
    }

    subject = st.selectbox("Select Subject", list(subjects.keys()))
    chapter = st.selectbox("Select Chapter", subjects[subject])

    if st.button("Start Learning"):
        save_current_chapter(st.session_state.user, subject, chapter)
        st.success(f"Saved: {subject} → {chapter}")
