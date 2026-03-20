# Author: Aaron Clure
# Lab 11 
# Grade Calculator

# !/usr/bin/env python3
def getGradeAvg(allGrades):
    all_Grades = allGrades
    weights = [0.4,0.4,0.2]
    averages = []
    finalGrade = 0
    
    for category in all_Grades:
        catTotal = 0
        for grade in category:
            catTotal += grade
            catAvg = catTotal/(len(category))
        averages.append(catAvg)

    for i in range(len(weights)):
        finalGrade += weights[i]*averages[i]
    return(finalGrade)

def main():
    allGrades = []
    categories = ["Lab", "Exam", "Quiz"]
    userGrade = 0
    
    for category in categories:
        i=1
        categoryGrades = []
        print(f"Enter your {category} grades. Enter a negative number to stop:")
        while (userGrade := float(input(f"{category} Grade {i}: "))) >= 0 :
            categoryGrades.append(userGrade)
            i+=1
        allGrades.append(categoryGrades)
    
    finalGrade = round(getGradeAvg(allGrades),2)
    print(f"\n\n\nCalculating your class grade...\n") 
    print(f"Your overall class grade is {finalGrade}")

if __name__ == "__main__":
    main()