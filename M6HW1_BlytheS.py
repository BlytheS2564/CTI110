#Program asks for 5 grades then displays a letter grade and average.
#CTI-110-0004
#Samuel Blythe
#M6HW1 - Test Grading Program
#

#Calls the next two functions and holds the imput commands.
def main():
    
    grade = 0
    totalGrade = 0
    
    print('Enter 5 grades')
    
    for i in range(1):
        grade = int(input('Please enter the first grade: '))
        letterGrade = determine_grade(grade)
        totalGrade += grade

        print(letterGrade)
        
        grade = int(input('Please enter the second grade: '))
        letterGrade = determine_grade(grade)
        totalGrade += grade

        print(letterGrade)
        
        grade = int(input('Please enter the third grade: '))
        letterGrade = determine_grade(grade)
        totalGrade += grade

        print(letterGrade)
        
        grade = int(input('Please enter the fouth grade: '))
        letterGrade = determine_grade(grade)
        totalGrade += grade

        print(letterGrade)

        grade = int(input('Please enter the fifth grade: '))
        letterGrade = determine_grade(grade)
        totalGrade += grade

        print(letterGrade)
        
    print('The grade average is ', calc_average(totalGrade))
    
#Accept 5 scores and return average score.
    
def calc_average(totalGrade):
   return totalGrade / 5

#Accept a score and return a letter grade.

def determine_grade(grade):
    
    if grade >= 90:
        return('The grade is an A')
    
    elif grade <=89 and grade >= 80:
        return('The grade is a B')
    
    elif grade <=79 and grade >= 70:
        return('The grade is a C')
    
    elif grade <=69 and grade >= 60:
        return('The grade is a D')
    
    else:
        return('The grade is an F')

main()
