# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 50) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Prelaz boja")

# -*- acsection: main -*-

def nasumicna_boja():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

broj_nijansi = 10
sirina_polja = sirina / broj_nijansi
visina_polja = visina
(r1, b1, g1) = nasumicna_boja()
(r2, b2, g2) = nasumicna_boja()
for i in range(0, broj_nijansi):
    r = round(r1 + i*(r2 - r1)/broj_nijansi)
    g = round(g1 + i*(g2 - g1)/broj_nijansi)
    b = round(b1 + i*(b2 - b1)/broj_nijansi)
    pg.draw.rect(prozor, [r, g, b], (i*sirina_polja, 0, sirina_polja, visina_polja))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
