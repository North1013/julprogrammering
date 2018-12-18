#!/usr/bin/env python3.7
import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

def draw_face():
    turtle.pencolor('black')
    turtle.fillcolor('pink')
    turtle.begin_fill()
    turtle.forward(200)
    turtle.circle(80, 160)
    turtle.circle(500, 10)
    turtle.right(70)
    turtle.forward(15)
    turtle.left(70)
    turtle.circle(300, 50)
    turtle.circle(70, 140)
    turtle.end_fill()

def draw_eyes():
    turtle.pencolor('black')
    turtle.fillcolor('white')
    
    turtle.setposition(600, 400)
    turtle.begin_fill()
    turtle.forward(200)
    turtle.end_fill()

    turtle.setposition(800, 400)
    turtle.begin_fill()
    turtle.forward(200)
    turtle.end_fill()
    
def draw_mouth():
    ...

def draw_nose():
    ...

def main():
    screen.setup(width=1920, height=1080, startx=500, starty=500)
    screen.bgpic('pic.gif')

    draw_face()
    draw_eyes()
    # draw_mouth()
    # draw_nose()
    screen.mainloop()

main()
