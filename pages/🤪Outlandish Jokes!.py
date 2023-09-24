import streamlit as st
import random

st.set_page_config(page_title="Outlandish Jokes!", page_icon="🤪")

st.markdown("# Outlandish Jokes! 🤪")

which = bool(random.getrandbits(1))

if which == 0:
    #jokes in jokesDict from: https://www.rd.com/article/space-puns/
    jokesDict = {
        "How do you get clean in outer space?":"You take a meteor shower.",
        "What is money called in space?":"Star bucks.", 
        "What is an alien with three eyes called?": "An aliiien!", 
        "What did the Earth make fun of the moon for?": "Having no life.", 
        "What happened to the alien who stepped in gum?🫧": "She got stuck in Orbit.", 
        "What should you do if you see a green alien?": "Wait until it’s ripe!"
        }
    
    start, ans = random.choice(list(jokesDict.items()))
    st.markdown(start)
    st.markdown(ans)

else:
    memes = [
    "A.jpg",
    "B.jpg", 
    "C.jpg", 
    "D.jpg"
    ]

    st.image(random.choice(memes))


st.sidebar.header("Out of this world humor!")

st.markdown("\n")
    # Add a refresh button at the bottom of the page
if st.button("Another Joke!"):
    st.experimental_rerun()  # Rerun the app to refresh the page