# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Круг три четвртине прозора")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
# centar kruga je u centru ekrana
(cx, cy) = (sirina / 2, visina / 2)
# izracunavamo poluprečnik kruga
r = math.sqrt(0.75 * visina * sirina / math.pi)
# crtamo krug
pg.draw.circle(prozor, pg.Color("purple"), (round(cx), round(cy)), round(r))

# -*- acsection: after-main -*-

# osvežavamo prikaz sadžaja prozora
pg.display.update()

# čekamo dok korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
