# Author: Aaron Clure
# Lab 11 
# Grade Calculator

# remove redundant code with functions.

def getGradeAvg(labGrades,examGrades,quizGrades):
    # write a block that will itterate through the list of lists to total and then average the grades weighting the final average appropriately.
    print()
    

def main():
    allGrades = []
    categories = ["Lab", "Exam", "Quiz"]
    userGrade = 0
    

    for category in categories:
        i=1
        gradeSum = 0
        print(f"Enter your {category} grades. Enter a negative number to stop:")
        while (userGrade := float(input(f"{category} Grade {i}: "))) >= 0 :
            gradeSum+=userGrade
            i+=1
            print(f"Grade Sum: {gradeSum}")



    
    
    # print(f"\n\n\n")
    # for grade in labGrades:
    #     print(f"lab grade: {grade}") 
    
    # for grade in examGrades:
    #     print(f"exam grade: {grade}")
    
    # for grade in quizGrades:
    #     print(f"quiz grade: {grade}")


if __name__ == "__main__":
    main()