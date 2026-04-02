#!/usr/bin/env python3

# Author : Aaron Clure
# Week 10 Class Notes
#       Lists pt2

# Function to add item to a list
# def add_to_list(list, item):
#   list.append(item)

# use enumerate(listName, itemName) ~~ look into this ~~
# for item, price in zip(inventory, price):  will zip the lists together
#   print(f"{item} (${price})")

# from the random module: 
# import random 
# random.choice(listName)  -  gets the value of a random index
# random.shuffle(listName)  -  shuffles the values in the list

# shallow copy
# listA = listB

# deep copy
# import copy
# listA = [0,1,2,3,4,5]
# listB = copy.deepcopy(listA)

# Slicing:  LEARN MORE ABOUT THIS
# listName[start:end:step]

# STUDY THIS:
# map and filter
# comprehension  ex:  squares = [n*n for n in numbers if n%2 == 0] >> 
# >> this will make a new list of squares of only the even numbers
# Functions can also be called before te for statement in the comprehension statement

invt = ["staff","hat","bread","potion"]
prices = [27.99, 10.99, 5.99, 19.99]

for i in range(0,len(invt)):
    print(f"{invt[i]} (${prices[i]})")


