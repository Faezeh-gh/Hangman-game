import random


def hangman_game():
    words = ['lion', 'mouse', 'tiger', 'owl', 'duck', 'monkey', 'snake', 'frog', 'turtle', 'elephant', 'bear', 'zebra',
             'wolf', 'dog', 'cat']
    selected_word = random.choice(words)
    guesses = []
    number_of_tries = 6

    while number_of_tries > 0:
        show_word = ""
        for char in selected_word:
            if char in guesses:
                show_word += char + " "
            else:
                show_word += "_ "
        print(show_word)

        if "_" not in show_word:
            print("*YOU WON*")
            return

        letter = input("*Enter a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("*Error...\n*Please enter one letter*")
            continue

        if letter in guesses:
            print("*You have already chosen this letter*")
            continue

        guesses.append(letter)

        if letter in selected_word:
            print("*Good choice*")
        else:
            number_of_tries -= 1
            print("*You lost 1 of your chance.*\n*You just have: *", number_of_tries)

    print("*Oops...\n*You lost the game*\n*The chosen word was *", selected_word)


hangman_game()

