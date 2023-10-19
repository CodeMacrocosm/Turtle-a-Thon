import turtle
import colorsys

screen = turtle.Screen()
screen.title('Slanted Rainbow Tree')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def slanted_tree(x,y,length,direction, hue):
    if length < 7: return
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(direction)
    turtle.pensize(length/50)
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    turtle.pencolor(r, g, b)
    turtle.fd(length)
    px,py = turtle.xcor(), turtle.ycor()
    slanted_tree(px,py,length*0.75,direction+45, (hue + 0.1) % 1)
    slanted_tree(px,py,length*0.75,direction-15, (hue + 0.1) % 1)

slanted_tree(50,-250,200,60, 0)
