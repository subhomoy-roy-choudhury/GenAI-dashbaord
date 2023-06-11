import streamlit as st
from apps.pandas_profiler import pandas_profiler

def main_page():
    st.title("Main Page")
    st.write("Welcome to the main page!")
    
def main():
    state = st.session_state.get("state", {"page": "Main Page"})

    # Create a sidebar navigation
    pages = {
        "Pandas Profiler": pandas_profiler,
        "Main Page": main_page,
    }

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Go to", ["Main Page", "Pandas Profiler"])
    # selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    if selected_page != state["page"]:
        state["page"] = selected_page

    st.session_state["state"] = state
    pages[state["page"]]()
    
if __name__ == "__main__":
    main()