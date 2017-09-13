#CTI 110
#Areas of Rectangles
#Samuel Blythe
#9/11/17

#Rectangle 1 Length Width
length1 = int(input ('What is the length of rectangle 1?: '))
width1 = int(input ('What is the width of rectangle 1?: '))

#Rectangle 2 Length Width
length2 = int(input ('What is the length of rectangle 2?: '))
width2 = int(input ('What is the width of rectangle 2?: '))

# Calculate Area
area1 = length1 * width1
area2 = length2 * width2

#Which is greater
if area1 > area2:
    print('Rectangle 1 has the greater area')
elif area1 < area2:
    print('Rectangle 2 has the greater area')
else:
    print('The areas are the same')
