# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Koncentrični krugovi")  # otvaramo prozor
(sirina, visina) = (225, 225)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

broj_krugova = 1   # broj krugova koji se trenutno craju
r = 10             # razlika poluprečnika susednih krugova
dk = 1             # promena broja krugova

def crtaj():
    prozor.fill(pg.Color("white"))            # bojimo pozadinu u belo
    (cx, cy) = (sirina // 2, visina // 2)     # centar krugova
    for i in range(1, broj_krugova + 1):      # crtamo krugove
        pg.draw.circle(prozor, pg.Color("red"), (cx, cy), i*r, 2)

def novi_frejm():
    global broj_krugova, dk
    # ako se promenom u tekućem smeru broj krugova povećava ili
    # smanjuje previše, menjamo smer promene
    if broj_krugova + dk > 10 or broj_krugova + dk < 1: 
        dk = -dk
    broj_krugova += dk  # menjamo broj krugova za 1, u odgovarajućem smeru

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
    sat.tick(10)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
