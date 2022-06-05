# Must import turtle module first
import turtle

# Create a full circle, radius attribute makes circle bigger or smaller
# Circle always completed a full circle
turtle.circle(75)

# Create a semi circle, second attribute determines if the circle is complete
turtle.circle(75, 180)

# Create a Square, side angle is 90 degrees
for side in range(4):
    turtle.forward(50)
    turtle.turn.right(90)

# Create Dimond
turtle.setheading(45)

for side in range(4):
    turtle.forward(100)
    turtle.right(90)

# Create five pointed star, side angle is 144 degrees
for side in range(5):
    turtle.forward(100)
    turtle.right(144)

# Create Octagon, side angle is 45 degrees
for side in range(8):
    turtle.forward(50)
    turtle.right(45)

# Create Hexagon, side angle is 60 degrees
for side in range(6):
    turtle.forward(50)
    turtle.right(60)

# Create Pentagon, side angle is 72 degrees
for side in range(5):
    turtle.forward(50)
    turtle.right(72)

# Create Equilateral Triangle, interior angles are 120 degrees
for side in range(3):
    turtle.forward(100)
    turtle.left(120)

# Create Isosceles Triangle
turtle.forward(100)
turtle.left(135)
turtle.forward(142)
turtle.left(135)
turtle.forward(100)

# Create Figure of 8
for side in range(2):
    turtle.circle(75)
    turtle.right(180)

# Create an Arch, range(72) will give full circle. Adjusting the range will determine how far the arch is drawn
for i in range(20):
    turtle.forward(10)
    turtle.left(5)

# Create a Spiral pattern, with fill
for i in range(36):
    turtle.forward(150)
    turtle.right(170)

# Create a shape pattern, nested for loop. Pentagram, Hexagram, Octogram
for num in range(12):
    turtle.right(30)
    for side in range(5):
        turtle.forward(50)
        turtle.right(72)

# Calculating if a turtle is inside a shape
# Given two coordinates take X from one and Y from other. Use AND for inside a shape use less than <
# -300, -300
#  200,  450
#   X     Y

if {POINT_1_X} < turtle.xcor() < {POINT_2_Y} and -300 < turtle.ycor() < 200:
    # Add instruction for turtle here for inside
else:
    # Add instructions here for outside the shape
