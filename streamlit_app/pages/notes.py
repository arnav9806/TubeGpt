import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("📝 Generate Notes")

    # ---------------------------
    # Notes Type Selection
    # ---------------------------
    option = st.selectbox(
        "Choose Notes Type",
        ["Study Notes", "Revision Notes", "Quiz", "Flashcards"]
    )

    # ---------------------------
    # Generate Button
    # ---------------------------
    if st.button("Generate"):
        if option == "Study Notes":
            st.subheader("📚 Study Notes")
            st.write("Detailed notes about the video will appear here...")

        elif option == "Revision Notes":
            st.subheader("📌 Revision Notes")
            st.write("Short and quick revision notes will appear here...")

        elif option == "Quiz":
            st.subheader("❓ Quiz")
            st.write("Q1. Sample question?")
            st.write("Q2. Sample question?")

        elif option == "Flashcards":
            st.subheader("🧠 Flashcards")
            st.write("Q: Sample question?")
            st.write("A: Sample answer")

    st.markdown("---")

    # ---------------------------
    # Back Button
    # ---------------------------
    if st.button("⬅ Back to Overview"):
        navigate("overview")