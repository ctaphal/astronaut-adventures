import streamlit as st
import random

st.set_page_config(page_title="Mad Libs!", page_icon="🤯")
st.title("Mad Libs! 🤯")
st.sidebar.header("Story time ~travel~ !")

# define prompts in a dictionary:
prompts = {
    "Astronaut Adventure!": "The brave astronaut decided to {} to the {} wearing a {} spacesuit. As they landed on the {}, they were greeted by a {} landscape filled with {} {}. The astronaut and their new {} friend {} explored this amazing world together, creating memories that would last a lifetime.",
    "Lost in Space!": "Oh no! I'm {} because I'm lost in space! I was on a mission to explore {} when my {} malfunctioned, and now I'm drifting through the endless {} darkness of space. I need to find my way back home, but all I have with me is a {}{}. I hope I encounter a friendly {} alien who can help me navigate this vast and {} universe. Until then, I'll just float and enjoy the view of the twinkling {}.",
    "Interstellar Picnic!": "We packed a picnic with {} and decided to {} under the {}. The {} sky stretched out above us, and we marveled at the {} stars twinkling like {}. The {} {}, our interstellar friend, shared stories of their {} on {}. It was such a {} day, and we counted {} shooting stars that night."
}
# add more prompts to dictionary later

def run() -> None:
    selected = st.sidebar.selectbox("Select a Mad Libs prompt: ", list(prompts.keys()))
    st.text(selected)

    if selected == "Astronaut Adventure!":

        verb = st.text_input("verb")
        noun = st.text_input("noun")
        color = st.text_input("color")
        celestial = st.text_input("celestial body (e.g., planet, moon)")
        adj = st.text_input("adjective")
        adj2 = st.text_input("another adjective")
        noun2 = st.text_input("another noun")
        adj3 = st.text_input("an adjective (again!)")
        alien = st.text_input("alien name")

        inputs = (verb, noun, color, celestial, adj, adj2, noun2, adj3, alien)

    if (selected == "Lost in Space!"):
        emotion = st.text_input("emotion")
        pOrG = st.text_input("planet or galaxy")
        n = st.text_input("noun")
        a3 = st.text_input("adjective")
        c1 = st.text_input("color")
        n2 = st.text_input("another noun")
        a4 = st.text_input("ANOTHER adjective")
        a5 = st.text_input("ANOTHER adjective (sorry! (not sorry))")
        n3 = st.text_input("plural noun")

        inputs = (emotion, pOrG, n, a3, c1, n2, a4, a5, n3)


    if selected == "Interstellar Picnic!":

        n_1 = st.text_input("noun")
        v = st.text_input("verb")
        n_2 = st.text_input("another noun")
        c = st.text_input("color")
        adj_1 = st.text_input("adjective")
        n_plural = st.text_input("plural noun")
        adj_2 = st.text_input("another adjective")
        job = st.text_input("a job title (ex: astronomer)")
        n_plural2 = st.text_input("another plural noun")
        cel = st.text_input("celestial body (e.g., planet, moon)")
        adj_3 = st.text_input("a third adjective")
        num = st.text_input("a number")

        inputs = (n_1, v, n_2, c, adj_1, n_plural, adj_2, job, n_plural2, cel, adj_3, num)

    if st.button("Generate Story"):
        if (selected == "Astronaut Adventure!"):
            if all(inputs):
                story = prompts[selected].format(verb, noun, color, celestial, adj, adj2, noun2, adj3, alien)
                st.markdown(story)
            else:
                st.warning("Please fill in all text boxes before generating your story!")

        if (selected == "Lost in Space!"):
            if all(inputs):
                story = prompts[selected].format(emotion, pOrG, n, a3, c1, n2, a4, a5, n3)
                st.markdown(story)
            else:
                st.warning("Please fill in all text boxes before generating your story!")

        if (selected == "Interstellar Picnic!"):
            if all(inputs):
                story = prompts[selected].format(n_1, v, n_2, c, adj_1, n_plural, adj_2, job, n_plural2, cel, adj_3, num)
                st.markdown(story)
            else:
                st.warning("Please fill in all text boxes before generating your story!")


run()