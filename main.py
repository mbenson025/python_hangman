# python_hangman

# python needs to import the random module
import random


word_bank = ["amusement", "balance", "chemical", "development"]

# ask user to guess a letter then covert to lowercase
user_guess = input("Guess a letter: ").lower()

# choose a random word from the word_bank
round_word = random.choice(word_bank)

# convert word to an array of letters
round_letters = list(round_word)
print(round_letters)

# iterate through letters to check if guess is right or wrong
for letter in round_letters:
    print(letter)
    if letter == user_guess:
        print("Right")
    else:
        print("Wrong")
