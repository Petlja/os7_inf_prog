# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 100)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Лоптица")

# -*- acsection: main -*-

x = 0  # pozicija loptice

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (x, visina // 2), 30)

def novi_frejm():
    global x
    x += 1    # pomeramo lopticu za jedan piksel nadesno
    if x > 300:
        x = 0
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 100 puta u sekundi
pygamebg.frame_loop(100, novi_frejm)
