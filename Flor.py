from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216')
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40,24)

# Draw flower center
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup()
    goto(x, y)
    setheading(i*golden_ang)
    pendown()
    stamp()

# Define points to draw letters
def point(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('black')
    begin_fill()
    circle(4)
    end_fill()

# Function to draw 'D'
def draw_D(x, y):
    positions_d = [(x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30), 
                   (x+6, y+30), (x+12, y+30), (x+18, y+24), (x+18, y+18), (x+18, y+12), 
                   (x+18, y+6), (x+12, y), (x+6, y)]
    for pos in positions_d:
        point(*pos)

# Function to draw 'A'
def draw_A(x, y):
    positions_a = [(x, y), (x+3, y+6), (x+6, y+12), (x+9, y+18), (x+12, y+24), (x+15, y+30),
                   (x+18, y+24), (x+21, y+18), (x+24, y+12), (x+27, y+6), (x+30, y),
                   (x+9, y+18), (x+15, y+18), (x+21, y+18)]
    for pos in positions_a:
        point(*pos)

# Function to draw 'I'
def draw_I(x, y):
    positions_i = [(x, y), (x+6, y), (x+12, y), (x+6, y+6), (x+6, y+12), (x+6, y+18), 
                   (x+6, y+24), (x+6, y+30), (x, y+30), (x+6, y+30), (x+12, y+30)]
    for pos in positions_i:
        point(*pos)

# Function to draw 'S'
def draw_S(x, y):
    positions_s = [(x, y+30), (x+6, y+30), (x+12, y+24), (x+12, y+18), (x+6, y+12), 
                   (x, y+12), (x, y+6), (x+6, y), (x+12, y)]
    for pos in positions_s:
        point(*pos)

# Function to draw 'Y'
def draw_Y(x, y):
    positions_y = [(x, y+30), (x+6, y+24), (x+12, y+18), (x+18, y+24), (x+24, y+30), 
                   (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y)]
    for pos in positions_y:
        point(*pos)

# Draw 'DAISY' with more spacing
draw_D(-80, -20)
draw_A(-40, -20)
draw_I(0, -20)
draw_S(40, -20)
draw_Y(80, -20)

hideturtle()
done()
