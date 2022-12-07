# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random
# Starting position
tim = t.Turtle()
tim.hideturtle()

tim.speed(0)
tim.penup()
tim.goto(-200, -200)
tim.pendown()
t.colormode(255)

# color list
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]


def move_forward():
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

for _ in range(10):
    for i in range(10):
        move_forward()

    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()



screen = t.Screen()
screen.exitonclick()
