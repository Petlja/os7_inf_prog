# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(visina, sirina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(visina, sirina, "Боја мишем")

# -*- acsection: main -*-

crvena = 0  # količina crvene boje
plava = 0   # količina plave boje

def crtaj():
    prozor.fill((crvena, 0, plava))      # bojimo prozor

def obradi_dogadjaj(dogadjaj):
    global crvena, plava, treba_crtati

    if dogadjaj.type == pg.MOUSEMOTION:
        (x, y) = dogadjaj.pos  # koordinate na kojima se miš trenutno nalazi
        crvena = round(x / sirina * 255)  # količina crvene boje zavisi od x
        plava  = round (y / visina * 255) # količina plave boje zavisi od y
        return True # treba crtati ponovo

    return False # ne treba crtati ponovo

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)
