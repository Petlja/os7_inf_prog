# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Slaliranje kvadrata")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))
# crtamo kvadrat u centru prozora
pg.draw.rect(prozor, pg.Color("red"), (100, 100, 100, 100), 5)

# -*- acsection: after-main -*-

pygamebg.wait_loop()
