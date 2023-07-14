import subprocess
import turtle
import random
import subprocess
import time



drawing_board = turtle.Screen()
drawing_board.bgpic("Output (1).gif")
def update_timer():
    global timer
    timer += 1
    turtle.clear()
    turtle.write(f"{timer} s", align="center", font=("Arial", 18, "italic"))
    turtle.ontimer(update_timer, 1000)

timer=0

turtle.penup()
turtle.hideturtle()
turtle.color("orange")
turtle.goto(-497,269)
turtle.write("", align="center", font=("Arial", 18, "italic"))

turtle.ontimer(update_timer, 1000)

title_view = turtle.Turtle()
title_view.hideturtle()
title_view.penup()
title_view.setx(-560)
title_view.sety(300)
title_view.color("orange")
style = ("Arial", 18, "italic")
title_view.write("Your score:  ", font=style, align="center")
title_view.hideturtle()


title_view2 = turtle.Turtle()
title_view2.hideturtle()
title_view2.penup()
title_view2.setx(-570)
title_view2.sety(270)
title_view2.color("orange")
style = ("Arial", 18, "italic")
title_view2.write("Your time: ", font=style, align="center")
title_view2.hideturtle()

turtle_view = turtle.Turtle()
turtle_view.color("red")
turtle_view.shape("turtle")
turtle_view.turtlesize(1.50, 1.25, 2)
turtle_view.penup()
turtle_view.speed(2.5)

score_view = turtle.Turtle()
score_view.color("orange")
score_view.hideturtle()
score_view.penup()
score_view.setx(-495)
score_view.sety(299)

puan = 0

def puan_artir(x, y):
    global puan
    puan += 1
    score_view.clear()
    score_view.write("{}".format(puan), font=style, align="center")

turtle_view.onclick(puan_artir)

def turtle_return_home():
    turtle_view.hideturtle()
    turtle_view.home()
    turtle_view.showturtle()


drawing_board.listen()
drawing_board.onkey(fun=turtle_return_home, key="h")


count = 0
while count < 51:
    count += 1
    if (turtle_view.xcor() > -4000 and turtle_view.xcor() < 4000) and \
            (turtle_view.ycor() > - 4000 and turtle_view.ycor() < 4000):
        turtle_view.hideturtle()
        turtle_view.forward(random.randint(70, 300))
        turtle_view.showturtle()
        turtle_view.right(random.randint(140, 360))

turtle.mainloop()
