import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("🎥 TubeGPT")

    # ---------------------------
    # Intro Text
    # ---------------------------
    st.write("Learn faster from YouTube using AI")
    st.write("Transform videos into structured knowledge in seconds 🚀")

    st.markdown("---")

    # ---------------------------
    # YouTube URL Input
    # ---------------------------
    youtube_url = st.text_input("Paste YouTube URL here")

    # ---------------------------
    # Submit Button
    # ---------------------------
    if st.button("Submit"):
        if youtube_url:
            # Store URL in session
            st.session_state.video_url = youtube_url

            # Navigate to processing page
            navigate("processing")
        else:
            st.error("Please enter a YouTube URL")

    st.markdown("---")

    # ---------------------------
    # Product Description
    # ---------------------------
    st.subheader("What you can do:")

    st.write("✅ Get AI-generated summaries")
    st.write("💬 Ask questions about the video")
    st.write("📝 Generate notes and quizzes")
    st.write("🌍 Translate content into different languages")