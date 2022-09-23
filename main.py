# python_hangman

import random
import os
from ascii import title, stages
from words import word_bank

end_game = False
lives = 6

round_word = random.choice(word_bank)
print(title)
# uncomment below to test
# print(f"Round word is {round_word}")

game_display = []
for each_letter in range(len(round_word)):
    game_display += "_"
print(f"{' '.join(game_display)}")
print(" ")

while not end_game:
    guess = input("Guess a letter: ").lower()

    # clear screen after guessing letter
    def clear():
        os.system('clear')

    # compare user guess to round word
    if guess in round_word:
        if guess in game_display:
            print(f"You've already tried the letter {guess}!")
        accumulator = 0
        for letter in round_word:
            if letter == guess:
                # replace "_" with correct letter
                game_display[accumulator] = guess
                # add to accumulator at the end of the loop for correct letter position
            accumulator += 1
    if guess not in round_word:
        lives -= 1
        print(f"Sorry, {guess} is not correct. Remaining lives: {lives}")
        if lives == 0:
            print(f"You Lose! The word was {round_word}")
            end_game = True
    print(stages[lives])
    print(f"{' '.join(game_display)}")
    print(" ")


if "_" not in game_display:
    print("You Win!")
    end_game = True
