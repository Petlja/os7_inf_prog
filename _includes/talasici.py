# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Talasici")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# broj talasica koji ce se nacrtati
brojTalasica = 10

# poluprecnik talasica
r = sirina / brojTalasica / 2

# sredina prozora po vertikali
sredina = visina / 2

# da li talasic ide na gore ili na dole
gore = True
for i in range(brojTalasica):
    if gore:
        (odUgao, doUgao) = (0, math.pi)
    else:
        (odUgao, doUgao) = (math.pi, 0)
    pg.draw.arc(prozor, pg.Color("blue"), (2 * i * r, sredina, 2*r, 2*r), odUgao, doUgao, 3)
    # naredni talasic ide u suprotnu stranu
    gore = not gore

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
