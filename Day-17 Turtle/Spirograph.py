import turtle as t
import random

tim=t.Turtle()
tim.shape("turtle")

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color=(r,g,b)
    return r_color



for i in range(100):
    # tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+10)


screen=t.Screen()
screen.exitonclick()