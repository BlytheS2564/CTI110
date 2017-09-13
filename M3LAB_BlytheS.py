# CTI-110
# M3LAB
# 9/13/17
# Samuel Blythe

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale

    
    score = int(input('Gimme Yo Score:'))

    if score >= 90:
        print('Your grade is: A')
    elif score >= 80 and score <= 89:
        print('Your grade is: B')
    elif score <= 79 and score >= 70:
        print('Your Grade is: C')
    elif score <=69 and score >= 60:
        print('Your Grade is: D')
    else:
        print('Your grade is: F') 



# program start
main()
