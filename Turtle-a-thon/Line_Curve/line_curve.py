from turtle import *
import turtle
from random import randint

colors = ['#70FF98', '#4285F4', '#FF8259', '#2B23FF']
tur = turtle.Turtle()
tur.penup()
tur.color("#4285F4", "#4285F4")

for ix in range(0, 300, 1):
    color_index = randint(0, 3)
    color_str = colors[color_index]
    tur.color(color_str, color_str)
    point1 = (0, ix)
    tur.goto(point1)
    tur.pendown()
    point2 = (ix, 300 - ix)
    tur.goto(point2)
    tur.penup()

turtle.done()