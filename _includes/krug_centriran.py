# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Koncentricni krugovi")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))
# centar kruga je u centru prozora
centar = (sirina // 2, visina // 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 30, 5)

# -*- acsection: after-main -*-

pygamebg.wait_loop()
