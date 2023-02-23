from random import choice


#  define a function that returns a random word from the words.txt file
#  and make sure it's lower case
def generate_word():
    with open("words.txt", "r") as f:
        words = f.readlines()
    return choice(words).lower().strip()
