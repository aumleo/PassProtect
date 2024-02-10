import colorgram as c
import turtle as tur
import random as ran

'''Only need to execute this once to get all the req colors'''
# colors = c.extract("vvg.jpg",40)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new= (r, g, b)
#     rgb_colors.append(new)
# print(rgb_colors)

tur.colormode(255)
tim = tur.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list=[(52, 41, 14), (125, 88, 38), (16, 28, 13), (87, 69, 27), (184, 161, 107), (170, 134, 62), (83, 106, 118), (80, 96, 87), (145, 163, 150), (122, 146, 158), (217, 196, 148), (108, 52, 23), (17, 23, 27), (56, 71, 52), (226, 202, 163), (109, 134, 142), (117, 135, 125), (12, 6, 9), (104, 130, 155), (200, 107, 61), (52, 68, 72), (51, 64, 78), (128, 126, 127), (159, 150, 151), (190, 198, 183), (195, 203, 188)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, ran.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = tur.Screen()
screen.exitonclick()