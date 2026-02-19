# print("\t input two integers. Press enter between numbers.")
# userNum1 = int(input())
# userNum2 = int(input())
# if userNum1 > userNum2 :
#     print(f"\t {userNum1}")
# elif userNum1 < userNum2 :
#     print(f"\t{userNum2}")
# else :
#     print(f"\t{userNum1} = {userNum2}")

# count = 0
# while count <= 10 :
#     if count%2 == 0:
#         print(count)
#     count = count + 1

# for count in range(0,11,1):
#     if count%2 == 0:
#         print(count)

# print("\t Input an integer.")
# userNum = int(input())
# calcSum = 0
# for count in range(1,userNum,1):
#     print(f"count={count}")
#     calcSum += count
# print(calcSum+userNum)

text = "Python is fun and easy."
total=0
for char in text :
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        total += 1
print(total)