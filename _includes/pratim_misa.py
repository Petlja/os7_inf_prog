# -*- acsection: general-init -*-
import random, math
import pygame as pg
import pygamebg

(sirina, visina) = (250, 250)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Лоптица прати миша")

# -*- acsection: main -*-

# rastojanje između dve date tačke (zadate parovima koordinata)
def rastojanje(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

# pozicija loptice
(x, y) = (sirina // 2, visina // 2)

def crtaj():
    # crtamo zelenu lopticu na beloj pozadini
    prozor.fill(pg.Color("white")) 
    pg.draw.circle(prozor, pg.Color("green"), (round(x), round(y)), 10)

def novi_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # koordinate pozicije miša
    d = rastojanje((x, y), (xm, ym))  # rastojanje tačke od miša
    v = 2                             # brzina kretanja loptice
    if d < v:                         # ako je loptica dovoljno blizu miša pomera
        (x, y) = (xm, ym)             #    pomera se tačno na poziciju miša
    else:                             # u suprotnom
        x = x + v * (xm - x) / d      #    pomera se malo u smeru ka mišu
        y = y + v * (ym - y) / d

    # ponovo iscrtavamo scenu
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(50, novi_frejm)
