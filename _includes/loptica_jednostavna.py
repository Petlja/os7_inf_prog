# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100)   # otvaramo prozor
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
    crtaj()

# -*- acsection: after-main -*-

# pokrecemo animaciju tako što funkciju novi_frejm pozivamo 50 puta u sekundi
pygamebg.frame_loop(50, novi_frejm)
