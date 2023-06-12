import streamlit as st
from apps.pandas_profiler import pandas_profiler
from apps.gorilla_llm import gorilla_llm

def main_page():
    st.title("Main Page")
    st.write("Welcome to the main page!")
    
def main():
    state = st.session_state.get("state", {"page": "Gorilla LLM"})

    # Create a sidebar navigation
    pages = {
        "Pandas Profiler": pandas_profiler,
        "Gorilla LLM": gorilla_llm,
        "Main Page": main_page,
    }

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Go to", ["Gorilla LLM","Main Page", "Pandas Profiler"])
    # selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    if selected_page != state["page"]:
        state["page"] = selected_page

    st.session_state["state"] = state
    pages[state["page"]]()
    
if __name__ == "__main__":
    main()