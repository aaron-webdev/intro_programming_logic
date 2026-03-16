# Author: Aaron Clure
# Debugging the Tax Calculator
# Debug the code.  Fix any errors.

# ORIGINAL CODE
#               >>>>>
# !/usr/bin/env python3
# TAX = 0.06
# def sales_tax(total)
#     sales_tax = total * tax
#     return total
# def main():
#     print("Sales Tax Calculator\n")
#     total = float(input("Enter total: "))
#     total_after_tax = round(total + sales_tax(total), 2)
#     print("Total after tax: ", total_after_tax)    
# if __name__ == "__main__":
#     main()
#               >>>>>
# ORIGINAL CODE

def sales_tax(total):               # Added :
    sales_tax = total * 0.06        # Changed to numeric value.
    newTotal = total + sales_tax    # Create new variable to store the new total.
    return newTotal                 # Return the new calculated value.

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(sales_tax(total), 2)        # Calls sales_tax function.  Rounds returned value two places after the decimal point.
    print("Total after tax: ", total_after_tax)

    
if __name__ == "__main__":
    main()      # Calls main function to start program