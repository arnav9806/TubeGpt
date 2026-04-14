import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("💬 Chat with Video")

    # ---------------------------
    # Initialize Chat History
    # ---------------------------
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ---------------------------
    # Display Chat Messages
    # ---------------------------
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # ---------------------------
    # User Input
    # ---------------------------
    user_input = st.chat_input("Ask something about the video...")

    if user_input:
        # Add user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        # Display user message
        with st.chat_message("user"):
            st.write(user_input)

        # Dummy AI response (for now)
        response = f"Answer for: {user_input} (timestamp: 1:23)"

        # Add AI response
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

        # Display AI response
        with st.chat_message("assistant"):
            st.write(response)

    # ---------------------------
    # Back Button
    # ---------------------------
    if st.button("⬅ Back to Overview"):
        navigate("overview")