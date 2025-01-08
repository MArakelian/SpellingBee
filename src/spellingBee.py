"""A small script to provide solutions to the NYT Spelling Bee Game"""

from functions import *

#  TODO: Find a more accurate list of words
#   The actual words used by the NYT does not
#   include all words in the dictionary.
#   so there will be some words provided here
#   that do not work in the game.


def main():
    # Filename
    filename = "../assets/words.txt"

    # Get the initial list of words from our .txt file
    words = initital_words(file=filename)

    # Only include words longer than four letters
    four_letter_words = [x for x in words if len(x) >= 4]

    # Read in the magic letter
    magic_letter = input("What letter must be in each word?: ")

    # Eliminate words that do not contain the magic letter
    words_with_letter = [x for x in four_letter_words if magic_letter in x]

    # Obtain the other letters in a list
    required_letters = [
        input("Please input a required letter and press Enter: ") for _ in range(6)
    ]

    # Add magic_letter to required_letters
    required_letters.append(magic_letter)

    # Eliminate words that contain letters
    solutions = eliminate_words(words_with_letter, required_letters)

    # Print our solutions
    print(solutions)


if __name__ == "__main__":
    main()
