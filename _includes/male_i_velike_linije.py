# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Свеска са малим и великим линијама")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))

veliki_razmak = 30
mali_razmak = 20

y = veliki_razmak
mali = True
while y <= visina:
    pg.draw.line(prozor, pg.Color("black"), (0, y), (sirina, y))
    if mali:
        y += mali_razmak
    else:
        y += veliki_razmak
    mali = not(mali)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
