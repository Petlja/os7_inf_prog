# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()                                # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Boja pozadine")  # otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

boje = ["red", "green", "blue"]  # boje koje ćemo postavljati
broj_boje = 0                    # pozicija tekuće boje

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    prozor.fill(pg.Color(boje[broj_boje]))   # postavljanje boje pozadine na tekući element liste
    broj_boje = (broj_boje + 1) % len(boje)  # prelazimo na narednu boju
    pg.display.update()

    for dogadjaj in pg.event.get():          # proveravamo da li je korisnik isključio prozor
        if dogadjaj.type == pg.QUIT:
            kraj = True

    sat.tick(2)                              # pauziramo do sledeceg frejma

# -*- acsection: after-main -*-

pg.quit() # isključujemo rad biblioteke PyGame
