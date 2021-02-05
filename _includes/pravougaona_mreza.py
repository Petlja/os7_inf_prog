# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pravougaona mreza")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

brojPodeoka = 10
dx = sirina / brojPodeoka
dy = visina / brojPodeoka

# crtamo horizontalne linije
for i in range(1, brojPodeoka):
    pg.draw.line(prozor, pg.Color("blue"), (0, i*dy), (sirina, i*dy), 5)

# crtamo vertikalne linije
for i in range(1, brojPodeoka):
    pg.draw.line(prozor, pg.Color("red"), (i*dx, 0), (i*dx, visina), 5)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
