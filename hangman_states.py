def hangman_states(state):
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

        "  ______\n"
        "  |    |\n"
        "  x    |\n"
        " /|\   |\n"
        " / \   |\n"
        " ______|_",
        ]

    states.reverse()
    return states[state]
