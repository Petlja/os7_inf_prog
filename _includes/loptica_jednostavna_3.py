# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Лоптица")

# -*- acsection: main -*-

x = 0  # pozicija loptice
r = 30 # poluprečnik loptice

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (x, visina // 2), r)

def novi_frejm():
    global x, r
    x += 1    # pomeramo lopticu za jedan piksel nadesno
    if x - r > sirina:
        r = random.randint(5, 30)
        x = -r
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 100 puta u sekundi
pygamebg.frame_loop(100, novi_frejm)
