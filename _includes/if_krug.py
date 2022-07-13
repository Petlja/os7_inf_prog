# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pun Krug / Kruznica")

# -*- acsection: main -*-


# bojimo pozadinu prozora u zuto
prozor.fill(pg.Color("yellow"))

pun_krug = True

if pun_krug:
    pg.draw.circle(prozor, pg.Color("blue"), (150, 150), 50)
else:
    pg.draw.circle(prozor, pg.Color("blue"), (150, 150), 50, 3)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()