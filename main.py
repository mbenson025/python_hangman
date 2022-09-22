# python_hangman

import random
from ascii import title
from ascii import stages
from words import word_bank


end_game = False
lives = 6

word_bank = ["amusement", "balance", "chemical", "development"]
round_word = random.choice(word_bank)
print(title)
print(f"Round word is {round_word}")

game_display = []
for each_letter in range(len(round_word)):
    game_display += "_"

already_guessed = []

while not end_game:
    guess = input("Guess a letter: ").lower()
    # compare user guess to round word
    if guess in round_word:
        accumulator = 0
        for letter in round_word:
            if letter == guess:
                # replace "_" with correct letter
                game_display[accumulator] = guess
                # add to accumulator at the end of the loop for correct letter position
            accumulator += 1
        print(game_display)
    if guess not in round_word:
        lives -= 1
        print(f"Wrong. Remaining lives: {lives}")
        if lives == 0:
            print("You Lose!")
            end_game = True
    print(stages[lives])
    print(game_display)


if "_" not in game_display:
    print("You Win!")
    end_game = True
