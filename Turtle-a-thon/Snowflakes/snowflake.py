import turtle
t = turtle.Turtle()
t.hideturtle()
#turtle.tracer(0)

def draw_koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_curve(t, length / 3, depth - 1)
            t.left(angle)

def draw_koch_snowflake(t, start_pos, length, depth, color):
    t.penup()
    t.goto(start_pos)
    t.pendown()
    
    t.begin_fill()
    for i in range(3):
        t.pencolor(color)
        t.fillcolor(color)
        draw_koch_curve(t, length, depth)
        t.right(120)
    t.end_fill()

# Turtle setup
turtle.bgcolor('black')
t.speed(0)

draw_koch_snowflake(t, (-150, 90), 300, 4, '#0000FF')
draw_koch_snowflake(t, (-100, 65), 200, 4, '#007FFF')
draw_koch_snowflake(t, (-50, 35), 100, 4, '#00BFFF')
draw_koch_snowflake(t, (-25, 15), 50, 4, '#00FFFF')
draw_koch_snowflake(t, (-14, 8), 25, 4, '#B0E0E6')

turtle.done()