# Read the Dictionary words into a list

words = []

with open("words.txt", "r") as words_file:
    for line in words_file:
        words.extend(line.split())

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

# Add magic_letter to required_letters (so you don't filter out words with magic_letter in last loop)
required_letters += magic_letter


solutions = []
non_solutions = []

# eliminate words that contain letters that aren't in our list of required letters
# THIS DOES NOT WORK

for word in words_with_letter:
    if all(letter in required_letters for letter in word):
        solutions.append(word)
    else:
        non_solutions.append(words)
print(solutions)