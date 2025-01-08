"""Functions for the Spelling Bee Solver"""


def initital_words(file):
    """Read the dictionary words into a list"""
    with open(file, "r") as words_file:
        return [line.strip() for line in words_file]


def eliminate_words(words_with_letters, required_letters):
    """Eliminate the words that do not contain the required letters"""
    return [
        word
        for word in words_with_letters
        if all(letter in required_letters for letter in word)
    ]
