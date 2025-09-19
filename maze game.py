import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Register shapes
turtle.shape("square")
turtle.speed(100)
# Maze grid
maze = [
    "XXXXXXXXXXXXXXX",
    "X   X         X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]

# Turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

#Obstacle setup 
obstacles=[]
def create ():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character= maze[y][x]
            screen_x = -288+(x*24)
            screen_y = 288-(y*24)
            if character=="X":
                obstacle=turtle.Turtle()
                obstacle.shape("square")
                obstacle.color("purple")
                obstacle.penup()
                obstacle.goto(screen_x,screen_y)
                obstacles.append(obstacle)
            elif character=="F":
                finish=turtle.Turtle()
                finish.shape("circle")
                finish.color("green")
                finish.penup()
                finish.goto(screen_x, screen_y)
def is_valid_move(x,y):
    for obstacle in obstacles:
        if obstacle.xcor()==x and obstacle.ycor()==y:
            return False
    return True
def move_up():
    new_x= player.xcor()
    new_y = player.ycor()+24
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
def move_down():
    new_x= player.xcor()
    new_y = player.ycor()-24
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
def move_left():
    new_x= player.xcor()-24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
def move_right():
    new_x= player.xcor()+24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
create()
player.goto(-264,264)
screen.mainloop()



