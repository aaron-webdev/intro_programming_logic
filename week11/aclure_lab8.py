# Aaron Clure
# Wizard Inventory
# Write code that keeps track and displays the invetory of a wizard

invt = ["wooden staff","wizard hat","cloth shoes"]
print(f"\n\tThe Wizard Inventory program\n")
print(f"\tCOMMAND MENU:")
print(f"\tshow - Show all items")
print(f"\tgrab - Grab an item")
print(f"\tedit - Edit an item")
print(f"\tdrop - Drop an item")
print(f"\texit - Exit program")

print(f"Command:")
userCmd = input()

if userCmd == "show" :
    i=1
    for item in invt:
        print(f"{i}.  {item}")
        i+=1
        
elif userCmd == "grab":
    if len(invt) == 4:
        print(f"\tYou can't carry any more items. Drop something first.")
    else:
        print(f"Name the item: ")
        invt = invt.append(input())