import turtle
import random
h = 10
wn = turtle.Screen()
Zach = turtle.Turtle()
Hello = turtle.Turtle()
Fart = turtle.Turtle()
Poop = turtle.Turtle()
Fart.right(90)
Poop.left(90)
Hello.right(180)
Poop.speed(100000000)
Fart.speed(100000000)
Zach.speed(100000000)
Hello.speed(100000000)
wn.colormode(255)
while True:
    for i in range(10,100000000, 1):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        Zach.color(a,b,c)
        Hello.color(a,b,c)
        Fart.color(a,b,c)
        Poop.color(a,b,c)
        Fart.goto(0,0)
        Zach.goto(0,0)
        Fart.goto(0,0)
        Zach.circle(i)
        Hello.goto(0,0)
        Hello.circle(i)
        Poop.circle(i)
        Fart.circle(i)
        
    
      
wn.exitonclick()