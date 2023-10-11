import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "brown", 30, 35, 50)
draw_circle(tommy, "brown", 30, -35, 50)

draw_circle(tommy, "pink", 25, 30, 50)
draw_circle(tommy, "pink", 25, -30, 50)

draw_circle(tommy, "brown", 50, 0, 0)

draw_circle(tommy, "pink", 30, 0, 0)

draw_circle(tommy, "black", 20, 0, 15)

draw_circle(tommy, "black", 10, -20, 60)
draw_circle(tommy, "black", 10, 20, 60)

tommy.hideturtle()