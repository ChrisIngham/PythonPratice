import turtle

def drawSquare(x, sz):
    
    for i in range(4):
        x.forward(sz)
        x.left(90)

wn = turtle.Screen()       
wn.bgcolor("Navy Blue")

turt = turtle.Turtle()     
turt.color('yellow')
turt.pensize(4)

for i in range(5):
    drawSquare(turt, 40)   
    turt.penup()
    turt.forward(-100)       
    turt.pendown()

wn.exitonclick()
