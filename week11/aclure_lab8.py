# Aaron Clure
# Wizard Inventory
# Write code that keeps track and displays the invetory of a wizard



# THIS NEEDS TO BE CLEANED UP WITH BETTER FUNCTIONS AND LOGIC FLOW.  EVERYTHING IS WORKING AS IS.
# THIS NEEDS TO BE CLEANED UP WITH BETTER FUNCTIONS AND LOGIC FLOW.  EVERYTHING IS WORKING AS IS.
# THIS NEEDS TO BE CLEANED UP WITH BETTER FUNCTIONS AND LOGIC FLOW.  EVERYTHING IS WORKING AS IS.
# THIS NEEDS TO BE CLEANED UP WITH BETTER FUNCTIONS AND LOGIC FLOW.  EVERYTHING IS WORKING AS IS.
# THIS NEEDS TO BE CLEANED UP WITH BETTER FUNCTIONS AND LOGIC FLOW.  EVERYTHING IS WORKING AS IS.



#!/usr/bin/env python3

def main():
    userCmd = input(f"\nCommand:")

    if userCmd == "show" :  # loop through the list and print each item with its place number
        i=1
        for item in invt:
            print(f"{i}.  {item}")
            i+=1

    elif userCmd == "grab": # limits carried items to 4
        if len(invt) > 3:
            print(f"You can't carry any more items. Drop something first.")
        else:
            invt.append(input(f"Name: "))
            lastItem = invt[-1] # grabs last item in the list
            print(f"{lastItem} was added.")

    elif userCmd == "edit":
        userNum = int(input(f"Number: "))
        index = userNum - 1 # convert from place number to list index number
        newName = input(f"Updated name: ")
        invt[index] = newName
        print(f"Item number {userNum} has been updated.")
    
    elif userCmd == "drop":
        userNum = int(input(f"Number: "))
        index = userNum - 1
        droppedItem = invt.pop(index) # removes specific item from 
        print(f"{droppedItem} was dropped.")

    elif userCmd == "exit":
        exit()

    else:
        print(f"Please input a valid command.")

    main()

invt = ["wooden staff","wizard hat","cloth shoes"]
print(f"\nThe Wizard Inventory program\n")
print(f"\nCOMMAND MENU:")
print(f"show - Show all items")     # print items with a loop
print(f"grab - Grab an item")       # add items to a list
print(f"edit - Edit an item")       # acces an index within a list
print(f"drop - Drop an item")       # remove items from a list
print(f"exit - Exit program")

if __name__ == "__main__":
    main()