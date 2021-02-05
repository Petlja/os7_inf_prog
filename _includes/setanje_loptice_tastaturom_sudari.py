# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Setanje loptice tastaturom")

# podešavamo događaje tastaturom - prvi događaj se generiše nakon
# 50ms, a svaki naredni nakon 25ms
pg.key.set_repeat(50, 25)

# funkcija koja vraća nasumično odredjenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# -*- acsection: main -*-

(x, y) = (sirina / 2, visina / 2)   # koordinate centra prozora
boja = nasumicna_boja()             # boja loptice se odredjuje nasumično
r = 40                              # poluprečnik loptice
(dx, dy) = (10, 10)                 # pomeraji po x i y koordinati

def crtaj():
    # bojimo prozor u belo
    prozor.fill(pg.Color("white"))
    # crtamo lopticu
    pg.draw.circle(prozor, boja, (round(x), round(y)), r)

def obradi_dogadjaj(dogadjaj):
    global x, y, boja

    if dogadjaj.type == pg.KEYDOWN:
        # kada je pritisnut taster, ponovo ćemo crtati lopticu
        if dogadjaj.key == pg.K_LEFT:    # strelica na levo
            x -= dx                      # pomeramo lopticu na levo
            if x - r < 0:                # ako je ispala van prozora
                x = r                    #    vraćamo je
                boja = nasumicna_boja()  #    menjamo joj boju
            return True                  # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_RIGHT:   # strelica na desno
            x += dx                      # pomeramo lopticu na levo
            if x + r > sirina:           # ako je ispala van prozora
                x = sirina - r           #    vraćamo je
                boja = nasumicna_boja()  #    menjamo joj boju
            return True                  # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_UP:      # strelica na gore
            y -= dy                      # pomeramo lopticu na levo
            if y - r < 0:                # ako je ispala van prozora
                y = r                    #    vraćamo je
                boja = nasumicna_boja()  #    menjamo joj boju
            return True                  # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_DOWN:    # strelica na dole
            y += dy                      # pomeramo lopticu na levo
            if y + r > sirina:           # ako je ispala van prozora
                y = sirina - r           #    vraćamo je
                boja = nasumicna_boja()  #    menjamo joj boju
            return True                  # treba ponovo nacrtati scenu
        return False                     # ne treba ponovo nacrtati scenu

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)
