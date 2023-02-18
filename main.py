from random import choice


class CurrentGenValue(object):

    def __init__(self, generator):
        self.__gen = generator()

    def __iter__(self):
        return self

    def __next__(self):
        self.current = next(self.__gen)
        return self.current

    def __call__(self):
        return self


@CurrentGenValue
def hangman_states():
    states = [
        "  ______\n"
        "  |    |\n"
        "       |\n"
        "       |\n"
        "       |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        "       |\n"
        "       |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        "  |    |\n"
        "       |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        " /|    |\n"
        "       |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        " /|\   |\n"
        "       |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        " /|\   |\n"
        " /     |\n"
        " ______|_",

        "  ______\n"
        "  |    |\n"
        "  O    |\n"
        " /|\   |\n"
        " / \   |\n"
        " ______|_",
        ]
    for state in states:
        yield state


def generate_word():
    random_word = choice(["haphazard", "jazziest", "wyattsucksass"])
    return random_word.lower()


word = generate_word()
word_list = [char for char in word]

guessed_word = ["_" for x in word]

try:
    guess = []
    gen_state = hangman_states()
    print(next(gen_state))
    print("Word: ", *guessed_word)
    print("Guesses: ")
    while True:
        guess.append(input("Enter your letter guess: ").lower())
        if guess[-1] in word_list:
            print(f"\nNice! {guess[-1]} is in the word!\n")
            print(gen_state.current)
            for letter in guess:
                copy_of_word = word_list.copy()
                n = 0
                while copy_of_word.count(letter) != 0:
                    i = copy_of_word.index(letter) + n
                    guessed_word[i] = letter
                    copy_of_word.remove(letter)
                    n += 1
            if set(guessed_word) == set(word_list):
                print("\nYou win!")
                print(f"The word was {word}")
                break
        else:
            print(f"\nBummer! {guess[-1]} is not in the word! \n{next(gen_state)}\n")
        print("Word: ", *guessed_word)
        print("Guesses: ", *guess)
except StopIteration:
    print("You lose!")
    print(f"The word was {word}")
    print(gen_state.current)
