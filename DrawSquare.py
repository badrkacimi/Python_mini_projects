import turtle

def draw():
    badr = turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("red")
    n=4
    for i in range(0,n,1) :
     badr.forward(100)
     badr.right(90)
     n+=1

    window.exitonclick()

draw()

