# Author : Aaron Clure
def feetToMeters(userNum):
    newMeters = round(userNum * 0.3048,2)      # convert and return rounded; 1ft = 0.3048m
    print(f"\t{newMeters} meters.")