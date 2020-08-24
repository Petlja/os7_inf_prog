# -*- acsection: general-init -*-
import math, random
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Више лоптица")  # otvaramo prozor
(sirina, visina) = (300, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

r = 10
    
# funkcija koja nasumično određuje centar loptice, tako da loptica bude cela u prozoru
def nasumicna_tacka():
    return [random.randint(r, sirina - r), random.randint(r, visina - r)]

# funkcija koja nasumično određuje vektor brzine loptice (pomeraj po x i y osi)
def nasumicna_brzina():
    return [random.randint(-1, 1), random.randint(-1, 1)]
       
broj_loptica = 5                                            # broj loptica
polozaj = [nasumicna_tacka() for i in range(broj_loptica)]  # nasumično generišemo početne položaje loptica
brzina = [nasumicna_brzina() for i in range(broj_loptica)]  # nasumično generišemo početne vektore brzine loptica
    
def crtaj():
    prozor.fill(pg.Color("white"))                           # bojimo pozadinu u belo
    for (x, y) in polozaj:                                   # crtamo sve loptice
        pg.draw.circle(prozor, pg.Color("red"), (x, y), r)
    
# rastojanje između centara loptica    
def rastojanje(i, j):
    (x1, y1) = polozaj[i]
    (x2, y2) = polozaj[j]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
# provera da li se dve loptice sudaraju
def sudar(i, j):
    return rastojanje(i, j) <= 2*r

def novi_frejm():
    for i in range(broj_loptica):                                # obrađujemo sve loptice
        
        polozaj[i][0] += brzina[i][0]                            # pomeramo lopticu horizontalno
        if polozaj[i][0] - r < 0 or polozaj[i][0] + r > sirina:  # ako je ispala van prozora
            brzina[i][0] *= -1                                   #   menjamo joj horizontalni smer kretanja
            
        polozaj[i][1] += brzina[i][1]                            # pomeramo lopticu vertikalno
        if polozaj[i][1] - r < 0 or polozaj[i][1] + r > visina:  # ako je ispala van prozora
            brzina[i][1] *= -1                                   #   menjamo joj vertikalni smer kretanja
    
    for i in range(broj_loptica):                                # za svaki par loptica
        for j in range(i+1, broj_loptica):
            if sudar(i,j):                                       # ako se loptice sudaraju, razmenjujemo im brzine
                (brzina[i][0], brzina[i][1], brzina[j][0], brzina[j][1]) = \
                (brzina[j][0], brzina[j][1], brzina[i][0], brzina[i][1])            

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

    # pauziramo do sledeceg frejma
    sat.tick(100)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
