# Author : Aaron Clure
# String and List Explorer


# Take a user input
print("\t Input a sentence, then press enter.")
userSent = input()
print("\t Input a word from that sentence.")
word = input()
userWord = word.lower()
lowUserSent = userSent.lower() # Convert to all lower to ensure correct alphabetization
splitSent = lowUserSent.split()

# Number of words in the sentence
wordCount = len(splitSent)
# Alphabetize [sort()].
alphSent = sorted(splitSent)
# Reverse alphabetize [reverse()].
revAlphSent = sorted(splitSent, reverse=True)
# Count user selected word [count()].
wordOccurrence = splitSent.count(userWord)
# Hyphenate the sentance [replace()].
hyphonSent = userSent.replace(" ", "-")


# Outputs
print(f"\tWord Count: {wordCount}")
print(f"\tAlphebatized Sentence: {alphSent}")
print(f"\tReversed Aplabetized List: {revAlphSent}")
print(f"\t{userWord} appeared {wordOccurrence} times")
print(f"\t{userSent.upper()}")# Print in all caps [upper()].
print(f"\t{userSent.lower()}")# Print in all lower case [lower()].
print(f"{hyphonSent}")