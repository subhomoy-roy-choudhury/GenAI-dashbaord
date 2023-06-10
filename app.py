import streamlit as st

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def main_page():
    st.title("Main Page")
    st.write("Welcome to the main page!")

def about_page():
    st.title("About Page")
    st.write("This is the about page.")

def contact_page():
    st.title("Contact Page")
    st.write("You can contact us here.")
    
def main():
    state = st.session_state.get("state", {"page": "Main Page"})

    # Create a sidebar navigation
    pages = {
        "Main Page": main_page,
        "About": about_page,
        "Contact": contact_page
    }

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Go to", ["Main Page", "About", "Contact"])
    # selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    if selected_page != state["page"]:
        state["page"] = selected_page

    st.session_state["state"] = state
    pages[state["page"]]()
    
if __name__ == "__main__":
    main()