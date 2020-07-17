# -*- acsection: general-init -*-
import random
import pygame as pg

import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Степенице")

# -*- acsection: main -*-

# funkcija koja gradi nasumicno odabranu boju
def nasumicnaBoja():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

prozor.fill(pg.Color("white"))

brojStepenika = 10

sirinaStepenika = sirina / brojStepenika
visinaStepenika = visina / brojStepenika

for i in range(brojStepenika):
    pg.draw.rect(prozor, nasumicnaBoja(), (i * sirinaStepenika, visina - i*visinaStepenika, sirinaStepenika, i*visinaStepenika))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
