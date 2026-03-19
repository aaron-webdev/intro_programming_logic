# Author: Aaron Clure
# Lab 11 
# Grade Calculator



def main():
    labGrades = []
    print(f"Enter your lab grades. Enter a negative number to stop:")
    i=1
    while (userGrade := float(input(f"Lab Grade {i}:"))) >= 0 :
        labGrades.append(userGrade)
        i+=1
    
    for grade in labGrades:
        print(f"grade: {grade}")



if __name__ == "__main__":
    main()