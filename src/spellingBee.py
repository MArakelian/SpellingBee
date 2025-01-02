"""A small script to provide solutions to the NYT Spelling Bee Game"""

from functions import *

#  TODO: Find a more accurate list of words
#   The actual words used by the NYT does not
#   include all words in the dictionary.
#   so there will be some words provdied here
#   that do not work in the game.


# Filename
filename = "../assets/words.txt"

# Get the initial list of words from our .txt file
words = initital_words(filename)

# only include words longer than four letters
four_letter_words = [x for x in words if len(x) >= 4]

# Read in the magic letter
magic_letter = input("What letter must be in each word?: ")

# eliminate words that do not contain the magic letter
solutions = words_with_letter = [x for x in four_letter_words if magic_letter in x]

# obtain the other letters in a list

required_letters = []
for l in range(0, 6):
    next_letter = input("Please input a required letter and press Enter: ")
    required_letters += next_letter


# Add magic_letter to required_letters
# (so you don't filter out words with magic_letter in last loop)
required_letters += magic_letter


# eliminate words that contain letters
solutions = eliminate_words(words_with_letter, required_letters)

# Print our solutions
print(solutions)
