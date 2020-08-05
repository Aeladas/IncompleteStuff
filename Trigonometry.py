import tkinter
import random
import math
import turtle

_size = 40
_font = ("OCR A extended", _size, "normal")

def draw_diagram():
    turtle.width(3)
    turtle.color("#000000")
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(425)
    #Write side A
    turtle.penup()
    turtle.goto(150, -50)
    turtle.write("A", font=_font)
    #Write side B
    turtle.goto(325, 125)
    turtle.write("B", font=_font)
    #Write side C
    turtle.goto(75, 125)
    turtle.write("C", font=_font)
