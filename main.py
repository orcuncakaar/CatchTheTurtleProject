import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")

turtle_view = turtle.Turtle()
turtle_view.color("light blue")
turtle_view.shape("turtle")

turtle_view.penup()
turtle_view.speed(2)
count=0
while count<51:
    count+=1
    if (turtle_view.xcor()>-4000 and turtle_view.xcor()<4000) and \
            (turtle_view.ycor()>- 4000 and turtle_view.ycor()<4000):
        turtle_view.forward(random.randint(70,150))
        turtle_view.right(random.randint(0,360))




turtle.done()
