# CTI-110 
# M3HW1 - Age Classifier 
# Samuel Blythe
# 9/13/17
#

def main():

    stop = 'N'
    
    while stop =='N':
    
        age = int(input('How old are you? '))

        if age <= 1:
            print('You are an infant')
        elif age >=2 and age <=12:
            print('You are a child')
        elif age >=13 and age <=20:
            print('You are a teen')
        else:
            print('You are an adult')


        stop = input('Would you like to exit? (N) (Y): ')    

    
main()
