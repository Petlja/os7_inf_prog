# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (500, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Suma")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# boje koje cemo koristiti
CRNA  = (0, 0, 0)
ZELENA = (0, 100, 36)
BRAON = (97, 26, 9)

def jelka(x, y):
    # stablo
    pg.draw.rect(prozor, BRAON, (x-10, y-25, 20, 25))
    # krošnja
    pg.draw.polygon(prozor, ZELENA, [(x-50, y-25), (x+50, y-25), (x, y-75)])
    pg.draw.polygon(prozor, ZELENA, [(x-37, y-50), (x+37, y-50), (x, y-100)])
    pg.draw.polygon(prozor, ZELENA, [(x-25, y-75), (x+25, y-75), (x, y-125)])

for x in range(50, sirina, 100):
    jelka(x, visina)
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
