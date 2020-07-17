# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Ротиране дужи")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))

# broj podeoka
n = 10
# priraštaj
dx = sirina / n
dy = visina / n

# crtamo n linija u donjem levom uglu prozora
for i in range(1, n):
    pg.draw.line(prozor, pg.Color("black"), (0, i*dy), (i*dx, visina), 1)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
