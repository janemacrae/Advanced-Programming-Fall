import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

jane = turtle.Turtle()

for i in range(72):
    for i in range(3):
        jane.forward(150)
        jane.left(90)
    jane.forward(150)
    jane.left(85)

window.exitonclick()
