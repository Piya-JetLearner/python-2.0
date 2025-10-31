import turtle
screen=turtle.Screen()
screen.bgpic("game background.gif")
screen.addshape("resized person icon.gif")
screen.addshape("platform.gif")
p=turtle.Turtle()
p.shape("resized person icon.gif")
screen.listen()
#Ground drawing
ground=turtle.Turtle()
ground.penup()
ground.goto(-625,-300)
ground.color("green")
ground.pendown()
ground.begin_fill()
for i in range(2):
    ground.forward(1250)
    ground.right(90)
    ground.forward(50)
    ground.right(90)
ground.end_fill()

p.penup()
p.dy=0
p.dx=0
def jump():
    if p.ycor()>-675:
        p.dy=5
        p.dx=5
    p.setx(p.xcor()+p.dx)
    p.sety(p.ycor()+p.dy)
screen.onkey(jump,'space')
screen.mainloop()

