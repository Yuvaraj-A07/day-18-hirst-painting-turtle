# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
# c = []
# for i in range(len(colors)):
#     first_color = colors[i]
#     r=first_color.rgb[0]
#     g = first_color.rgb[1]
#     b = first_color.rgb[2]
#     rgb = (r,g,b)
#     c.append(rgb)
#
# print(c)
import random
import turtle
from turtle import Turtle,Screen
color_list = [(253, 251, 243), (254, 247, 252), (240, 252, 246), (246, 249, 253), (242, 233, 55), (184, 14, 29), (219, 162, 67), (24, 147, 24), (240, 229, 5), (22, 213, 103), (30, 87, 176), (229, 50, 155), (29, 38, 151), (55, 15, 11), (94, 10, 31)]
t = Turtle()
turtle.colormode(255)
t.speed(1000)
for row in range(10):
    for col in range(10):
        t.color(random.choice(color_list))
        t.dot(20)
        if col != 9:
            t.up()
            t.fd(50)
            t.down()
        else:
            t.left(90)
            t.up()
            t.fd(50)
            t.down()
            t.left(90)
            t.up()
            t.fd(50*col)
            t.down()
            t.right(90)
            t.right(90)




s = Screen()
s.exitonclick()