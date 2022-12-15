import streamlit as st

st.set_page_config(
    page_title="jorisvdstraten.nl",
    # page_icon='dog'
)


def main():

    print(" Main load ")

    st.write(
        """
    # Work experience
    """
    )


def hide_footer():
    hide_footer_style = """
    <style>
    #MainMenu { visibility: hidden;}
    footer {visibility: hidden;}
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)


if __name__ == "__main__":
    hide_footer()
    main()
