#CTI-110
#M5HW3 - Factorial
#Samuel Blythe
#

def main():
    
    userNumber = int(input('Enter a positive number: '))
    
    while userNumber < 1:
        userNumber = int( input('Please make sure the number entered is positive:'))

    factorial = 1

    for totalNumber in range(1,userNumber + 1):
        factorial = factorial*totalNumber

    print('The factorial of',userNumber,'is',factorial)

main()
