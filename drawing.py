import turtle
import random

wn = turtle.Screen()
Zach = turtle.Turtle()
while True:
    a = random.randint(1,200)
    b = random.randint(1,200)
    c = random.randint(1,200)
    d = random.randint(1,200)
    e = random.randint(1,200)

    Zach.forward(a)
    Zach.circle(b)
    Zach.goto(e)
    Zach.backward(c)
    Zach.circle(d)
    
wn.exitonclick()