from math import *

class Param_equations:
    #r_great - R promień większego okręgu,
    #r - promień mniejszego,
    #pc - odległość między 'dlugopisem' a środkiem mniejszego okręgu
    #a - alfa

    def __init__(self, x, y, alpha):           #    def __init__(self, fruit, color):
        self.x = x                                         #self.fruit = fruit
        self.y = y                                         #self.color = color
        self.alpha = alpha

    k = r/r_great
    l = pc/r

     def hipotro(r_great, r, pc, alpha);
       #HIPOTROCHOIDA:
    x = r_great* ((1 - k)* sin(alpha) + l* k* cos(alpha* (1-k)/k)

    def epitro(r_great, r, pc, alpha):
       #EPITROCHOIDA:
    y = r_great* ((1 - k)* cos(alpha) + l* k* sin(alpha* (1-k)/k)
    
