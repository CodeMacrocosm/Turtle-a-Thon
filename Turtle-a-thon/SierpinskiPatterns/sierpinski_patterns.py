import turtle
import random
import math

screen = turtle.Screen()
screen.title('Sierpinski Patterns')
screen.setup(700, 600)
screen.setworldcoordinates(-200, -200, 200, 200)
screen.tracer(0, 0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

m = int(input("Input a number to draw the particular patter with the number of sides(should be 3 or more - )  "))
angle = math.pi/4
V = []
for i in range(m):
    p = (400*math.cos(angle), 400*math.sin(angle))
    V.append(p)
    angle += math.pi*2/m

for v in V:
    turtle.goto(v)
    turtle.dot('blue')

n = 100000  # number of points to draw
p = V[0]  # start from the first vertex
t = turtle.Turtle()
t.up()
t.hideturtle()
for i in range(n):
    t.goto(p)
    t.dot(2, 'red')
    r = random.randrange(len(V))  # pick a random vertex
    if random.randint(0, 1) == 0:  # randomly decide to use edge or vertex
        q = V[r]  # vertex
    else:
        # go to mid point between two vertices
        q = ((V[r][0]+V[(r+1) % len(V)][0])/2,
             (V[r][1]+V[(r+1) % len(V)][1])/2)
    p = ((q[0]+p[0])/3, (q[1]+p[1])/3)  # go 1/3 towards target
    if i % 1000 == 0:  # update for every 1000 moves, this part is for performance reason only
        t = turtle.Turtle()  # use new turutle
        t.up()
        t.hideturtle()
        screen.update()
