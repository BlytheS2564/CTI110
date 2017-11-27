#CTI-110
#M5HW1 - Distance Traveled
#Samuel Blythe
#

def main():

    carSpeed = int( input('How fast was the vehicle travelling?(mph)'))
    carTime = int( input('How many miles did the vehicle travel?'))

    print('Hour','\tDistance Traveled')
    print('-------------------------')

    for carHours in range(1,carTime + 1):
        carDistance = carSpeed*carHours
        print(carHours ,'\t',carDistance)

main()
