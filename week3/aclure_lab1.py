# Travel Time Calculator 
# This program will take user inputs for distance and speed and calculate the travel time

# intitialize variables and set to 0 to clear any unwated data
userDistance = 0
userSpeed = 0
calcHours = 0
calcMinutes = 0

print("How far is your trip (in miles)?")
userDistance = int(input())
print("How fast will you be driving (in miles per hour)?")
userSpeed = int(input())

calcHours = userDistance // userSpeed
calcMinutes = userDistance % userSpeed

print("Your trip will take")
print("Hours: ", calcHours)
print("Minutes: ",calcMinutes)