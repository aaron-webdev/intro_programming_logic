# Author: Aaron Clure
# Week 11:
# Lists and Tuples
# !/usr/bin/env python3


fruits = ["banana", "pear", "watermelon", "strawberry", "peach"]
print(fruits) # this will print the literal with brakets and commas (a for loop can be used to format the print)
print(fruits[0],fruits[4])

colors = ["red","blue","green"]
print(f"First List: {colors}")
colors.append("magenta")
colors.insert(1,"cyan")
print(f"New List: {colors}")
print(*colors)


