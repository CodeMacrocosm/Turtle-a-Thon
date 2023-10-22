import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
olympics = turtle.Turtle()
olympics.pensize(6)

# Define the Olympic ring colors and positions
ring_colors = ["blue", "black", "red", "yellow", "green"]
ring_positions = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -60)]

# Draw the Olympic rings
for color, position in zip(ring_colors, ring_positions):
    olympics.penup()
    olympics.color(color)
    olympics.goto(position)
    olympics.pendown()
    olympics.circle(60)

# Hide the Turtle
olympics.hideturtle()

# Keep the window open until the user clicks
screen.exitonclick()