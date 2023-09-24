import streamlit as st
import random

st.set_page_config(page_title="Space Pics!", page_icon="📷")

def run() -> None:

    imDesDict = {
    "1.jpg":"These astronomers went on an exciting 7-hour adventure to capture pictures of special places against a background of colorful lights, called auroras. Auroras are natural displays of dazzling lights that usually happen in the far north and south parts of Earth's Hemispheres. You can tell that this is the Northern Hemisphere because at the very top of the picture, there is a special star called Polaris, which is also known as the North Star. 🌟 It's like the captain of all the stars because it always shows us which way is north, even when we're in the dark!",
    "2.jpg":"This photo is not just a normal nebula photo, it was taken just 2 minutes after a rocket launch! The rocket, called Falcon 9 was on a mission called SpaceX Crew-7, taking four people to the International Space Station. In the picture, you can see two bright dots. The lower one is the part of the rocket that carries the astronauts into space. The dot above it is the first part of the rocket, and it's getting ready to come back to Earth. So, it is like a space adventure picture, showing the rocket going up and coming back down on our planet!", 
    "3.jpg": "Do stars always create jets when they form? As a baby star is born they can sometimes spin too fast, which can stop them from growing into full-grown stars. Sometimes these baby stars will shoot out something called jets. These jets help the baby stars slow down their spinning.", 
    "4.jpg": "This is what a solar eclipse looks like! A solar eclipse is when the moon gets in front of the sun and covers most of it! The bright part of the sun that we can still see is called a ring of fire! This awesome picture was not totally planned because the person in it walked in unexpectedly!", 
    "5.jpg": "🪐Spots and moons of Jupiter: The big oval spot near the center is Jupiter’s Great Red Spot– a storm that’s possibly lasted for over 355 years! The small ball near the bottom left is one of Jupiter’s largest moons, Europa - tiny in comparison to Jupiter! Some also say that there might be an underground ocean on Europa. Conclusion: Europa might have alien mermaids! 👽🧜‍♀️", 
    "6.jpg": "“🦅Birds don't fly this high. ✈️Airplanes don't go this fast. 🗽The Statue of Liberty weighs less.” This is the launch of the Chandrayaan-3 mission! This was India’s first moon landing and the first ever landing on the south pole of the moon!"
    }

    st.sidebar.header("“Stellar” space pics!")

    img, desc = random.choice(list(imDesDict.items()))

    st.image(img)   

    st.markdown(desc)
    
    st.markdown("\n")
    # Add a refresh button at the bottom of the page
    if st.button("Another Pic!"):
        st.experimental_rerun()  # Rerun the app to refresh the page

    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    
    st.markdown("Images and description inspiration from: https://apod.nasa.gov/apod/archivepix.html")


st.markdown("# Space Pics! 📷")

run()
