#CTI-110-0004
#Samuel Blythe
#M6T1 - Kilometer Converter
#

# Converts kilometers to miles.
MILES_CONVERSION = 0.6214

# Obtains distance in kilometers and calls
# the show_miles function to convert it.
def main():
    # Obtains the kilometers from the user.
    kilometers = float(input('Please enter a distance in kilometers: '))

    # Displays the converted distance and calls the function to calculate.
    show_miles(kilometers)
    
# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):

    # Calculate miles.
    miles = km * MILES_CONVERSION

    # Display miles.
    print(km, 'kilometers equals', format(miles, ',.4f'), 'miles.')

# Calls the main function.
main()
    
