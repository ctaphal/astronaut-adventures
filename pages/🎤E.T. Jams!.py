import streamlit as st
from streamlit_player import st_player
import random

def run():
    st.set_page_config(page_title="E.T. Jams!", page_icon="🎸")
    st.markdown("# E.T. Jams!🎤🤘")
    st.sidebar.header("""Nep-"tunes"!""")
    st.write(
        """Music from outer space!"""
    )

    music_list = ["https://soundcloud.com/loveblonde1/dua-lipa-levitating-fixed-version?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
                  "https://soundcloud.com/wxliumusic-3098824/starlight-taylor-swift-house-remix?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/mlicasiano09/talking-to-the-moon-bruno-mars?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/user-956334953/pitch-shifted-coldplay-a-sky-full-of-stars-official-video-2?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/interscope/onerepublic-counting-stars?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/timothyns/ariana-grande-nasa-lo-fi-remix?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/rodesnanda/frank-sinatra-fly-me-to-the?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/886beatz/little-einsteins-mix?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", 
                  "https://soundcloud.com/flopline/daylight-acoustic-piano?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
                  ]
    st_player(random.choice(music_list))

    st.markdown("\n")

     # Add a refresh button at the bottom of the page
    if st.button("Another song!"):
        st.experimental_rerun()  # Rerun the app to refresh the page

run()