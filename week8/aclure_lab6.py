def sales_tax(total): # added :
    sales_tax = total * 0.06 # changed to numeric value
    newTotal = total + sales_tax
    return newTotal

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
main()