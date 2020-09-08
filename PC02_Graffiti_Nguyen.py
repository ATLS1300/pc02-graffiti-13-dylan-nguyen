#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:39:26 2020

@author: dylannguyen
"""

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)
Turtle()
forward(350)
left(90)
forward(200)
circle(45)
left(180)
forward(400)
pensize(10)
shape("triangle")
right(90)
forward(650)
right(90)
forward(200)
right(90)
goto(0,0)
forward(70)
left(90)
forward(230)
left(90)
forward(180)
right(90)
backward(230)
right(180)
forward(100)
pensize(3)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(135)
forward(120)
right(90)
forward(70)
right(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)