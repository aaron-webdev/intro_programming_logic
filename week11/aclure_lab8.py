# Aaron Clure
# Wizard Inventory
# Write code that keeps track and displays the invetory of a wizard

invt = ["wooden staff","wizard hat","cloth shoes"]
print(f"\nThe Wizard Inventory program\n")

def main():
    print(f"\nCOMMAND MENU:")
    print(f"show - Show all items")     # print items with a loop
    print(f"grab - Grab an item")       # add items to a list
    print(f"edit - Edit an item")       # acces an index within a list
    print(f"drop - Drop an item")       # remove items from a list
    print(f"exit - Exit program")

    print(f"\nCommand:")
    userCmd = input()

    if userCmd == "show" :
        i=1
        for item in invt:
            print(f"{i}.  {item}")
            i+=1

    elif userCmd == "grab":
        if len(invt) > 3:
            print(f"You can't carry any more items. Drop something first.")
        else:
            print(f"Name: ")
            invt.append(input())
            lastItem = invt[-1]
            print(f"{lastItem} was added.")

    elif userCmd == "edit":
        print(f"Number: ")
        userNum = int(input())
        index = userNum - 1
        print(f"Updated name: ")
        newName = input()
        invt[index] = newName
        print(f"Item number {userNum} has been updated.")
    
    elif userCmd == "drop":
        print(f"Number: ")
        userNum = int(input())
        index = userNum - 1
        droppedItem = invt.pop[index]
        print(f"{droppedItem} was dropped.")

    elif userCmd == "exit":
        exit()

    else:
        print(f"Please input a valid item number.")


    main()





if __name__ == "__main__":
    main()