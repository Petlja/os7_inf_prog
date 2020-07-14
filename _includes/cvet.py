# -*- acsection: general-init -*-
import math
import pygame as pg, pygamebg

(sirina, visina) = (400, 400)  # uključujemo prozor dimenzije 400x400 piksela
prozor = pygamebg.open_window(400, 400, "Blue circle")

# boje koje ćemo koristiti
BELA = (255, 255, 255)
ZUTA = (255, 255, 0)
ROZE = (255, 200, 200)

# -*- acsection: main -*-
prozor.fill(BELA)   # bojimo pozadinu u belo

(cx, cy) = (sirina // 2, visina // 2) # koordinate centra prozora

# prečnici krugova - dužina stranice pravilnog šestougla u čijim se
# temenima nalaze centri krugova
a = 100
# visina karakterističnog trougla šestougla
h = round(a * math.sqrt(3) / 2)

# sva temena šestougla dele ove koordinate
x1 = cx + a
x2 = cx - a//2
x3 = cx + a//2
x4 = cx - a
y1 = cy - h
y2 = cy
y3 = cy + h

# koordinate temena šestougla
O = (cx, cy)
A1 = (x1, y2)
A2 = (x2, y1)
A3 = (x3, y1)
A4 = (x4, y2)
A5 = (x3, y3)
A6 = (x2, y3)

# poluprečnik krugova
r = a // 2

# iscrtavamo krugove
pg.draw.circle(prozor, ZUTA, O, r)
pg.draw.circle(prozor, ROZE, A1, r)
pg.draw.circle(prozor, ROZE, A2, r)
pg.draw.circle(prozor, ROZE, A3, r)
pg.draw.circle(prozor, ROZE, A4, r)
pg.draw.circle(prozor, ROZE, A5, r)
pg.draw.circle(prozor, ROZE, A6, r)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
