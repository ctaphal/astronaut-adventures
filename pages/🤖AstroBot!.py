import streamlit as st

st.set_page_config(page_title="🤖 AstroBot!")
st.title("🤖 AstroBot!")
st.sidebar.header("TaKe mE tO YoUR tEaCHeR")

# Define functions
def inputsolar():
    st.write("Great choice! Did you know that the Solar System was born 4.6 million years ago? We are nowhere near the center of the galaxy either! 😄")

def inputstars():
    st.write("The next fact that I'm about to tell you will blow you mind! There are about 200 billion stars in our world! Did I just blow your mind or what?")

def inputconstellations():
    st.write("Cool! Do you know how many constellations there are?")
    user_guess = st.number_input("Guess the number of constellations:")
    correct_answer = 88  # The actual number of constellations
    if user_guess == correct_answer:
        st.write("That's correct! There are indeed 88 constellations.")
    else:
        st.write(f"Sorry, that's not correct. The correct answer is 88 constellations.")
        
def inputquestone():
    st.write("Nice choice! The Milky Way is a barred spiral galaxy, about 100,000 light-years across. 💫")

def inputquesttwo():
    st.write("Our universe is about 13.8 billion years old, so most galaxies formed when the universe was quite young! Astronomers believe that our own Milky Way galaxy is approximately 13.6 billion years old. The newest galaxy we know of formed only about 500 million years ago.")

def options():
    st.write("")

def main():
    st.write("Hi! My name is AstroBot!")

    # Getting user's name
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hey {name}, it's nice to meet you!")

        gbord = st.selectbox(f"How are you doing today?", ("Good", "Okay", "Bad"))

        # Feelings
        if gbord == "Good":
            st.write(f"That's wonderful, {name}! 😁")
        elif gbord == "Okay":
            st.write(f"That's good to hear, {name}! 😊")
        elif gbord == "Bad":
            st.write(f"Oh, I'm sorry, {name}! I hope learning about space will cheer you up! ☺️")

        # Get ready to learn!
        a = st.radio("Are you ready to learn?", ("Yes", "No"))

        #If yes 
        if a == "Yes":
            st.write(" Let's get ready to blast into the world of knowledge! ☄️ ")
            options()
            b = st.radio("Which do you want to learn about:", ("Solar System", "Stars", "Constellations", "What type of galaxy the Milky Way is", "Age of Milky Way?", "Done"))
            if b == "Solar System":
                inputsolar()
            elif b == "Stars":
                inputstars()
            elif b == "Constellations":
                inputconstellations()
            elif b == "What type of galaxy the Milky Way is":
                inputquestone()
            elif b == "Age of Milky Way?":
                inputquesttwo()
            elif b == "Done":
                st.write("Bye! It's been a blast!")


        # If no
        if a == "No":
            st.write("Oh, okay...bye 🥲")
            st.write("Just Kidding!")
            options()
            b = st.radio("Which do you want to learn about:", ("Solar System", "Stars", "Constellations", "What type of galaxy the Milky Way is", "Age of Milky Way?", "Done"))
            if b == "Solar System":
                inputsolar()
            elif b == "Stars":
                inputstars()
            elif b == "Constellations":
                inputconstellations()
            elif b == "What type of galaxy the Milky Way is":
                inputquestone()
            elif b == "Age of Milky Way?":
                inputquesttwo()
            elif b == "Done":
                st.write("Bye! It's been a blast!")

if __name__ == "__main__":
    main()
