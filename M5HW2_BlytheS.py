#CTI-110
#M5HW2 - Running Total
#Samuel Blythe
#

def main():

    total=0
    
    enteredNumber = int(input('Type a positive number to add or a negative number to quit:'))
    
    while enteredNumber > -1:
        total = total + enteredNumber
        enteredNumber = int(input('Type another number:'))
    
    print('Total:', total)
                         
main()
