"""Functions for the Spelling Bee Solver"""


def initital_words(file):
    """Read the Dictionary words into a list"""

    words = []

    with open(file, "r") as words_file:
        for line in words_file:
            words.extend(line.split())

    return words


def eliminate_words(words_with_letters, required_letters):
    """Eliminate the words that do not contain the required letters"""
    solutions = []
    non_solutions = []

    for word in words_with_letters:
        if all(letter in required_letters for letter in word):
            solutions.append(word)
        else:
            non_solutions.append(word)

    return solutions
