# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Oblaci")

# -*- acsection: main -*-

# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 100), 80)

# procedura koja crta oblak na datoj poziciji, date velicine u datoj
# nijansi sive boje
def oblak(x, y, r, siva):
    # crtamo oblak od tri kruga
    boja = (siva, siva, siva)
    pg.draw.circle(prozor, boja, (x, y), r)
    r_malo = round(5 * r / 8)
    pg.draw.circle(prozor, boja, (x - r, y), r_malo)
    pg.draw.circle(prozor, boja, (x + r, y), r_malo)

oblak(240, 200, 40, 180)
oblak(270, 250, 50, 210)
oblak(230, 100, 50, 230)
oblak(80, 80, 30, 150)
oblak(110, 320, 60, 255)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
