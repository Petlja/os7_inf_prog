# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Ротиране дужи")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))

# broj podeoka
n = 10
# prirastaj
dx = sirina / n
dy = visina / n

# Crtamo n linija u donjem levom uglu prozora
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (0, i*dy), (i*dx, visina), 1)

# Crtamo n linija u gornjem desnom uglu prozora
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (i*dx, 0), (sirina, i*dy), 1)

# Crtamo n linija u gornjem levom uglu
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (i*dx, 0), (0, visina-i*dy), 1)

# Crtamo n linija u donjem desnom uglu
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (i*dx, visina), (sirina, visina-i*dy), 1)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
