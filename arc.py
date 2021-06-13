import turtle
import time
#variables
HEIGHT= 500
WIDTH=800
dx=1
dy=1

#creating a window
windows = turtle.Screen()

#setting up pong
windows.title('Ping-Pong Game')
windows.bgpic('C:\\Users\\royel\\djangoAdvance\\arc\\bg_pic2.png')
windows.setup(WIDTH,HEIGHT)
windows.tracer(0)

#creating object
box =turtle.Turtle()
box.color('yellow')
box.width(10)
box.penup()
box.goto(0,-230)
box.pendown()
box.forward(375)
box.left(90)
box.forward(470)
box.left(90)
box.forward(750)
box.left(90)
box.forward(470)
box.left(90)
box.forward(380)


#ball 
ball = turtle.Turtle()
ball.shape('circle')
ball.color('#800080')
ball.penup()


#bat_left
bat_left = turtle.Turtle()
bat_left.shape('square')
bat_left.color('#800080')
bat_left.penup()
bat_left.shapesize(stretch_len=1,stretch_wid=5)
bat_left.goto(-355,0)


#bat_right
bat_right = turtle.Turtle()
bat_right.shape('square')
bat_right.color('#800080')
bat_right.penup()
bat_right.shapesize(stretch_len=1,stretch_wid=5)
bat_right.goto(355,0)

#net
net = turtle.Turtle()
net.penup()
net.goto(0,-230)
net.left(90)
# net.pendown()
# net.goto(230,0)
# net.left(180)
# net.pendown()

#def left bat function
def left_up():
    y = bat_left.ycor()
    bat_left.sety(y+20)
def left_down():
    y = bat_left.ycor()
    bat_left.sety(y-20)   

#def right bat function    
def right_up():
    y = bat_right.ycor()
    bat_right.sety(y+20)
def right_down():
    y = bat_right.ycor()
    bat_right.sety(y-20)   

def movement():
    ball.goto(ball.xcor()+dx,ball.ycor()+dy)



#on key press
windows.listen()
windows.onkeypress(left_up,'w')
windows.onkeypress(left_down,'s')
windows.onkeypress(right_up,'Up')
windows.onkeypress(right_down,'Down')

#score board
score_left = 0
score_right = 0
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.speed(0)
score.color('#A32CC4')
score.goto(0,210)
score.write('Player A: {}   Player B: {}'.format(score_left,score_right),font=('arial',15),align= 'center')


#to hold window
while True:
    movement()

    #detecting upper boundry
    if ball.ycor() >= 230:
        dy*=-1
    if ball.ycor() <= -230:
        dy = dy*(-1)    
  
    if ball.xcor() >= 375:
        ball.goto(0,0)
        score_left += 10
        score.clear()
        score.write('Player A: {}   Player B: {}'.format(score_left, score_right), font=('arial', 15), align='center')
        time.sleep(0)
    if ball.xcor()<=-320:
        ball.goto(0, 0)
        score_right += 10
        score.clear()
        score.write('Player A: {}   Player B: {}'.format(score_left, score_right), font=('arial', 15), align='center')
        time.sleep(1)
    #collision with bat_right
    if ball.xcor()>=320 and (ball.ycor()>bat_right.ycor()-50 and ball.ycor()<bat_right.ycor()+50):
        ball.setx(320)
        dx *= -1
    #collision with bat_left
    if ball.xcor()<=-310 and (ball.ycor()>bat_left.ycor()-50 and ball.ycor()<bat_left.ycor()+50):
        ball.setx(-310)
        dx *= -1  

    windows.update()