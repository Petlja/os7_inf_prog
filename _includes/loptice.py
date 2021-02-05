# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (800, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Sarene loptice")

# -*- acsection: main -*-

# boje koje cemo koristiti
CRVENA = (255, 0, 0)
ZELENA = (0, 255, 0)
PLAVA = (0, 0, 255)
ZUTA = (255, 255, 0)
BELA = (255, 255, 255)

prozor.fill(BELA)

# vertikalna sredina prozora
sredina = visina // 2

# lista boja koje se naizmenicno smenjuju
boje = [CRVENA, ZELENA, PLAVA, ZUTA]
# redni broj kruga
i = 0
# poluprecnik kruga
r = 10
# polozaj levog kraja kruga
x = 0
# dok god levi kraj kruga ne ispadne van prozora
while x <= sirina:
    # crtamo krug - boja je odredjena na osnovu rendog broja i
    pg.draw.circle(prozor, boje[i % len(boje)], (x + r, sredina), r)
    # izracunavamo polozaj levog kraja narednog kruga
    x += 2*r
    # povecavamo poluprecnik narednog kruga
    r += 10
    # azuriramo redni broj kruga
    i += 1

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
