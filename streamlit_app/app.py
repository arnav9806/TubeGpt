import streamlit as st

# ---------------------------
# Page Config (Optional)
# ---------------------------
st.set_page_config(
    page_title="TubeGPT",
    layout="wide"
)

# ---------------------------
# Initialize Session State
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"
    
# ---------------------------
# Sidebar Visibility Control  ✅ ADD HERE
# ---------------------------
hide_sidebar_pages = ["login", "register", "landing", "processing"]

if st.session_state.page in hide_sidebar_pages:
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Navigation Function
# ---------------------------
def navigate(page_name):
    st.session_state.page = page_name


# ---------------------------
# ROUTER (Main Logic)
# ---------------------------
page = st.session_state.page

if page == "login":
    from pages.login import show
    show(navigate)

elif page == "register":
    from pages.register import show
    show(navigate)

elif page == "landing":
    from pages.landing import show
    show(navigate)

elif page == "processing":
    from pages.processing import show
    show(navigate)

elif page == "overview":
    from pages.overview import show
    show(navigate)

elif page == "summary":
    from pages.summary import show
    show(navigate)

elif page == "chat":
    from pages.chat import show
    show(navigate)

elif page == "notes":
    from pages.notes import show
    show(navigate)

elif page == "language":
    from pages.language import show
    show(navigate)

else:
    st.error("Page not found")