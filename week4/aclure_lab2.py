# Author: Aaron Clure
# Letter Grade Converter
# Create a program that will take a numerical input and convert that value to a leter grade

# A - 90-100
# B - 80-89
# c - 70-79
# D - 60-69
# F - < 60

#Take and store user input
print("\t Check your letter grade.")
print("\t Input your number grade (to the nearest tenth)." )
userGrade = float(input())  # forces correct format to avoid errors

#Assign and output letter grade based on numeric value
if userGrade >= 90.0 :
    print("\t Letter Grade:  A")
elif userGrade >= 80.0 and userGrade < 90.0 :
    print("\t Letter grade:  B.")
elif userGrade >= 70.0 and userGrade < 80.0 :
    print("\t Letter grade:  C.")
elif userGrade >= 60.0 and userGrade < 70.0 :
    print("\t Letter grade:  D.")
elif userGrade < 60.0 :
    print("\t Letter grade:  F.")
else:
    print("\t Enter a valid number value for the grade (Between 0.0 and 100.0)")