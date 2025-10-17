import turtle
screen=turtle.Screen()
screen.tracer(0)
screen.bgcolor("pink")
score=0
scorepen=turtle.Turtle()
scorepen.color("black")
scorepen.penup()
scorepen.goto(-575,300)
scorepen.write("Score: {}".format(score),font=("Courier",16,"normal"))

bricks=[]
x=-500
for i in range(6):
    block=turtle.Turtle()
    block.color("red")
    block.penup()
    block.shape("square")
    block.goto(x,300)
    x=x+200
    bricks.append(block)
x=-500
for i in range(6):
    block=turtle.Turtle()
    block.color("yellow")
    block.penup()
    block.shape("square")
    block.goto(x,200)
    x=x+200
    bricks.append(block)
x=-500
for i in range(6):
    block=turtle.Turtle()
    block.color("green")
    block.penup()
    block.shape("square")
    block.goto(x,100)
    x=x+200
    bricks.append(block)
x=-500
for i in range(6):
    block=turtle.Turtle()
    block.color("blue")
    block.penup()
    block.shape("square")
    block.goto(x,0)
    x=x+200
    bricks.append(block)
paddle=turtle.Turtle()
paddle.color("black")
paddle.penup()
paddle.goto(0,-275)
paddle.shape("square")
ball=turtle.Turtle()
ball.color("purple")
ball.penup()
ball.goto(0,-90)
ball.shape("circle")
def left():
    x=paddle.xcor()
    paddle.setx(x-20)
def right():
    x=paddle.xcor()
    paddle.setx(x+20)
screen.listen()
screen.onkeypress(left,'a')
screen.onkeypress(right, 'd')
ball.dx=0.5
ball.dy=0.5
game=False
def start(x,y):
    global game
    game=True
screen.onclick(start)
while True:
    screen.update()
    if not game: continue
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.xcor()>490 or ball.xcor()<-490:
        ball.dx*=-1
    if ball.ycor()>390:
        ball.dy*=-1
    if ball.ycor()<-390:
        ball.goto(0,0)
        ball.dy*=-1
        game=False
    if ball.distance(paddle)<40:
        ball.dy *=-1
    for block in bricks:
        if ball.distance(block)<40:
            ball.dy *=-1
            block.hideturtle()
            bricks.remove(block)
            score=score+1
            scorepen.clear()
            scorepen.write("Score: {}".format(score),font=("Courier",16,"normal"))


