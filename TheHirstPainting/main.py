# import colorgram
# rgb_colors=[]
# colors=colorgram.extract("Hirst.jpg",20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(235, 234, 231), (235, 229, 232), (230, 237, 232), (223, 232, 237), (235, 36, 108), (143, 28, 66), (238, 75, 36), (9, 146, 93), (223, 168, 48), (48, 190, 230), (184, 158, 48), (30, 126, 192), (126, 192, 81), (253, 223, 0), (83, 28, 90), (175, 44, 93), (243, 219, 54), (40, 171, 114), (208, 132, 166), (196, 61, 43)]
import random
import turtle as t
t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen=t.Screen()
screen.exitonclick()