import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("🌍 Language Translation")

    # ---------------------------
    # Get Video Data
    # ---------------------------
    video_data = st.session_state.get("video_data", {})

    summary = video_data.get(
        "summary",
        "This is a sample summary of the video."
    )

    # ---------------------------
    # Language Selection
    # ---------------------------
    language = st.selectbox(
        "Select Language",
        ["English", "Hindi", "Spanish", "French"]
    )

    # ---------------------------
    # Translate Button
    # ---------------------------
    if st.button("Translate"):
        st.subheader(f"Translated to {language}")

        # Dummy translation (for now)
        if language == "Hindi":
            st.write("यह वीडियो का अनुवादित सारांश है।")

        elif language == "Spanish":
            st.write("Este es un resumen traducido del video.")

        elif language == "French":
            st.write("Ceci est un résumé traduit de la vidéo.")

        else:
            st.write(summary)

    st.markdown("---")

    # ---------------------------
    # Back Button
    # ---------------------------
    if st.button("⬅ Back to Overview"):
        navigate("overview")