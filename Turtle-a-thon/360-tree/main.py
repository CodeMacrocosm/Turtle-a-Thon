import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.left(90)
t.speed(20) 
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(4)
        t.pencolor("peru")
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.backward(l)
draw(20)
t.right(90)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(4)
        t.pencolor("saddle brown")
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.backward(l)
draw(20)
t.left(270)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(4)
        t.pencolor("peru")
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.backward(l)
draw(20)
t.right(90)
t.speed(2000)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(4)
        t.pencolor('saddle brown')
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.backward(l)


draw(20)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("light green")
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.backward(l)
draw(40)
t.right(90)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("sea green")
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.backward(l)
draw(40)
t.left(270)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("light green")
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.backward(l)
draw(40)
t.right(90)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor('sea green')
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.backward(l)
draw(40)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(1)
        t.pencolor("light green")
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.backward(l)
draw(45)
t.right(90)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(1)
        t.pencolor("sea green")
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.backward(l)
draw(45)
t.left(270)
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(1)
        t.pencolor("light green")
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.backward(l)
draw(45)
t.right(90)
# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(1)
        t.pencolor('sea green')
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw(45)
t.hideturtle()
turtle.done()