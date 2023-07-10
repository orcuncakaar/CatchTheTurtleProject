import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")

turtle_view = turtle.Turtle()
turtle_view.color("light blue")
turtle_view.shape("turtle")

turtle_view.penup()
turtle_view.speed(2)
count = 0
while count < 51:
    count += 1
    if (turtle_view.xcor() > -4000 and turtle_view.xcor() < 4000) and \
            (turtle_view.ycor() > - 4000 and turtle_view.ycor() < 4000):
        turtle_view.hideturtle()
        turtle_view.forward(random.randint(70, 300))
        turtle_view.showturtle()
        turtle_view.right(random.randint(140, 360))


def turtle_return_home():
    turtle_view.home()


drawing_board.onkey(fun=turtle_return_home, key="h")

turtle.mainloop()
