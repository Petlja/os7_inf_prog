# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Концентрични кругови")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))

# centar kruga je u centru prozora
centar = (sirina // 2, visina // 2)

# poluprecnik se menja od 10 do 100, sa korakom 10
for r in range(10, 101, 10):
    # crtamo krug
    pg.draw.circle(prozor, pg.Color("red"), centar, r, 5)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
