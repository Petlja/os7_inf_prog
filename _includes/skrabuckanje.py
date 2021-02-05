# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Skrabuckanje")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

korak_x = 3
korak_y = 15
greska_y = 5

# ostavljamo mali prostor na vrhu ekrana
y = greska_y
# dok linija ne moze da udari u dno prozora
while y + greska_y < visina:
    # krecemo od leve ivice ekrana
    x = 0
    # pamtimo koordinate prethodne tacke
    (prethodno_x, prethodno_y) = (x, y)
    # dok tekuca tacka ne dostigne desnu ivicu prozora
    while x < sirina:
        # nasumicna vrednost u intervalu [-greska_y, greska_y]
        dy = random.random() * 2 * greska_y - greska_y
        # crtamo liniju od prethodne do tekuce tacke
        pg.draw.line(prozor, pg.Color("black"), (prethodno_x, prethodno_y), (x, y + dy))
        # tekuca tacka postaje prethodna za narednu iteraciju
        (prethodno_x, prethodno_y) = (x, y + dy)
        # pomeramo se nadesno
        x += korak_x
    # prelazimo na sledeci horizontalni red
    y += korak_y

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
