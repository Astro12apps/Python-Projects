from turtle import Turtle,Screen

tim=Turtle()
screen =Screen()



def forwards():
    tim.forward(50)
def backwards():
    tim.backward(50)
def counter_clockwise():
    tim.left(10)
    tim.forward(50)
def clockwise():
    tim.right(10)
    tim.forward(50)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forwards,"w")
screen.onkey(backwards,"s")
screen.onkey(counter_clockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(clear,"c")
screen.exitonclick()