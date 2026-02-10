def sales_tax(total): # added :
    sales_tax = total * 0.06 # changed to numeric value
    newTotal = total + sales_tax # create new variable to store the new total
    return newTotal # return the new calculated value

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(sales_tax(total), 2) # call calculator function and pass user input, returns the new total
    print("Total after tax: ", total_after_tax)
    
main()