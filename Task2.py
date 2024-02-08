import turtle
import math


def draw_pythagoras_tree(x, y, length, angle, level):
    if level == 0:
        return
    else:
        # Draw the main branch
        x1 = x + length * math.cos(angle)
        y1 = y + length * math.sin(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x1, y1)

        # Draw the first sub-branch (left)
        draw_pythagoras_tree(x1, y1, 0.7 * length, angle - math.pi / 4, level - 1)

        # Draw the second sub-branch (right)
        draw_pythagoras_tree(x1, y1, 0.7 * length, angle + math.pi / 4, level - 1)


# Get user input for recursion level
while True:
    try:
        recursion_level = int(input("Enter the recursion level: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Set up the turtle
turtle.speed(2)  # You can adjust the speed if needed

# Set the initial position and heading
turtle.penup()
turtle.setpos(0, -200)
turtle.setheading(90)  # Початковий кут нахилу 90 градусів (вгору)
turtle.pendown()

# Call the function to draw the Pythagoras tree with the specified recursion level
draw_pythagoras_tree(0, -200, 100, 0, recursion_level)

# Close the turtle graphics window when clicked
turtle.exitonclick()
