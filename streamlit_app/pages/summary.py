import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("🧠 AI Summary")

    # ---------------------------
    # Get Video Data
    # ---------------------------
    video_data = st.session_state.get("video_data", {})

    summary = video_data.get(
        "summary",
        "This is a sample summary of the video."
    )

    # ---------------------------
    # Tabs for Different Summaries
    # ---------------------------
    tab1, tab2, tab3 = st.tabs([
        "Quick Summary",
        "Detailed Summary",
        "Key Points"
    ])

    # ---------------------------
    # Quick Summary
    # ---------------------------
    with tab1:
        st.subheader("⚡ Quick Summary")
        st.write(summary)

    # ---------------------------
    # Detailed Summary
    # ---------------------------
    with tab2:
        st.subheader("📖 Detailed Summary")
        st.write("This is a more detailed explanation of the video content...")
        st.write(summary)

    # ---------------------------
    # Key Points
    # ---------------------------
    with tab3:
        st.subheader("📌 Key Takeaways")
        st.write("🔹 Point 1 from the video")
        st.write("🔹 Point 2 from the video")
        st.write("🔹 Point 3 from the video")

    st.markdown("---")

    # ---------------------------
    # Back Button
    # ---------------------------
    if st.button("⬅ Back to Overview"):
        navigate("overview")