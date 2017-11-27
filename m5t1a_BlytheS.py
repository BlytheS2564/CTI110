#CTI-110-0004
#M5T1a - Turtle Graphics  
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
    for t in range(4):
        turt.forward(100)
        turt.left(90)

    for t2 in range(3):
        turt.left(120)
        turt.forward(50)
        
        
    

main()
