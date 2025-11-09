import streamlit as st


class MultiPage:
    """
    A class to create a multi-page Streamlit app.
    This class allows you to define multiple pages within the app
    and switch between them using a sidebar navigation menu.
    """
    def __init__(self, app_name):
        """
        Initializes the MultiPage app with the given name.
        """
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,  # Set the title of the page
            page_icon="🌇"  # Set the page icon
        )

    def add_page(self, title, func):
        """
        Adds a new page to the app.
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Runs the app by displaying the main title and setting up a sidebar menu
        for navigation.
        The selected page will be rendered based on the sidebar choice.
        """
        st.title(self.app_name)

        page = st.sidebar.radio(
            "Menu",  # Label for the sidebar menu
            self.pages,  # List of pages to display
            format_func=lambda page: page["title"]
        )

        page["function"]()
