#!/usr/bin/env python3.7

# from turtle import Screen, Turtle
import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

turtle.speed(10)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
num = 0
for i in range(0, 360, 15):
    turtle.setheading(i)
    turtle.forward(200)
    turtle.pencolor(colors[i % 6])
    turtle.fillcolor(colors[i % 6])
    print(i % 6)
    turtle.write(str(i) + '°')
    turtle.left(90)
    turtle.begin_fill()
    turtle.circle(90)
    turtle.circle(80, 180)
    turtle.end_fill()
    turtle.left(90)
    turtle.pencolor('black')
    turtle.forward(200)
    num += i % 6
    turtle.pensize(num)

turtle.hideturtle()
screen.mainloop()
