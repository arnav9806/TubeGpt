import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("📝 Register for TubeGPT")

    # ---------------------------
    # Input Fields
    # ---------------------------
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # ---------------------------
    # Register Button
    # ---------------------------
    if st.button("Register"):
        if not email or not password or not confirm_password:
            st.error("Please fill all fields")
        elif password != confirm_password:
            st.error("Passwords do not match ❌")
        else:
            st.success("Registration successful ✅")

            # Store user info (temporary)
            st.session_state.user = email

            # Navigate to login page
            navigate("login")

    # ---------------------------
    # Login Redirect
    # ---------------------------
    st.write("Already have an account?")

    if st.button("Go to Login"):
        navigate("login")