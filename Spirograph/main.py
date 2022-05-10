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
        turtle.setpos(x + r* math.cos(alpha), y + r* math.sin(alpha))

draw_circle(100, 100, 50)
turtle.mainloop()

class Spiro:
    def __init__(self, x_centre, y_centre, colour, r_great, r, l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawing_complete = False

        self.setparams(x_centre, y_centre, colour, r_great, r, l)

        self.restart()

    def set_params(self, x_centre, y_centre, colour, r_great, r, l):
        self.x_centre= x_centre
        self.y_centre = y_centre
        self.r_great = int(r_great)
        self.r = int(r)
        self.l = l
        self.colour = colour

        gcdVal= gcd(self.r, self.r_great) #najwiekszy wspolny dzielnik
        self.nRot = self.r//gcdVal

        self.k = r/float(r_great)

        self.colour(*colour)

        self.alpha = 0











        
