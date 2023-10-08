import turtle

import colorgram
import random
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)


color_list = [(234, 229, 226), (241, 237, 238), (211, 148, 111), (216, 223, 233), (218, 229, 222), (135, 159, 189)]

end_paint = False

row_count = 0
position = [-275, -200]


def for_moves():
    dot_count = 0
    for t in range(10):
        # tim.pencolor(41, 41, 253)
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20)
        dot_count += 1
        if dot_count == 10:
            position[1] = position[1] + 40


# def moves():
#     global dot_count
#     global row_count
#
#     if dot_count < 11:
#         # tim.color("40", "80", "120")
#         tim.dot(20)
#         tim.penup()
#         tim.forward(50)
#         tim.pendown()
#         tim.dot(20)
#         dot_count += 1
#         row_count += 1
#     else:
#         # area_position()
#         dot_count = 0
#         row_count += 1
#         global end_paint
#         end_paint = True


for _ in range(10):
    tim.penup()
    tim.setpos(position[0], position[1])
    for_moves()


# while not end_paint:
#     # area_position()
#     tim.penup()
#     if row_count == 0:
#         tim.setpos(-275, -200)
#     moves()

myScreen = Screen()
myScreen.exitonclick()

# Previous code to extract the colors from the image

# colors = colorgram.extract("images.jpg", 6)
# print(colors)
# print(len(colors))

# count = 0

# rgb_list = []

# for i in colors:
#     colour = colors[count]
#     rgb = colour.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     final_rgb = (red, green, blue)
#     rgb_list.append(final_rgb)
#     count += 1

# print(rgb_list)

# Alternate way of coding with definition

# def get_rgb():
#     global count
#     colours = colors[count]
#     rgb = colours.rgb
#     # print(rgb)
#     count += 1
#     # print(count)
#     return rgb


# for t in range(len(colors)):
#     get_rgb()
#     rgb_list.append(get_rgb())
#     print(rgb_list)





