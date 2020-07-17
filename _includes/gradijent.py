# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (512, 250) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Градијент")

# -*- acsection: main -*-

# bojimo pozadinu gradijentom
dx = sirina / 256
for i in range(0, 256):
    pg.draw.rect(prozor, [i, i, i], (i*dx, 0, dx, visina))

# crtamo jednobojni sivi pravougaonik u sredini
sx = round(0.75 * sirina)
sy = 50
pg.draw.rect(prozor, [128, 128, 128], ((sirina - sx) / 2, (visina - sy) / 2, sx, sy))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
