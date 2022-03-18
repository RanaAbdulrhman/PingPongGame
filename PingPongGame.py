import turtle
wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)#stops the window from updating automatically


#racket1 
racket1= turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.color("blue")
racket1.penup()
racket1.goto(-350,0)
#rackit2 
racket2= turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.color("red")
racket2.penup()
racket2.goto(350,0)
#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx= 0.2
ball.dy= 0.2

#score
score1= 0
score2= 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player1: 0, player2: 0", align= "center",font=("Courier",24,"normal"))
#functions

#The movement of racket1
def racket1_up():
  y= racket1.ycor()
  y= y+20 
  racket1.sety(y)

def racket1_down():
  y= racket1.ycor()
  y= y-20 
  racket1.sety(y)

#The movement of racket2
def racket2_up():
  y= racket2.ycor()
  y= y+20 
  racket2.sety(y)

def racket2_down():
  y= racket2.ycor()
  y= y-20 
  racket2.sety(y)

#keyboard
wind.listen()
wind.onkeypress(racket1_up,"w")
wind.onkeypress(racket1_down,"s")
wind.onkeypress(racket2_up,"Up")
wind.onkeypress(racket2_down,"Down")

#main game loop
while True:
  wind.update()

  #movement of the ball
  ball.setx(ball.xcor()+ ball.dx)
  ball.sety(ball.ycor()+ ball.dy)

  #border check
  if ball.ycor()>290:
    ball.sety(290)
    ball.dy=ball.dy*-1

  if ball.ycor()<-290:
    ball.sety(-290)
    ball.dy=ball.dy*-1 

  if ball.xcor() >390:
    ball.goto(0,0)
    ball.dx=ball.dx*-1
    score1 += 1
    score.clear()
    score.write("player1: {}, player2:{}".format(score1,score2), align= "center",font=("Courier",24,"normal"))
    

  if ball.xcor() <-390:
    ball.goto(0,0) 
    ball.dx=ball.dx*-1
    score2 += 1
    score.clear()
    score.write("player1: {}, player2:{}".format(score1,score2), align= "center",font=("Courier",24,"normal"))

  #hiting rackets and the ball  
  if (ball.xcor()>330 and ball.xcor()<340) and (ball.ycor() < racket2.ycor() + 50 and ball.ycor() > racket2.ycor()-50):
    ball.setx(330)
    ball.dx*=-1

  if (ball.xcor()<-330 and ball.xcor()>-340) and (ball.ycor() < racket1.ycor() +50 and ball.ycor() > racket1.ycor()-50):
    ball.setx(-330)
    ball.dx*=-1  


