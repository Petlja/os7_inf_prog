# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200)
prozor = pygamebg.open_window(sirina, visina, "Boja pozadine")

# -*- acsection: main -*-

def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def crtaj():
    boja = nasumicna_boja()  # nasumično određujemo boju pozadine
    prozor.fill(boja)        # bojimo pozadinu prozora
    
# -*- acsection: after-main -*-

# pokrećemo animaciju tako što funkciju crtaj pozivamo 4 puta u sekundi
pygamebg.frame_loop(4, crtaj)
