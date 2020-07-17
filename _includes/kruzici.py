# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Мрежа кружића")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# Maksimalni poluprečnik kružića
r_max = 10
# rastojanje izmedju vrsta i kolona
d = 2 * r_max

# indeksi kolona
for i in range(sirina//d):
    # indeksi vrsta
    for j in range(visina//d):
        # centar kruga u koloni i, vrsti j
        (cx, cy) = (r_max + i*d, r_max + j*d)
        # nasumično određujemo poluprečnik kruga (maksimalni poluprečnik je r_max)
        r = random.randint(2, r_max)
        # nasumično određujemo nijansu sive boje
        b = random.randint(0, 255)
        boja = [b, b, b]
        # crtamo krug
        pg.draw.circle(prozor, boja, (cx, cy), r)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
