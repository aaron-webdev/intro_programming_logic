# Author : Aaron Clure
def metersToFeet(userNum):
    newFeet = round(userNum * 3.28084,2)     # convert and return rounded; 1m = 3.28084ft
    print(f"\t{newFeet} feet.")