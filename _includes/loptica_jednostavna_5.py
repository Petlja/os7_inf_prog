# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Loptica")

# -*- acsection: main -*-

x = 0  # pozicija loptice
y = visina // 2
r = 30 # poluprečnik loptice
v = 1  # brzina loptice

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (x, y), r)

def novi_frejm():
    global x, y, r, v
    x += v    # pomeramo lopticu za jedan piksel nadesno
    if x - r > sirina:
        r = random.randint(5, 30)
        x = -r
        y = random.randint(r, visina - r)
        v = random.randint(1, 5)
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 100 puta u sekundi
pygamebg.frame_loop(100, novi_frejm)
