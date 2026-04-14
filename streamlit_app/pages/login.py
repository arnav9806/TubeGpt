import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("🔐 Login to TubeGPT")

    # ---------------------------
    # Input Fields
    # ---------------------------
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # ---------------------------
    # Login Button
    # ---------------------------
    if st.button("Login"):
        # For now (no backend), just validate basic input
        if email and password:
            st.success("Login successful ✅")

            # Store user info in session
            st.session_state.user = email

            # Navigate to landing page
            navigate("landing")
        else:
            st.error("Please enter email and password")

    # ---------------------------
    # Register Redirect
    # ---------------------------
    st.write("Don't have an account?")

    if st.button("Go to Register"):
        navigate("register")