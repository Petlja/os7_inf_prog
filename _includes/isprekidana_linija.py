# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Isprekidana linija")

# -*- acsection: main -*-

# funkcija koja gradi nasumicno odabranu boju
def nasumicnaBoja():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# duzina jednog podeoka je 30 piksela
podeok = 30

# sredina prozora
sredina = visina / 2

# dok god levi kraj linije ne ispadne van prozora
x = 0
while x < sirina:
    # crtamo linijicu
    pg.draw.line(prozor, nasumicnaBoja(), (x, sredina), (x+podeok, sredina), 5)
    # pomeramo se za duzinu linije i duzinu razmaka
    x += 2 * podeok

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
