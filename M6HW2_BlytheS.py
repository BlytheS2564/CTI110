
#CTI-110-0004
#Samuel Blythe
#M6HW2 - Guessing Game
#

#Main funtion of program
def main():
    replay = 'y'
    #While loop will keep the game running as long as user hits "y"
    while replay == 'y':
    #Executes the play_game function
        play_game()
        #Asks the user if they would like to play again
        print('Would you like to play again?')
        replay = input('Enter "y" to continue or "n" to quit: ')
    

#Function that contains the game
def play_game():
    #Imports random number
    import random
    #Sets range for random number
    randomNumber = random.randint(1,100)
    #Greeting message
    print('Try to guess the winning number between 1 - 100')
    #Stores user input as guess
    guess = int(input('Enter your guess: '))

    #While loop with if elif statement will run until guess matches number
    while guess != randomNumber:
        if randomNumber < guess:
            print('Too high, try again!')
            guess = int(input('Enter a number: '))
        elif randomNumber > guess:
            print('Too low, try again!')
            guess = int(input('Enter a number: '))
    #Message letting the user know that they guessed correctly
    print('Correct!')
    print('You win!')

main()

