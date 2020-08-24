# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Боја позадине")

# -*- acsection: main -*-

boje = ["red", "green", "blue"]  # boje koje ćemo postavljati
broj_boje = 0                    # pozicija tekuće boje

def crtaj():
    global broj_boje                         # ova promenljiva se menja u funkciji
    prozor.fill(pg.Color(boje[broj_boje]))   # postavljanje boje pozadine na tekući element liste
    broj_boje = (broj_boje + 1) % len(boje)  # prelazimo na narednu boju
    
# -*- acsection: after-main -*-

# pokrećemo animaciju tako što se funkcija crtaj poziva dva puta u sekundi
pygamebg.frame_loop(2, crtaj)
