# Author:  Aaron Clure
# Travel Time Calculator
# This program will take user inputs for distance and speed and calculate the travel time.

# intitialize variables and set to 0 to clear any unwated data
userDistance = 0
userSpeed = 0
calcHours = 0
calcMinutes = 0
milesRemaining = 0

print("How far is your trip (to the nearest miles)?")
userDistance = int(input()) # force variable to float
print("How fast will you be driving (to the nearest mile per hour)?")
userSpeed = int(input()) # force variable to float
if userSpeed == 0 or userDistance == 0:   # avoid infiinte computations
    print("Try again.  Enter only non-zero values.")
    exit() #kill current run

calcHours = userDistance // userSpeed
milesRemaining = userDistance % userSpeed # 
calcMinutes = (milesRemaining * 60) // userSpeed

print("Your trip will take approximately")
print("Hours: ", calcHours)
print("Minutes: ",calcMinutes)