# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Насумични облици")  # otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# funkcija koja vraća nasumično određenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# funkcija koja vraća nasumično određenu tačku na ekranu
def nasumicna_tacka():
    return (random.randint(0, sirina), random.randint(0, visina))

def crtaj():
    # postavljanje boje pozadine na belu
    prozor.fill(pg.Color("white"))

    # nasumično biramo oblik (1 linija, 2 kvadrat, 3 krug)
    oblik = random.randint(1, 3)
    if oblik == 1:
        # crtamo liniju koja spaja dve nasumične tacke
        pg.draw.line(prozor, nasumicna_boja(), nasumicna_tacka(), nasumicna_tacka(), 3)
    elif oblik == 2:
        # gornje levo teme pravougaonika odredjujemo nasumično, a
        # dimenzije tako da pravougaoni ne ispadne van ekrana
        (x, y) = nasumicna_tacka()
        s = random.randint(0, sirina - x)
        v = random.randint(0, visina - y)
        pg.draw.rect(prozor, nasumicna_boja(), (x, y, s, v))
    elif oblik == 3:
        # centar kruga biramo nasumično, a poluprečnik tako da
        # krug ne ispadne van ekrana
        (x, y) = nasumicna_tacka()
        r = random.randint(0, min(x, sirina-x, y, visina-y))
        pg.draw.circle(prozor, nasumicna_boja(), (x, y), r)

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
    sat.tick(4)

pg.quit() # isključujemo rad biblioteke PyGame
