# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Broj pi")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# ukupan broj tačaka
n = 10000
# broj tačaka koje pripadaju jediničnom krugu
broj_tacaka_u_krugu = 0
for i in range(n):
    # nasumično biramo tačku iz jediničnog kvadrata
    x = random.random()
    y = random.random()
    # brojimo tačke koje pripadaju jediničnom krugu
    if x**2 + y**2 <= 1:
        broj_tacaka_u_krugu += 1
    # postavljamo boju u zavisnosti od toga da li je tačka unutar
    # jediničnog kruga
    if x**2 + y**2 <= 1:
        boja = pg.Color("black")
    else:
        boja = pg.Color("red")
    # iscrtavamo tacku
    pg.draw.circle(prozor, boja, (round(x*sirina), visina - round(y*visina)), 2)
# procenu broja pi vrsimo na osnovu odnosa broja tacaka u jediničnom
# krugu i ukupnog broja tacaka
pi = 4 * broj_tacaka_u_krugu / n

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
