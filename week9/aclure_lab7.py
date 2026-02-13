# Author : Aaron Clure
# String and List Explorer
# 1. Take a user input
# 2. Demonstrate different ways to manipulate strings.

# Count the words in the sentence [count()].
# Alphabetize [sort()].
# Reverse alphabetize [reverse()].
# Count user selected word [count()].
# Print in all caps [upper()].
# Print in all lower case [lower()].
# Hyphenate the sentance [replace()].
def countTrackedWord(userPhrase,trackWord):
     wordCountOutput = userPhrase.count(trackWord)
     return wordCountOutput
def alphabetizedList(userPhrase):
     sortedList=userPhrase.sort()
     return sortedList
def main():
    print(f"\t Enter a sentence: ")
    userPhrase = input()
    print(F"\t Enter a word to count: ")
    trackWord = input()
    wordCountOutput = countTrackedWord(userPhrase,trackWord)
    alphList = alphabetizedList(userPhrase)

# Outputs
    print(f"\t Word chosen: {trackWord} \n\t Occurrences: {wordCountOutput}")
    print(f"\t Alphabatical list: {alphList} ")

main()