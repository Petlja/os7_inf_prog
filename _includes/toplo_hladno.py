# -*- acsection: general-init -*-
import math, random
import pygame as pg

pg.init()   # uključujemo rad biblioteke PyGame
pg.display.set_caption("Pronadji tacku")  # otvaramo prozor
(visina, sirina) = (400, 400)
prozor = pg.display.set_mode((visina, sirina))

# -*- acsection: main -*-

# rastojanje između dve tačke (zadate parovima koordinata)
def rastojanje(A, B):
    (x1, y1) = A
    (x2, y2) = B
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# funkcija određuje nasumičnu tačku na ekranu
def nasumicna_tacka():
    return (random.randint(0, sirina), random.randint(0, visina))

mis = (0, 0)  # pozicija miša
tacka = nasumicna_tacka()  # nepoznata tačka
prikazi_tacku = False      # u početku je ona skrivena

def crtanje():
    r = rastojanje(tacka, mis)                       # rastojanje od nepoznate tačke do miša
    maks_r = max(rastojanje(tacka, (0, 0)),          # najveće rastojanje od
                 rastojanje(tacka, (0, visina)),     # nepoznate tačke do
                 rastojanje(tacka, (sirina, 0)),     # bilo koje tačke na ekranu
                 rastojanje(tacka, (sirina, visina)))
    # boju određujemo tako da kada je miš došao do nepoznate take ona bude
    # crvena, a kada je na najdaljoj tački na ekranu ona bude crna
    boja = (round(255 - r/maks_r*255), 0, 0)
    prozor.fill(boja)                                        # bojimo prozor
    if prikazi_tacku:                                        # ako je odabrano da se prikazuje nepoznata tačka
        pg.draw.circle(prozor, pg.Color("black"), tacka, 3)  #   prikazujemo je

def obradi_dogadjaj(dogadjaj):
    global mis, tacka, prikazi_tacku
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:    # pritisak dugmeta miša
        if dogadjaj.button == 1:               #    levo dugme
            prikazi_tacku = not prikazi_tacku  #       menjamo prikaz nepoznate tačke
            return True                        #      treba ponovo iscrtati ekran
        elif dogadjaj.button == 3:             #    desno dugme
            tacka = nasumicna_tacka()          #      biramo novu nepoznatu tačku
            prikazi_tacku = False              #      sakrivamo je
            return True                        #      treba ponovo iscrtati ekran
    elif dogadjaj.type == pg.MOUSEMOTION:      # pomeranje miša
        mis = dogadjaj.pos                     #    pamtimo poziciju miša
        return True                            #   treba ponovo iscrtati ekran
    return False                               # ne treba ponovo iscrtavati ekran

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame
