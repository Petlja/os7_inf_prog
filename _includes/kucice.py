# -*- acsection: general-init -*-
import math, random
import pygame as pg
import pygamebg

(sirina, visina) = (600, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Selo")

# -*- acsection: main -*-

# crta kućicu kojoj je donje levo teme u (x, y)
def kucica(x, y, dim_kucice):
    (x0, y0) = (x, y - dim_kucice)  # gornje levo teme osnove
    # crtamo osnovu kuće
    pg.draw.rect(prozor, pg.Color("white"), (x0, y0, dim_kucice, dim_kucice))
    # crtamo krov (jednakostranični trougao)
    krov_levo  = (x0, y0)                                                        # donje levo teme krova
    krov_desno = (x0+dim_kucice, y0)                                          # donje desno teme krova
    krov_vrh   = (x0 + dim_kucice/2, y0 - dim_kucice * math.sqrt(3) / 2)   # vrh krova
    pg.draw.polygon(prozor, pg.Color("red"), [krov_levo, krov_desno, krov_vrh])
    # uokvirujemo osnovu kuće
    pg.draw.rect(prozor, pg.Color("black"), (x0, y0, dim_kucice, dim_kucice), 1)
    # crtamo vrata
    sirina_vrata = dim_kucice / 4
    visina_vrata = dim_kucice / 2
    vrata_levo = x + (dim_kucice - sirina_vrata) / 2   # x koordinata leve ivice vrata
    vrata_gore = y - visina_vrata                         # y koordinata gornje ivice vraa
    pg.draw.rect(prozor, pg.Color("brown"), (vrata_levo, vrata_gore, sirina_vrata, visina_vrata))
    

# bojimo pozadinu u nebo-plavo
prozor.fill(pg.Color("skyblue"))

# crtamo jednu po jednu kućicu
broj_kucica = 5
dim_kucice = sirina / broj_kucica
for i in range(broj_kucica):
    kucica(i * dim_kucice, visina, dim_kucice)
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
