# -*- acsection: general-init -*-
import random, math
import pygame as pg

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Loptica prati misa")  # otvaramo prozor
(sirina, visina) = (250, 250)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# pozicije centra loptice
trag = []

# rastojanje između dve tačke
def rastojanje(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

(x, y) = (sirina / 2, visina / 2)  # trenutna pozicija loptice (inicijalno u centru prozora)

def crtaj():
    # postavljanje boje pozadine na belu
    prozor.fill(pg.Color("white"))
    for (x, y) in trag:  # crtamo sve položaje loptice zabeležene u listi trag - zeleni krugovi uokvireni crnom kružnicom
        pg.draw.circle(prozor, pg.Color("green"), (round(x), round(y)), 10)
        pg.draw.circle(prozor, pg.Color("black"), (round(x), round(y)), 10, 1)

def novi_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()         # pozicija miša
    d = rastojanje((x, y), (xm, ym))      # rastojanje od pozicije miša do centra loptice
    v = 5                                 # brzina kretanja loptice
    if d < v:                             # ako je loptica veoma blizu miša
        (x, y) = (xm, ym)                 #   pomeramo joj centar tačno na poziciju miša
    else:                                 # u suprotnom
        x = x + v * (xm - x) / d          #   pomeramo je u pravcu miša
        y = y + v * (ym - y) / d
    if not trag or trag[-1] != (x, y):    # ako je trag prazan ili ako je njegov poslednji element različit od trenutne loptice
        trag.append((x, y))               #   ubacujemo lopticu

def obradi_dogadjaj(dogadjaj):
    global trag
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # događaj pritiska dugmeta miša
        trag = []                             # brišemo dosadašnji trag

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)

    # pauziramo do sledeceg frejma
    sat.tick(24)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
