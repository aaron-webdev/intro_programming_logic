# Author : Aaron Clure
# Feet and Meter Converter
# Create a program that will convert between feet and meters upon request

def feetToMeters(userNum):
    newMeters = round(userNum * 0.3048,2)      # convert and return; 1ft = 0.3048m
    print(f"\t {newMeters} meters.")
    askToRepeat()

def metersToFeet(userNum):
    newFeet = round(userNum * 3.28084,2)     # convert and return; 1m = 3.28084ft
    print(f"\t {newFeet} feet.")
    askToRepeat()

def askToRepeat():
    print("\t Would you like to continue? (Y/N)")       # Ask to continue
    goAgain = input()
    if goAgain == "Y" or goAgain == "y":
        main()
    else:
        exit()



def main():
    print()
    print("\t Feet and Meters Converter.")       # Ask the user for F >> M or F << M
    print()
    print("\tConversions Menu:")
    print("\tA: Feet to meters.")
    print("\tB: Meters to Feet.")
    userChoice = input()
    print()

    if userChoice == "a" or userChoice == "A":
        print("\t Number of feet?")
        userNum = float(input())      # store and pass value
        feetToMeters(userNum)

    elif userChoice == "b" or userChoice == "B":
        print("\t Number of meters?")
        userNum = float(input())      # store and pass value
        metersToFeet(userNum)

    else:
        print("\t Invalid input. Input A or B to make a selection.")


main() # Starts program