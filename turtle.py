import turtle
import time

t = turtle.Turtle()
t.color("red")


def quad_draw(a,b,c,d):
    t.penup()
    t.goto(a)
    t.pendown()
    t.goto(b)
    t.goto(c)
    t.goto(d)
    t.goto(a)

def draw_grid(m,n):
    
    t.forward(m)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(m)
    t.left(90)
    t.forward(n)

a = (50,50)
b = (100,200)
c = (300,200)
d = (60,40)

m = 30
n = 20

quad_draw(a,b,c,d)
draw_grid(20,30)
print(t.pos())   

turtle.done()
