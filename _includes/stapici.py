# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Stapici")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# broj stapica
broj_stapica = 20

# razmak izmedju dva stapica odredjujemo tako da stapici ravnomerno
# budu rasporedjeni sirinom celog prozora
razmak = round(sirina / (broj_stapica + 1))

# crtamo jedan po jedan stapic
for i in range(1, broj_stapica+1):
    # visina gorne i donje tacke stapica
    ymin = 0.1 * visina
    ymax = 0.9 * visina
    # horizontalni polozaj stapica, pre nego sto se pomeri
    x = i * razmak
    # gornje i donje teme stapica nasumicno pomeramo
    x1 = x + random.randint(-razmak, razmak)
    x2 = x + random.randint(-razmak, razmak)
    # crtamo stapic
    pg.draw.aaline(prozor, pg.Color("black"), (x1, ymin), (x2, ymax))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
