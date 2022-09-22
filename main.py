# python_hangman

import random

word_bank = ["amusement", "balance", "chemical", "development"]
round_word = random.choice(word_bank)
print(f"Round word is {round_word}")

game_display = []
for each_letter in range(len(round_word)):
    game_display += "_"


def letterguess():
    guess = input("Guess a letter: ").lower()
    accumulator = 0
    # compare user guess to round word
    for letter in round_word:
        if letter == guess:
            # replace "_" with correct letter
            game_display[accumulator] = guess
            # add to accumulator at the end of the loop for correct letter position
        accumulator += 1
    print(game_display)


while "_" in game_display:
    letterguess()

if "_" not in game_display:
    print("You Win!")
