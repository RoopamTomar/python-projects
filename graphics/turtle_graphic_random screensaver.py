import turtle
import random
t = turtle.Turtle()
t.color('blue','cyan')
t.shape("turtle")
t.speed(90)
def fun(x,y,z,r):
    t.begin_fill()
    t.circle(r)
    t.left(90)
    t.end_fill()
    t.color("green",z)
    t.penup()
    t.goto(x,y)
    t.pendown()

for n in range(100):
    color = ["pink","cyan","yellow","brown","orange","grey"]
    a = random.randint(-500,500)
    b = random.randint(-500,500)
    c = random.choice(color)
    d = random.randint(30,150)
    fun(a,b,c,d)

#a = input("enter input:")