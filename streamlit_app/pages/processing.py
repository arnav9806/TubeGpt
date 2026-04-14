import streamlit as st
import time

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("⏳ Processing Video")

    st.write("Please wait while we process your video...")

    st.markdown("---")

    # ---------------------------
    # Processing Steps UI
    # ---------------------------
    progress_text = st.empty()

    with st.spinner("Processing..."):
        steps = [
            "📥 Fetching transcript...",
            "🧠 Generating embeddings...",
            "✍️ Creating summary..."
        ]

        for step in steps:
            progress_text.write(step)
            time.sleep(1.5)  # simulate delay

    # ---------------------------
    # Store Dummy Data (for now)
    # ---------------------------
    st.session_state.video_data = {
        "title": "Sample Video Title",
        "summary": "This is a dummy summary of the video.",
    }

    st.success("Processing complete ✅")

    time.sleep(1)

    # ---------------------------
    # Navigate to Overview Page
    # ---------------------------
    navigate("overview")