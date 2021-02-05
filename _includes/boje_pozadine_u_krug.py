# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Boja pozadine")

# -*- acsection: main -*-

boje = ["red", "green", "blue"]  # boje koje ćemo postavljati
broj_boje = 0                    # pozicija tekuće boje

def crtaj():
    prozor.fill(pg.Color(boje[broj_boje]))  # postavljanje boje pozadine na tekući element liste

def novi_frejm():
    global broj_boje # menjaćemo ovu globalnu promenljivu
    broj_boje = (broj_boje + 1) % len(boje)  # prelazimo na narednu boju
    crtaj() # ponovo iscrtavamo prozor

# -*- acsection: after-main -*-

# pokrećemo animaciju tako što se funkcija novi_frejm poziva dva puta u sekundi
pygamebg.frame_loop(2, novi_frejm)
