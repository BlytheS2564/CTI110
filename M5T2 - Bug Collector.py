#CTI-110
#M5T2 - Bug Collector
#Samuel Blythe
#10/09/17
#

def main():

    # Initialize the accumulator
    totalBugs=0

    #Get number of bugs collected per day
    for day in range(1,8):
        #Prompt User
        print('How many bugs were collected on day', day, '?')

        # Input number of bugs
        dayBug = int(input())

        #Add bugs to total
        totalBugs += dayBug
        
    #Display the total of bugs
    print('You collected', totalBugs, 'bugs.')



main()
