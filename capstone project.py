import turtle
import random
screen=turtle.Screen()
screen.bgpic("game background.gif")
screen.addshape("resized person icon.gif")
screen.addshape("platform.gif")
#screen.addshape("Obstacles python.gif")
screen.tracer(0)
#images=["Obstacles python.gif","platform.gif"]
p=turtle.Turtle()
p.shape("resized person icon.gif")
screen.listen()
score=0
pen=turtle.Turtle()
pen.up()
pen.goto(-600,300)
pen.color("orange")
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
    if (p.ycor()>-675 and p.xcor()<700):
        p.dy=5
     #   p.dx=5
    #p.setx(p.xcor()+p.dx)
    p.sety(p.ycor()+p.dy)
screen.onkey(jump,'space')
obstacles=[]
def spawn_obstacle():
    obs=turtle.Turtle()
    #obs.shape(random.choice(images))
    obs.shape("platform.gif")
    obs.hideturtle()
    x=600
    y=random.randint(-200,300)
    obs.penup()
    obs.goto(x,y)
    obstacles.append(obs)
    screen.ontimer(spawn_obstacle,random.randint(2500,3500))
    obs.showturtle()
def is_on_ground():
    """Check if player stands on ground"""
    return p.ycor()<=-300 + 70
def is_on_obstacle():
    global score
    for obs in obstacles:
        ox,oy=obs.xcor(),obs.ycor()
        if (abs(p.xcor()-ox)<30):

            if p.dy<=0 and p.ycor()<=oy+45 and p.ycor()>oy+20:
                p.sety(oy+45)
                p.dy=0
                score=score+1
                pen.clear()
                pen.write("Score:"+str(score))

def gameloop():
    global obstacles
    p.dy+=-0.7
    p.sety(p.ycor()+p.dy)
    if is_on_ground():
        p.sety(-300+70)
        p.dy=0

    for obs in obstacles:
        obs.setx(obs.xcor()-5)
        if obs.xcor()<-600:
            obs.hideturtle()
            obstacles.remove(obs)
    is_on_obstacle()

    screen.update()
    screen.ontimer(gameloop,20)
        
spawn_obstacle()
gameloop()




screen.mainloop()
