import turtle

def draw_pythagoras_tree(branch_length, t, level):
    if level == 0:
        return
    else:
        # Draw the main branch
        t.forward(branch_length)

        # Save the current position and heading
        pos = t.pos()
        heading = t.heading()

        # Draw the first sub-branch (left)
        t.left(45)
        draw_pythagoras_tree(0.6 * branch_length, t, level - 1)

        # Return to saved position and heading
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()

        # Draw the second sub-branch (right)
        t.right(90)
        draw_pythagoras_tree(0.6 * branch_length, t, level - 1)

        # Return to saved position and heading
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()

        # Draw the third sub-branch (center)
        t.left(45)
        t.forward(branch_length * 0.6)
        t.backward(branch_length * 0.6)

# Get user input for recursion level
while True:
    try:
        recursion_level = int(input("Enter the recursion level: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Set up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(2)  # You can adjust the speed if needed

# Set the initial position
my_turtle.left(90)
my_turtle.penup()
my_turtle.setpos(0, -200)
my_turtle.pendown()

# Call the function to draw the Pythagoras tree with the specified recursion level
draw_pythagoras_tree(100, my_turtle, recursion_level)

# Close the turtle graphics window when clicked
turtle.exitonclick()
