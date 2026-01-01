import streamlit as st
import sqlite3
from database import create_db, add_user, login_user

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Tutor - Class 9", layout="centered")

# ---------------- DATABASE ----------------
create_db()

def save_current_chapter(username, subject, chapter):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            username TEXT,
            subject TEXT,
            chapter TEXT
        )
    """)
    c.execute(
        "INSERT INTO progress VALUES (?, ?, ?)",
        (username, subject, chapter)
    )
    conn.commit()
    conn.close()

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# ---------------- SUBJECT DATA ----------------
subjects = {
    "Physics": [
        "Motion",
        "Force and Laws of Motion",
        "Gravitation",
        "Work and Energy"
    ],
    "Chemistry": [
        "Matter in Our Surroundings",
        "Is Matter Around Us Pure",
        "Atoms and Molecules"
    ],
    "Biology": [
        "The Fundamental Unit of Life",
        "Tissues",
        "Diversity in Living Organisms"
    ],
    "Mathematics": [
        "Number Systems",
        "Polynomials",
        "Linear Equations in Two Variables"
    ]
}

# ---------------- UI ----------------
st.title("📘 AI Tutor – Class 9")

menu = st.sidebar.selectbox("Menu", ["Login", "Signup"])

# ---------------- SIGNUP ----------------
if menu == "Signup":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):
        try:
            add_user(new_user, new_pass)
            st.success("Account created successfully!")
        except:
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
            st.success("Login Successful")
        else:
            st.error("Invalid username or password")

# ---------------- DASHBOARD ----------------
if st.session_state.logged_in:
    st.success(f"Welcome {st.session_state.user} 👋")
    st.subheader("📚 Subject & Chapter Selection")

    subject = st.selectbox("Select Subject", list(subjects.keys()))
    chapter = st.selectbox("Select Chapter", subjects[subject])

    if st.button("Start Learning"):
        save_current_chapter(st.session_state.user, subject, chapter)
        st.success(f"Selected: {subject} → {chapter}")
        st.info("Next Step: Diagnostic Test")
