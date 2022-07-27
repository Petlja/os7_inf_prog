# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Koncentricni krugovi")  # otvaramo prozor
(sirina, visina) = (225, 225)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# centar kruga je u centru prozora - obrati pažnju na tip podataka
centar = (sirina//2, visina//2)

# poluprečnik se menja od 10 do 100, sa korakom 10
for r in range(10, 101, 10):
    # crtamo krug
    pg.draw.circle(prozor, pg.Color("red"), centar, r, 5)


# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
