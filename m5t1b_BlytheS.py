#CTI-110-0004
#M5T1b - Turtle Graphics  
#Samuel Blythe
#10-11-17
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
#Letter S
    for t in range(1):
        turt.forward(100)
        turt.left(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(100)
        turt.right(90)
        turt.forward(75)
        turt.right(90)
        turt.forward(100)
#Pen up and back down
        turt.penup()
        turt.forward(90)
        turt.pendown()
#Letter B
        turt.forward(100)
        turt.right(90)
        turt.forward(100)
        turt.right(90)
        turt.forward(100)
        turt.right(90)
        turt.forward(100)
        turt.backward(200)
        turt.right(90)
        turt.forward(120)
        turt.left(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(20)
        
    

main()
