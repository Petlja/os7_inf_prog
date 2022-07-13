# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kvadrat / Krug")

# -*- acsection: main -*-


# bojimo pozadinu prozora u zuto
prozor.fill(pg.Color("yellow"))

kvadrat = True

if kvadrat:
    pg.draw.rect(prozor, pg.Color("blue"), (100, 100, 100, 100), 3)
else:
    pg.draw.circle(prozor, pg.Color("blue"), (150, 150), 50, 3)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()