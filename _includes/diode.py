# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 100) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Diode")

# -*- acsection: main -*-

broj_dioda = 20                     # ukupan broj dioda na displeju
ukljucena = 0                       # redni broj trenutno uključene diode
r = sirina // (2 * broj_dioda)      # poluprečnik jedne diode
r = sirina // (2 * broj_dioda)

def crtaj():
    prozor.fill(pg.Color("black"))                         # bojimo pozadinu u crno
    kasnjenje = 10                                         # broj dioda koje se još nisu isključile
    for i in range(-kasnjenje, 1):                         # za sve brojeve -kasnjenje, -kasnjenje+1, ..., -1, 0
        dioda = (ukljucena + broj_dioda + i) % broj_dioda  # redni broj diode koja je uključena i koraka pre tekuće
        nijansa = (255 / kasnjenje) * i + 255              # nijansu sive boje određujemo tako da je dioda na mestu -kasnjenje crna, a na mestu 0 bela
        boja = (nijansa, nijansa, nijansa)
        (x, y) = (r + dioda * 2 * r, visina // 2)          # određujemo poziciju diode
        pg.draw.circle(prozor, boja, (x, y), r)            # crtamo diodu

def novi_frejm():
    global ukljucena
    ukljucena = (ukljucena + 1) % broj_dioda               # prelazimo na narednu diodu
    crtaj()

# -*- acsection: after-main -*-

# tokom animacije se funkcija novi_frejm poziva 5 puta u sekundi
pygamebg.frame_loop(25, novi_frejm)
