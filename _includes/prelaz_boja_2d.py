# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Прелаз боја")

# -*- acsection: main -*-

def nasumicna_boja():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

broj_nijansi = 10
sirina_polja = sirina / broj_nijansi
visina_polja = visina / broj_nijansi
(r1, b1, g1) = nasumicna_boja()
(r2, b2, g2) = nasumicna_boja()
(r3, b3, g3) = nasumicna_boja()
for i in range(0, broj_nijansi):
    for j in range(0, broj_nijansi):
        r = max(0, min(255, round(r1 + i*(r2 - r1)/(broj_nijansi - 1) + j*(r3-r1)/(broj_nijansi - 1))))
        g = max(0, min(255, round(g1 + i*(g2 - g1)/(broj_nijansi - 1) + j*(g3-g1)/(broj_nijansi - 1))))
        b = max(0, min(255, round(b1 + i*(b2 - b1)/(broj_nijansi - 1) + j*(b3-b1)/(broj_nijansi - 1))))
        pg.draw.rect(prozor, [r, g, b], (i*sirina_polja, j*visina_polja, sirina_polja, visina_polja))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
