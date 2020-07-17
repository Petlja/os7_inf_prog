# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Згуснуте линије")

# -*- acsection: main -*-

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("black"))

# y koordinate krajeva linija
y1 = 50
y2 = visina - 50
# tekuća koordinata x
x = 50
# tekući razmak između dve linije
dx = 20
# 10 puta ponavljamo
for i in range(10):
    # crtamo tekuću liniju
    pg.draw.line(prozor, pg.Color("white"), (x, y1), (x, y2), 2);
    # izračunavamo položaj sledeće na osnovu tekućeg razmaka
    x += dx
    # uvećavamo razmak za 10 posto
    dx *= 1.1

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
