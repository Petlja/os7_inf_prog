# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 200)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Две лоптице")

# -*- acsection: main -*-

r = 20
(x1, y1) = (r, r)
(dx1, dy1) = (1, 1)
(x2, y2) = (sirina - r, visina - r)
(dx2, dy2) = (-1, -1)

def crtaj():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (x1, y1), r)
    pg.draw.circle(prozor, pg.Color("blue"), (x2, y2), r)

# rastojanje između centara loptica
def rastojanje():
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# provera da li se dve loptice sudaraju
def sudar():
    return rastojanje() <= 2*r

def novi_frejm():
    global x1, y1, x2, y2, dx1, dy1, dx2, dy2

    # pomeramo prvu lopticu i proveravamo sudar sa ivicama prozora
    x1 += dx1
    y1 += dy1
    if x1 - r < 0 or x1 + r > sirina:
        dx1 = -dx1
    if y1 - r < 0 or y1 + r > visina:
        dy1 = -dy1

    # pomeramo drugu lopticu i proveravamo sudar sa ivicama prozora
    x2 += dx2
    y2 += dy2
    if x2 - r < 0 or x2 + r > sirina:
        dx2 = -dx2
    if y2 - r < 0 or y2 + r > visina:
        dy2 = -dy2

    # ispitujemo sudar dve loptice
    if sudar():
        (dx1, dy1, dx2, dy2) = (dx2, dy2, dx1, dy1)

    # crtamo ponovo scenu
    crtaj()


# -*- acsection: after-main -*-

pygamebg.frame_loop(100, novi_frejm)
