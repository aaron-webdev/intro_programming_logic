# Author: Aaron Clure
# Lab 11 
# Grade Calculator

def getGradeAvg(labGrades,examGrades,quizGrades):
    i=0
    for grade in labGrades:
        labTotal =+ grade
        i+=1
    labAvg = labTotal/i

    i=0
    for grade in examGrades:
        examTotal =+ grade
        i+=1
    examAvg = examTotal/i

    i=0
    for grade in quizGrades:
        quizTotal =+ grade
        i+=1
    quizAvg = quizTotal/i

    finalGrade = (labAvg*)+(testAvg*)+(quizAvg*)
    return(finalGrade)
    

def main():
    labGrades = []
    examGrades = []
    quizGrades = []

    print(f"Enter your lab grades. Enter a negative number to stop:")
    i=1
    while (userGrade := float(input(f"Lab Grade {i}: "))) >= 0 :         # gets all of user's lab grades
        labGrades.append(userGrade)
        i+=1

    print(f"Enter your exam grades. Enter a negative number to stop:")
    i=1
    while (userGrade := float(input(f"Exam Grade {i}: "))) >= 0 :         # gets all of user's exam grades
        examGrades.append(userGrade)
        i+=1

    print(f"Enter your quiz grades. Enter a negative number to stop:")
    i=1
    while (userGrade := float(input(f"Quiz Grade {i}: "))) >= 0 :         # gets all of user's quiz grades
        quizGrades.append(userGrade)
        i+=1

    finalGrade = getGradeAvg(labGrades,examGrades,quizGrades)
    print(f"Calculating your class grade...\n\n") 
    print(f"Your overall class grade is {finalGrade}")
    
    
    # print user input to check loading the arrays
    #
    # print(f"\n\n\n")
    # for grade in labGrades:
    #     print(f"lab grade: {grade}") 
    
    # for grade in examGrades:
    #     print(f"exam grade: {grade}")
    
    # for grade in quizGrades:
    #     print(f"quiz grade: {grade}")


if __name__ == "__main__":
    main()