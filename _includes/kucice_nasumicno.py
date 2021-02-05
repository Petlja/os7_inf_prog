# -*- acsection: general-init -*-
import math, random
import pygame as pg
import pygamebg

(sirina, visina) = (600, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Selo")

# -*- acsection: main -*-

# crta kućicu date boje kojoj je donje srednje teme u (x, y)
def kucica(boja, x, y, sirina_kucice):
    (x0, y0) = (x - sirina_kucice / 2, y - sirina_kucice)  # gornje levo teme osnove
    # crtamo osnovu kuće
    pg.draw.rect(prozor, boja, (x0, y0, sirina_kucice, sirina_kucice))
    # crtamo krov (jednakostranični trougao)
    krov_levo  = (x0, y0)                                                        # donje levo teme krova
    krov_desno = (x0+sirina_kucice, y0)                                          # donje desno teme krova
    krov_vrh   = (x0 + sirina_kucice/2, y0 - sirina_kucice * math.sqrt(3) / 2)   # vrh krova
    pg.draw.polygon(prozor, pg.Color("red"), [krov_levo, krov_desno, krov_vrh])
    # uokvirujemo osnovu kuće
    pg.draw.rect(prozor, pg.Color("black"), (x0, y0, sirina_kucice, sirina_kucice), 1)
    # crtamo vrata
    sirina_vrata = sirina_kucice / 4
    visina_vrata = sirina_kucice / 2
    vrata_levo = x0 + (sirina_kucice - sirina_vrata) / 2   # x koordinata leve ivice vrata
    vrata_gore = y - visina_vrata                          # y koordinata gornje ivice vraa
    pg.draw.rect(prozor, pg.Color("brown"), (vrata_levo, vrata_gore, sirina_vrata, visina_vrata))

prozor.fill(pg.Color("skyblue"))
broj_kucica = 5
maks_sirina_kucice = sirina / broj_kucica
for i in range(broj_kucica):
    boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = i * maks_sirina_kucice + maks_sirina_kucice / 2    # horizontalna sredina kucice
    y = visina
    sirina_kucice = random.randint(maks_sirina_kucice // 2, maks_sirina_kucice)
    kucica(boja, x, y, sirina_kucice)
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
