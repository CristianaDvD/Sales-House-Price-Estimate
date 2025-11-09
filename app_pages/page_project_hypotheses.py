import streamlit as st


def page_project_hypotheses_body():
    '''
    Displays the hypotheses and their validation results
    '''
    st.write("### Project Hypotheses and Validation")

    # Display first hypothesis
    st.success(
        f"💭 **Hypothesis 1:**\n"
        f"- Houses with higher overall material and finish quality\
        sell for higher prices.\n"
        f"\n**Rationale:**\n"
        f"- Durability and appeal are increased by superior construction.\n"
        f"\n**Validation:**\n"
        f"\n✅ The overall quality rating of a house and its sale price \
        are strongly correlated, according to our statistics,\
        which approves our first assumption."
    )

    # Display second hypothesis
    st.success(
        f"💭 **Hypothesis 2:**\n"
        f"- Houses with larger above-ground living area have higher\
        sale prices.\n"
        f"\n**Rationale:**\n"
        f"- Because they have greater living space, larger homes\
        are typically more valuable.\n"
        f"\n**Validation:**\n"
        f"\n✅ We found a positive and moderate correlation between \
        parameters related to property size and sale price after doing a\
        comprehensive correlation analysis. This supports our original\
        hypothesis by indicating that larger houses typically\
        sell for higher prices."
    )

    # Display 3rd hypothesis
    st.success(
        f"💭 **Hypothesis 3:**\n"
        f"- Houses with extra spaces get to a higher sale price.\n"
        f"\n**Rationale:**\n"
        f"- Houses with additional features such as garages, or finished\
        basements are more expensive.\n"
        f"\n**Validation:**\n"
        f"\n✅ Our analysis confirmed our assumption by revealing a good\
        positive correlation of all that indicates additional features and\
        spaces, like garage area or basement area. These features improve\
        comfort and perceived luxury."
    )

    # Display our 4th but not fully confirmed hypothesis
    st.success(
        f"💭 **Hypothesis 4:**\n"
        f"- Houses with a good kitchen quality have a good impact on the\
        sale price.\n"
        f"\n**Rationale:**\n"
        f"- A good quality kitchen attracts buyers, as that is the place\
        where majority spend a large amount of time.\n"
        f"\n**Validation:**\n"
        f"\n❔❔ We can maintain our premise that a high-quality kitchen \
        enhances the overall quality of a property even if the variable does\
        not correspond to our top factors. Additionally, this variable had a\
        favorable link with our target, according to our correlation\
        investigation."
    )
