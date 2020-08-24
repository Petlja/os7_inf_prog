# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Диоде")

# -*- acsection: main -*-

broj_dioda = 10                     # ukupan broj dioda na displeju
ukljucena = 0                       # redni broj trenutno uključene diode
r = sirina // (2 * broj_dioda)      # poluprečnik jedne diode

def crtaj():
    prozor.fill(pg.Color("black"))                         # bojimo pozadinu u crno
    (x, y) = (r + ukljucena * 2 * r, visina // 2)          # izračunavamo položaj centra diode
    pg.draw.circle(prozor, pg.Color("white"), (x, y), r)   # crtamo diodu belom bojom

def novi_frejm():
    global ukljucena
    ukljucena = (ukljucena + 1) % broj_dioda               # prelazimo na narednu diodu
    crtaj()

# -*- acsection: after-main -*-

# tokom animacije se funkcija novi_frejm poziva 5 puta u sekundi
pygamebg.frame_loop(5, novi_frejm)
