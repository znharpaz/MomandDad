import turtle
import random
h = 10
wn = turtle.Screen()
Zach = turtle.Turtle()
Hello = turtle.Turtle()
Hello.right(180)
Zach.speed(100000)
Hello.speed(100000)
wn.colormode(255)
while True:
    for i in range(10,100000000, 20):
        a = random.randint(0,256)
        b = random.randint(0,256)
        c = random.randint(0,256)
        Zach.color(a,b,c)
        Hello.color(a,b,c)
        Zach.goto(0,0)
        Zach.circle(i)
        Hello.goto(0,0)
        Hello.circle(i)
        
    
      
wn.exitonclick()