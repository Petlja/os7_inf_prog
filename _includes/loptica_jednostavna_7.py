# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Loptica")

# -*- acsection: main -*-

x = sirina // 2  # pozicija loptice
y = visina // 2
r = 30 # poluprečnik loptice
v = 1  # brzina loptice
boja = pg.Color("red") # boja loptice

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, boja, (x, y), r)

def novi_frejm():
    global x, y, r, v, boja
    x -= v    # pomeramo lopticu za jedan piksel nadesno
    if x + r < 0:
        r = random.randint(5, 30)
        x = sirina + r
        y = random.randint(r, visina - r)
        v = random.randint(1, 5)
        boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 100 puta u sekundi
pygamebg.frame_loop(100, novi_frejm)
