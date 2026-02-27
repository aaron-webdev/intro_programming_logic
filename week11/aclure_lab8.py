# Aaron Clure
# Wizard Inventory
# Write code that keeps track and displays the invetory of a wizard

def main():
    invt = ["wooden staff","wizard hat","cloth shoes"]
    print(f"\nThe Wizard Inventory program\n")
    print(f"COMMAND MENU:")
    print(f"show - Show all items")
    print(f"grab - Grab an item")
    print(f"edit - Edit an item")
    print(f"drop - Drop an item")
    print(f"exit - Exit program")

    print(f"Command:")
    userCmd = input()

    if userCmd == "show" :
        i=1
        for item in invt:
            print(f"{i}.  {item}")
            i+=1
        main()

    elif userCmd == "grab":
        if len(invt) > 3:
            print(f"You can't carry any more items. Drop something first.")
        else:
            print(f"Name: ")
            invt.append(input())
            lastItem = invt[-1]
            print(f"{lastItem} was added.")
        main()

    elif userCmd == "edit":
        print(f"Number: ")
        userNum = int(input())
        index = userNum - 1
        print(f"Updated name: ")
        newName = input()
        invt[index] = newName
        print(f"Item number {userNum} has been updated.")
        main()






if __name__ == "__main__":
    main()