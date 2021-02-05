# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Margine")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# crtamo sadržaj stranice
procenat_margine = 0.1
pocetak_sadrzaja_x = procenat_margine * sirina
pocetak_sadrzaja_y = procenat_margine * visina
sirina_sadrzaja = (1 - 2*procenat_margine) * sirina
visina_sadrzaja = (1 - 2*procenat_margine) * visina
pg.draw.rect(prozor, pg.Color("blue"), (pocetak_sadrzaja_x, pocetak_sadrzaja_y, sirina_sadrzaja, visina_sadrzaja))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
