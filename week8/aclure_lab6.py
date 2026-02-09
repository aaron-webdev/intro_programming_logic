#!/usr/bin/env python3

TAX = 0.06

def sales_tax(total): # added :
    sales_tax = total * 0.06 # changed to numeric value
    newTotal = total * sales_tax
    return newTotal

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    sales_tax(total)
    total_after_tax = round(newTotal, 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
