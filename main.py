from words import generate_word
from hangman_states import hangman_states


def play_game():
    word = generate_word()
    tries_left = 7
    guesses = []
    word_list = [char for char in word]
    guessed_word = ["_" for char in word]

    print("Welcome to Hangman!")
    while True:
        print(hangman_states(tries_left))
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Guesses: {' '.join(guesses)}" if guesses else "")

        get_input = input("Enter your guess: ")
        if get_input not in guesses:
            guesses.append(get_input)
        else:
            print(f"\nYou already guessed {get_input}!" if get_input != "" else "\nDon't enter blank space!")
            continue

        if guesses[-1] in word_list:
            print(f"\nNice! {guesses[-1]} is in the word!")
            for index, letter in enumerate(word_list):
                if letter == guesses[-1]:
                    guessed_word[index] = letter
        else:
            print(f"\nSorry, {guesses[-1]} is not in the word!")
            tries_left -= 1

        if guessed_word == word_list:
            print(f"You won! The word was {word}")
            break
        elif tries_left == 0:
            print(f"You lost! The word was {word}")
            print(hangman_states(tries_left))
            break

    play_again = input("Would you like to play again? ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")
        return


play_game()
