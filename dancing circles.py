import turtle 
import random
import time
turtle.hideturtle()
turtle.speed(0)
screen=turtle.Screen()
screen.bgcolor("black")
turtle.colormode(255)
def s():
    turtle.penup()
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle.goto(x,y)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.pendown()
    turtle.color(r,g,b)
    turtle.begin_fill()
    turtle.circle(random.randint(20,70))
    turtle.end_fill()
start=time.time()
for i in range(25):
    s()
    time.sleep(0.25)
    turtle.clear()
end=time.time()
total=end-start
print(total)
