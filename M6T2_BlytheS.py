# Calculates and returns feet to inches
# 11-01-17
# CTI-110-0004 M6T2_Feet to Inches
# Samuel Blythe
#

# Constant number of inches per foot.
INCHES_PER_FOOT = 12

# Main function
def main():
    # Obtain number of feet input from user
    userFeet = int(input('Enter number of feet: '))
    # If else statement to change foot to feet if value is greater than 1 foot
    # Prints converted feet to inches
    if userFeet <= 1:
        print(userFeet, 'foot equals', feet_to_inches(userFeet),'inches.')
    else:
        print(userFeet, 'feet equals', feet_to_inches(userFeet),'inches.')

# Converts feet to inches
def feet_to_inches(userFeet):
    return userFeet * INCHES_PER_FOOT
                 

# Calls the main function.
main()
