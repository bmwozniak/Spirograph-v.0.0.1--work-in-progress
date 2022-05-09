import math
import turtle
import tkinter

import Param_equations as peq

def draw_circle(x, y, r): #x,y środek okręgu
    turtle.up()  #podnieś pióro
    turtle.setpos(x + r, y)  #ustaw żółwia 
    turtle.down()  #opuść pióro

    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r* math.cos(a), y + r* math.sin(a))

draw_circle(100, 100, 50)
turtle.mainloop()

class Spiro:
    def __init__(self, xc, yc, col, r_great, r, l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawing_complete = False

        self.setparams(xc, yc, col, r_great, r, l)

        self.restart()

    def set_params(self, xc, yc, col, r_great, r, l):
        self.xc = xc
        self.yc = yc
        self.r_great = r_great
        self.r = r
        self.l = l
        self.col = col

        gcdVal = gcd(self.r, self.r_great)
        self.nRot = self.r/gcdVal

        self.k = r/float(r_great)

        self.color(*col)

        self.a = 0











        
