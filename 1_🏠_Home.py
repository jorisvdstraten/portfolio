import streamlit as st

st.set_page_config(
    page_title="jorisvdstraten.nl",
    # page_icon='dog'
)


def main():

    print(" Main load ")

    st.write(
        """
    # Joris van der Straten
    Hi, I'm Joris, lecturer at Fontys University of Applied Sciences in the Netherlands. I'm a data enthusiast with a passion for visualization and machine learning.     
    """
    )

    st.write(
        """If you have any questions / thoughts, feel free to reach out to me at work via [e-mail](mailto:j.vanderstraten@fontys.nl) or [LinkedIn](https://linkedin.com/in/jorisvdstraten)."""
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
