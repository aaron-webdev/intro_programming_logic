#!/usr/bin/env python3
# Author: Aaron Clure
# Week 13 Class Practice


# Write a program that asks for two numbers and calculates their division
# Handle user inputs wrong data types or if the user attempts to divide by zero
# def divide_numbers():
#     try:
       
#         num1 = float(input("Input the numerator:\t"))
#         num2 = float(input("Input the denominator:\t"))
        
#         dividend = num1 / num2
#         print(f"The result is: {dividend}")
        
#     except ValueError:
#         print("Error: Invalid data type. Please enter numeric values only.")
#     except ZeroDivisionError:
#         print("Error: Can not divide by zero.")

# divide_numbers()

# Write a program that asks the user to type the name of the file and attempts to open the file and read the contents
# FileNotFoundError
# PermissionError

# fileName = input("Please enter the name of the file you would like to open: ")
# fileName = "E:\\PythonProgrammingLabs\\intro_programming_logic\\week13\\textDoc.txt"
# try:
#     with open(fileName, mode='r') as testFile:
#         print(testFile.read())
#         # Manually raising this for demonstration as per your request
#         raise PermissionError 
# except PermissionError:
#     print("Permission Denied")
# except FileNotFoundError:
#     print("Try looking for another file")


# Write a program that will let a user enter an expression and the code with parse the input and then run the calulation
# error handle for zero division, invalid opperators, invalid data types

expression = input(f"\tInput a mathematical expression then press enter.\n").strip()
splitExpress = expression.split()
print(splitExpress)
try:
    num1 = int(splitExpress[0])
    operator = splitExpress[1]
    num2 = int(splitExpress[2])

except ZeroDivisionError:
    print(f"Can not divide by zero.")