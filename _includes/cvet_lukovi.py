# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Cvet")

# -*- acsection: main -*-

# pomoćna funkcija za crtanje kruznog luka
def luk(prozor, boja, centar, r, pocetni_ugao, krajnji_ugao, debljina):
    (x, y) = centar
    pg.draw.arc(prozor, boja, (x - r, y - r, 2 * r, 2 * r),
                math.radians(pocetni_ugao), math.radians(krajnji_ugao), debljina)

# boje koje cemo koristiti
BELA = (255, 255, 255)
CRVENA = (255, 0, 0)
ZELENA = (0, 255, 0)
PLAVA = (0, 0, 255)
ZUTA = (255, 255, 0)
LJUBICASTA = (255, 0, 255)
REZEDA = (0, 255, 255)

prozor.fill(BELA)  # bojimo pozadinu u belo

(cx, cy) = (sirina // 2, visina // 2) # koordinate centra prozora

# prečnici krugova - dužina stranice pravilnog šestougla u čijim se
# temenima nalaze centri krugova
a = 100
# visina karakterističnog trougla šestougla
h = round(a * math.sqrt(3) / 2)

# sva temena šestougla dele ove koordinate
x1 = cx - a
x2 = cx - a//2
x3 = cx + a//2
x4 = cx + a
y1 = cy - h
y2 = cy
y3 = cy + h

# koordinate temena šestougla
A1 = (x1, y2)
A2 = (x2, y1)
A3 = (x3, y1)
A4 = (x4, y2)
A5 = (x3, y3)
A6 = (x2, y3)

# poluprečnik krugova
r = a

# debljina linija
debljina = 3

# iscrtavamo krugove
luk(prozor, CRVENA, A1, r, -60, 60, debljina)
luk(prozor, ZELENA, A2, r, -120, 0, debljina)
luk(prozor, PLAVA, A3, r, -180, -60, debljina)
luk(prozor, ZUTA, A4, r, 120, -120, debljina)
luk(prozor, LJUBICASTA, A5, r, 60, 180, debljina)
luk(prozor, REZEDA, A6, r, 0, 120, debljina)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
