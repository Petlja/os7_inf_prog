# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Испрекидана линија црта-тачка")

# -*- acsection: main -*-

# funkcija koja gradi nasumicno odabranu boju
def nasumicnaBoja():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# duzina jednog podeoka
kratka_linija = 10
duga_linija = 30
razmak = 10

# sredina prozora
sredina = visina / 2

# da li se crta duga ili kratka linija
duga = True
# koordinata pocetka linije
x = 0
# dok god linija pocinje unutar prozora
while x < sirina:
    # odredjujemo duzinu linije
    d = duga_linija if duga else kratka_linija
    # crtamo liniju
    pg.draw.line(prozor, pg.Color("green"), (x, sredina), (x+d, sredina), 5)
    # pocetak naredne linije
    x += d + razmak
    # naredna linija menja duzinu u odnosu na tekucu
    duga = not duga

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
