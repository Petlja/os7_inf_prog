# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Cigle")

# -*- acsection: main -*-

prozor.fill(pg.Color("red"))
(sirina_cigle, visina_cigle) = (80, 40)
x_pocetak = 0
for y0 in range(0, visina, visina_cigle):
    for x0 in range(x_pocetak, sirina, sirina_cigle):
        pg.draw.rect(prozor, pg.Color("black"), (x0, y0, sirina_cigle, visina_cigle), 1)
    if x_pocetak == 0:
        x_pocetak = -sirina_cigle//2
    else:
        x_pocetak = 0

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
