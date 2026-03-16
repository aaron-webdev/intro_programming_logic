# Author : Aaron Clure
# Feet and Meter Converter
# Create a program that will convert between feet and meters upon request

# Create modules for functions and update code to call and return from modules.
import aclure_feetToMeters as fTm
import aclure_metersToFeet as mTf


def askToRepeat():
    print("\tWould you like to perform another conversion? (Y/N)")       # Ask to continue
    goAgain = input()
    if goAgain == "Y" or goAgain == "y":
        main()
    else:
        print("\tThank you. Onward and upward!")
        exit()



def main():
    print()
    print("\tFeet and Meters Converter.")       # Ask the user for F >> M or F << M
    print()
    print("\tConversions Menu:")
    print("\tA: Feet to meters.")
    print("\tB: Meters to Feet.")
    userChoice = input()
    print()

    if userChoice == "a" or userChoice == "A":
        print("\tNumber of feet?")
        userNum = float(input())      # store and pass value
        newMeters = fTm.feetToMeters(userNum)

    elif userChoice == "b" or userChoice == "B":
        print("\tNumber of meters?")
        userNum = float(input())      # store and pass value
        newFeet = mTf.metersToFeet(userNum)

    else:
        print("\tInvalid input. Input A or B to make a selection.")
        
    askToRepeat()

if __name__ == "__main__":
    main()                             # Starts program