# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (500, 100) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kvadrati - naizmenicno menjanje boja")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))
# -*- acsection: main -*-

# broj kvadrata koje treba iscrtati
broj_kvadrata = 10
# sirina i visina jednog kvadrata
dimenzija_kvadrata = sirina / broj_kvadrata
# vertikalna sredina ekrana
sredina = visina / 2

for i in range(0, broj_kvadrata):
    # boja zavisi od toga da li je redni broj kvadrata paran ili neparan
    if i % 2 == 0:
        boja = pg.Color("yellow")
    else:
        boja = pg.Color("green")
    # koordinate gornjeg levog temena
    (levo, gore) = (i * dimenzija_kvadrata, sredina - dimenzija_kvadrata / 2)
    # crtamo kvadrat
    pg.draw.rect(prozor, boja, (levo, gore, dimenzija_kvadrata, dimenzija_kvadrata))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
