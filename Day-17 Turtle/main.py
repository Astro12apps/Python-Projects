
import turtle as t
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
t.colormode(255)
#
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for _ in range(3,11):
#     draw_shape(_)

directions=[0,90,180,270]
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour=(r,g,b)
    return random_colour
import random
for _ in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
