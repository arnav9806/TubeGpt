import streamlit as st

def show(navigate):
    # ---------------------------
    # Page Title
    # ---------------------------
    st.title("🎥 Video Overview")

    # ---------------------------
    # Get Video Data (from processing)
    # ---------------------------
    video_data = st.session_state.get("video_data", {})

    title = video_data.get("title", "Sample Video Title")
    summary = video_data.get("summary", "This is a sample summary of the video.")

    # ---------------------------
    # Sidebar (Feature Navigation)
    # ---------------------------
    st.sidebar.title("📚 Features")

    if st.sidebar.button("🧠 Summary"):
        navigate("summary")

    if st.sidebar.button("💬 Chat"):
        navigate("chat")

    if st.sidebar.button("📝 Notes"):
        navigate("notes")

    if st.sidebar.button("🌍 Language"):
        navigate("language")

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        navigate("login")

    # ---------------------------
    # Main Content
    # ---------------------------
    st.subheader(f"📌 {title}")

    st.markdown("### 🧠 AI Summary")
    st.write(summary)

    st.markdown("---")

    st.markdown("### 📖 Key Sections")

    st.write("🔹 Introduction of the video topic")
    st.write("🔹 Important concepts explained")
    st.write("🔹 Final conclusion and takeaways")