import streamlit as st


def page_summary_body():
    """
    Displays the contents of the project summary page in the Streamlit app.
    This includes an overview of the project, dataset details, business
    requirements, and additional resources like the README file.
    """
    st.write("### Project Overview")

    # Credits for summary text to https://github.com/linobollansee
    st.info(
        "📌 **Project Summary**\n\n"
        "After inheriting four houses in Ames, Iowa, our client enlisted our "
        "expertise to help secure the highest possible 💲 sale prices. "
        "To accomplish this, we designed a 🤖 Machine Learning model paired "
        "with 📈 regression algorithms to provide precise pricing insights and "
        "maximize the 🏠 property's market value."
    )
    # Displays Terms often used in the project
    st.info(
        f"📌 **Project Terms & Jargons**\n\n"
        f"* **Sales price** of a house refers to the current market price, in\
        US dollars, of a house with with various attributes.\n"
        f"* **Inherited house** is a house that the client inherited\
        from great-grandfather.\n"
    )

    # text based on README file - "Dataset Content" section
    st.info(
        f"📌 **Project Dataset**\n"
        f"* The dataset, which consists of 1460 rows, represents housing\
        records from Ames, Iowa. For homes constructed between 1872 and\
        2010, it shows the house profile (Floor Area, Basement, Garage,\
        Kitchen, Lot, Porch, Wood Deck, Year Built) and its corresponding\
        sale price.\n"
        f"* It is available in\
        [Kaggle via Code Institute](https://www.kaggle.com/codeinstitute/housing-prices-data)\n"
        f"* The dataset of inherited homes with the identical characteristics\
        as the primary data set,\
        aside from the SalePrice, which we must assist in forecasting,\
        is also provided."
    )
    # Display Business Requirements
    st.success(
        f"📌 **Project Business Requirements**\n\n"
        f"This project has 2 business requirements:\n"
        f"1. The client is interested in discovering how the house attributes\
        correlate with the sale price.\
        Therefore, the client expects data visualisations of the correlated\
        variables against the sale price to show that.\n"
        f"2. The client is interested in predicting the house sale price from\
        her four inherited houses and any other house in Ames, Iowa."
    )
    # Link to README file, so the users can have access to full\
    # project documentation
    st.info(
        f"📌 **Additional Information**\n"
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/CristianaDvD/Sales-House-Price-Estimate/blob/main/README.md).")
