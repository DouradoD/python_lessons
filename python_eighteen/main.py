import random
import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
turtle.colormode(255)

my_turtle.shape("turtle")
my_turtle.color("blue")

your_turtle = Turtle()
your_turtle.shape("turtle")
your_turtle.color("red")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

'''
for _ in range(4):
    your_turtle.forward(100)
    my_turtle.forward(100)
    my_turtle.left(90)
    your_turtle.left(90)
    
distance = 0
while distance < 50000:
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    distance += 10
    
sides = 3
while sides < 15:
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.left(360/sides)
    sides += 1
'''
print(random_color())
my_turtle.speed('fastest')
my_turtle.circle(100)
my_turtle.setheading(my_turtle.heading() + 10)
while my_turtle.heading() != 0.0:
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + 10)


screen = turtle.Screen()
screen.exitonclick()
