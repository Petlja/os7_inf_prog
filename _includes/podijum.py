# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Podijum za igru")

# -*- acsection: main -*-

def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# broj kvadrata
broj_kvadrata = 8
# dimenzija kvadrata
a = sirina / broj_kvadrata

# prolazimo kroz sva polja
for i in range(broj_kvadrata):
    for j in range(broj_kvadrata):
        pg.draw.rect(prozor, nasumicna_boja(), (i*a, j*a, a, a))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
