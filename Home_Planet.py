import streamlit as st
from streamlit.logger import get_logger
import random


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Cool Space",
        page_icon="🚀",
    )

    st.write("# :rainbow[Astronaut Adventures!] 🚀")

    st.markdown(
        ''':violet[Cool space things!]'''
    )
    
    st.image("HomePic.jpg")

    st.markdown(
        '''Check out "stellar" space music, jokes, pics, and Mad Libs using the menu on the top left!'''
    )
    

if __name__ == "__main__":
    run()
