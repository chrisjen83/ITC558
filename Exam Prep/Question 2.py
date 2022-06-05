import turtle

# turtle.goto(-200,460)

if -300 < turtle.xcor() < 450 and -300 < turtle.ycor() < 200:
    # Set Green Colour
    turtle.fillcolor('green')

    turtle.begin_fill()
    # Create the Square
    for side in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
else:
    # Create a circle with blue pen
    turtle.pensize(10)
    turtle.pencolor('blue')
    turtle.circle(75)

turtle.done()





