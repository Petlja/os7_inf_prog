# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (800, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Крешендо")

# -*- acsection: main -*-

# boje koje cemo koristiti
PLAVA = (100, 100, 255)
BELA = (255, 255, 255)

# bojimo pozadinu prozora u belo
prozor.fill(BELA)

# broj linija koje se crtaju
brojLinija = 100
# razmak izmedju linija
razmak = sirina / brojLinija
# razlika u visini izmedju susednih linija
prirastaj = visina / brojLinija
# vertikalna sredina prozora
sredina = visina / 2

# horizontalna pozicija tekuce linije
polozaj = 0
# duzina tekuce linije
duzina = 0
# crtamo jednu po jednu liniju
for i in range(brojLinija):
    # pola duzine se nalazi iznad, a pola duzine ispod sredine prozora
    pg.draw.line(prozor, PLAVA, (polozaj, sredina - duzina/2), (polozaj, sredina + duzina/2), 3)
    # povecavamo duzinu linije
    duzina += prirastaj
    # pomeramo se horizontalno udesno
    polozaj += razmak

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
