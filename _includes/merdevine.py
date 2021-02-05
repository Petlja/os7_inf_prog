# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Merdevine")

# -*- acsection: main -*-

prozor.fill(pg.Color("beige")) # bojimo pozadinu ekrana u bež

pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)    # leva strana
pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)    # desna strana

for y in range(50, 251, 50):
    pg.draw.line(prozor, pg.Color("brown"), (100, y), (200, y), 10) # precaga

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
