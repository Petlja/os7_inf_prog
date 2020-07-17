# -*- acsection: general-init -*-
import random, math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Клупко")

# -*- acsection: main -*-

# funkcija nasumicno bira tacku sa kruga ciji je centar u (cx, cy),
# a poluprecnik je r
def nasumicnaTackaNaKrugu(cx, cy, r):
    # nasumicno biramo ugao u radijanima (izmedju 0 i 2*pi)
    ugao = 2 * math.pi * random.random()
    # izracunavamo koordinate tacke na osnovu ugla
    (x, y) = (cx + r * math.cos(ugao), cy + r * math.sin(ugao))
    return (x, y)

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# centar kruga je centar ekrana
(cx, cy) = (sirina / 2, visina / 2)
# poluprecnik kruga (precnik je 90% sirine ekrana)
r = 0.9 * (sirina / 2)

brojDuzi = 500
for i in range(brojDuzi):
    # temena duzi su dve nasumicno odabrane tacke na krugu
    (x1, y1) = nasumicnaTackaNaKrugu(cx, cy, r)
    (x2, y2) = nasumicnaTackaNaKrugu(cx, cy, r)
    # crtamo duz crnom bojom
    pg.draw.aaline(prozor, pg.Color("black"), (x1, y1), (x2, y2), 1)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
