import turtle
import random

score=0


sea=turtle.Screen()
sea.bgpic("goldhunt.gif")
sea.addshape("left.gif")
sea.addshape("right.gif")
sea.addshape("coin.gif")

hunter=turtle.Turtle()
hunter.shape("left.gif")
hunter.penup()
hunter.goto(0,-150)

scoreboard = turtle. Turtle()
scoreboard.penup()
scoreboard.speed(500)
scoreboard.goto(-100,240)
scoreboard.write("Score: 0", font=("Courier", 27, "bold"))
scoreboard.hideturtle()

coin=turtle.Turtle()
coin.speed(1000)
coin.shape("coin.gif")
coin.penup()
coin.goto(-280,280)


def right():
    hunter.shape("left.gif")
    hunter.forward(5)
def left():
    hunter.shape("right.gif")
    hunter.backward(5)


turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")


turtle.listen()

def move():
    y=coin.ycor()
    coin.sety(y-3)

while True:
    sea.update()
    move()
    
    if coin.ycor()<-300 :
        x=random.randint(-280,280)
        coin.goto(x,280)
    
    if hunter.distance(coin)<50:
        score = score +1
        scoreboard.clear()
        scoreboard.write("score: {}".format(score), font=("Courier",27,"bold"))
        x=random.randint(-280,280)
        coin.goto(x,280)

turtle.done()