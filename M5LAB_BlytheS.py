#CTI-110-0004
#M5LAB: Nested Loops  
#Samuel Blythe
#10-23-17
#

def main():

#Importing turtle and changing shape and color

    import turtle
    ts = turtle.Screen()
    ts.bgcolor("lightblue")
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.pensize(2)
    turt.color("darkgrey")


#For Loop and Movement
    turt.right(180)

    for t in range(8):
        for t2 in range(2):
            turt.forward(100)
            turt.right(90)
        turt.forward(100)
        turt.left(45)
    

main()
