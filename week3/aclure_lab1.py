# Author:  Aaron Clure
# Travel Time Calculator
# This program will take user inputs for distance and speed and calculate the travel time.

# intitialize variables and set to 0 to clear any unwated data
userDistance = 0
userSpeed = 0
calcHours = 0
calcMinutes = 0
milesRemaining = 0

print("How far is your trip (in miles)?")
userDistance = int(input()) # force user input into a integer variable
print("How fast will you be driving (in miles per hour)?")
userSpeed = int(input()) # accept user input
if userSpeed == 0 or userDistance == 0:  # force user input into a integer variable
    print("Try again.  Enter only non-zero values.")

calcHours = userDistance // userSpeed
milesRemaining = userDistance % userSpeed # 
calcMinutes = (milesRemaining * 60) // userSpeed

print("Your trip will take")
print("Hours: ", calcHours)
print("Minutes: ",calcMinutes)