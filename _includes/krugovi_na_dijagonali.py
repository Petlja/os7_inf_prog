# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (500, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Кругови на дијагонали")

# -*- acsection: main -*-

# broj krugova
n = 10
# duzina dijagonale
d = round(math.sqrt(sirina**2 + visina**2))
# poluprecnik krugova
r = round(d / (2 * n))
# razmak izmedju centara krugova po x i y osi
kx = round((r*sirina) / d)
ky = round((r*visina) / d)

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
# crtamo krugove
for i in range(n):
    pg.draw.circle(prozor, pg.Color("red"), ((2*i+1)*kx, (2*i+1)*ky), r, 3)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
