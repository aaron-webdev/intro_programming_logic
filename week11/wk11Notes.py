# Author: Aaron Clure
# Week 11:
# Lists and Tuples
# !/usr/bin/env python3


# fruits = ["banana", "pear", "watermelon", "strawberry", "peach"]
# print(fruits) # this will print the literal with brakets and commas (a for loop can be used to format the print)
# print(fruits[0],fruits[4])

# colors = ["red","blue","green"]
# print(f"First List: {colors}")
# colors.append("magenta")
# colors.insert(1,"cyan")
# print(f"New List: {colors}")
# print(*colors)

# numbers = [11,22,33,44,55]
# print(f"Full List: {numbers}")
# numbers.pop(3)
# print(f"Post Pop List: {numbers}")
# numbers.remove(22)
# print(f"Post Remove List: {numbers}")

# numbers = [11,22,33,33,44,55,33]
# numCount = numbers.count(33)
# print(numCount)

# names = ["Steve", "Jason", "Kim", "Darien", "Diane"]
# for name in names:
#     print(f"{name}")
# print("\n\n")
# for i in range(0,len(names)):
#     print(f"{names[i]}")

# animals = ["giraffe","lion","zebra","hippo"]
# animals.append("penguin")
# animals.remove("hippo")
# print(len(animals))
# for animal in animals:
#     print(animal)


# numberMatrix = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]
# rowSums = []
# for row in numberMatrix:
#     rowSum = 0
#     for num in row:
#         rowSum+=num
#     rowSums.append(rowSum)

# columnSums = [0,0,0]
# for row in range(3):
#     for col in range(3):
#         columnSums[col] += numberMatrix[row][col]

# print(rowSums)
# print(columnSums)

# scores = [100,97,64,77,78,79,94,92,99,84]
# maxScore = max(scores)
# minScore = min(scores)
# sumScore = sum(scores)
# print(f"Max: {maxScore}")
# print(f"Min: {minScore}")
# print(f"Sum: {sumScore}")