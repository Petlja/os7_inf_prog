# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (800, 600) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Дрворед")

# -*- acsection: main -*-

def zatamni(boja, zatamnjenje):
    (r, g, b) = boja
    return (round(r*zatamnjenje), round(g*zatamnjenje), round(b*zatamnjenje))

def jelka(x, y, dim, zatamnjenje):
    # boje koje cemo koristiti
    CRNA  = (0, 0, 0)
    ZELENA = (0, 100, 36)
    BRAON = (97, 26, 9)
    
    j = dim / 300
    pg.draw.rect(prozor, BRAON, (x-20*j, y-50*j, 40*j, 50*j))
    # krošnja - trougao A
    Alevo = (x-100*j, y-50*j)
    Adesno = (x+100*j, y-50*j)
    Agore = (x, y-150*j)
    pg.draw.polygon(prozor, zatamni(ZELENA, zatamnjenje), [Alevo, Adesno, Agore])
    # krošnja - trougao B
    Blevo = (x-75*j, y-100*j)
    Bdesno = (x+75*j, y-100*j)
    Bgore = (x, y-200*j)
    pg.draw.polygon(prozor, zatamni(ZELENA, zatamnjenje), [Blevo, Bdesno, Bgore])
    # krošnja - trougao C
    Clevo = (x-50*j, y-150*j)
    Cdesno = (x+50*j, y-150*j)
    Cgore = (x, y-250*j)
    pg.draw.polygon(prozor, zatamni(ZELENA, zatamnjenje), [Clevo, Cdesno, Cgore])

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
horizont_y = visina * 0.55         # visina linije horizonta
# crtamo nebo i sunce
pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, horizont_y))
pg.draw.circle(prozor, pg.Color("yellow"), (150, 150), 65)

broj_stabala = 6

# crtatmo levi drvored
x, y, dim = sirina / 2 - 0.1 * sirina, horizont_y + 0.1 * visina,  150
for i in range(broj_stabala):
    jelka(x, y, dim, random.uniform(0.2, 2.0))
    x -= 0.075 * sirina
    y += 0.05 * visina
    dim += 20

# crtamo desni drvored
x, y, dim = sirina / 2 + 0.1 * sirina, horizont_y + 0.1 * visina,  150
for i in range(broj_stabala):
    jelka(x, y, dim, random.uniform(0.2, 2.0))
    x += 0.075 * sirina
    y += 0.05 * visina
    dim += 20
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
