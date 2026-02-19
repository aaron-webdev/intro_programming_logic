# Author : Aaron Clure
# String and List Explorer


# Take a user input
print("\t Input a sentence, then press enter.")
userSent = input()
print("\t Input a word from that sentence.")
trackedWord = input()
lowUserSent = userSent.lower() # Convert to all lower to ensure correct alphabetization
splitSent = lowUserSent.split()

# Number of words in the sentence
wordCount = len(splitSent)
# Alphabetize [sort()].
alphSent = sorted(splitSent)
# Reverse alphabetize [reverse()].
revAlphSent = sorted(splitSent, reverse=True)
# Count user selected word [count()].

# Print in all caps [upper()].
# Print in all lower case [lower()].
# Hyphenate the sentance [replace()].
# Outputs
print(f"\tWord Count: {wordCount}")
print(f"\tAlphebatized Sentence: {alphSent}")
print(f"\tReversed Aplabetized List: {revAlphSent}")



# you need to make the string into a list, 
# before you can sort and do other list things.
# newList = userInput.split().
# inside the () is for a delimiter.
# If left empty any white space will be the delimiter.
# aka where the string is broken into substrings.