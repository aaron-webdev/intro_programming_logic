# Author : Aaron Clure
# Even or Odd Checker
# Create a program that will take a user input and output if the number is even or odd.

def num_is_even (userNum):  # function checks if input is even and returns True if true
    remainder = userNum%2   # even numbers will equal 0
    if remainder == 0:
        return True
    else:
        return False
        

def main ():
    print("\t Input any whole number.")
    userNum = int(input())  # convert data type
    num_is_even (userNum)   # call check function
    result = num_is_even(userNum)  # store return to use in a boolean
    if result:
        print(f"\t {userNum} is an even number.")
    else:
        print(f"\t {userNum} is an odd number.")


print("\t Even or Odd Checker.")
print()
main()  # calls main function after displaying the title