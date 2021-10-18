import turtle
import winsound
import tkinter as tk

window = turtle.Screen()
root = turtle.Screen()._root
root.iconbitmap(r'images.ico')
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#score
score_a = 0
score_b = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"PlayerA: {score_a} PlayerB : {score_b}", align="center", font=("Courier", 24, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main game Loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1  # reverses direction



    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB : {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB : {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() - 80):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Boing.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() - 80):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Boing.wav", winsound.SND_ASYNC)


