# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Балони")

# -*- acsection: main -*-

def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255),  random.randint(0, 255))

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("yellow"))

broj_balona = 5
sirina_polja = sirina / broj_balona
sirina_balona = 50
visina_balona = 70
for i in range(broj_balona):
    centar_polja = i*sirina_polja + sirina_polja / 2
    pg.draw.ellipse(prozor, nasumicna_boja(), (centar_polja - sirina_balona / 2, 0, sirina_balona, visina_balona))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
