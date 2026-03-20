# Author: Aaron Clure
# Lab 11 
# Grade Calculator

# remove redundant code with functions.

def getGradeAvg(labGrades,examGrades,quizGrades):
    i=0
    labTotal=0
    for grade in labGrades:
        labTotal += grade
        i+=1
    labAvg = labTotal/i
    print(labAvg)

    i=0
    examTotal=0
    for grade in examGrades:
        examTotal += grade
        i+=1
    examAvg = examTotal/i
    print(examAvg)

    i=0
    quizTotal=0
    for grade in quizGrades:
        quizTotal += grade
        i+=1
    quizAvg = quizTotal/i
    print(quizAvg)

    finalGrade = round((labAvg*0.4)+(examAvg*0.4)+(quizAvg*0.2),2)
    return(finalGrade)
    

def main():
    allGrades = [[labGrades],[examGrades],[quizGrades]]
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
    print(f"\n\n\nCalculating your class grade...\n") 
    print(f"Your overall class grade is {finalGrade}")
    
    
    # print(f"\n\n\n")
    # for grade in labGrades:
    #     print(f"lab grade: {grade}") 
    
    # for grade in examGrades:
    #     print(f"exam grade: {grade}")
    
    # for grade in quizGrades:
    #     print(f"quiz grade: {grade}")


if __name__ == "__main__":
    main()