# Author: Aaron Clure
# Lab 11 
# Grade Calculator

# remove redundant code with functions.

def getGradeAvg(labGrades,examGrades,quizGrades):
    # write a block that will itterate through the list of lists to total and then average the grades weighting the final average appropriately.
    print()
    

def main():
    labGrades = []
    examGrades = []
    quizGrades = []
    allGrades = [[labGrades],[examGrades],[quizGrades]]

    for category in allGrades:
        print(f"Enter your grade. Enter a negative number to stop:")
        i=1
        while (userGrade := float(input(f"Lab Grade {i}: "))) >= 0 :         # gets all of user's lab grades
            category.append(userGrade)
            i+=1
    print(allGrades)

    
    
    # print(f"\n\n\n")
    # for grade in labGrades:
    #     print(f"lab grade: {grade}") 
    
    # for grade in examGrades:
    #     print(f"exam grade: {grade}")
    
    # for grade in quizGrades:
    #     print(f"quiz grade: {grade}")


if __name__ == "__main__":
    main()