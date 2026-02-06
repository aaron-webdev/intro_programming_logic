# Author: Aaron Clure
# Change Calculator
# Create a program that will take an value input and putput the coins require to make that change value.  The program then asks to run again.


# Accecpt and store user input
print("\t Input number of cents (0-99):")
userChange=int(input())
quart = 0
dime = 0
nick = 0
penn = 0

# Decrement by userChange while value is greater than or equal to the coin value
while userChange > 24 :
  quart += 1
  userChange -= 25
while userChange > 9 :
  dime += 1
  userChange -= 10
while userChange > 4 :
  nick += 1
  userChange -= 5
while userChange > 0 :
  penn += 1
  userChange -= 1
# Store number of each coin needed to make input value equal zero


# Output coin count
print(f"\t Quarters: {quart}")
print(f"\t Dimes:    {dime}")
print(f"\t Nickles:  {nick}")
print(f"\t Pennies:  {penn}")

# Ask if user wants to restart the program
print("\t Continute? (y/n)")
