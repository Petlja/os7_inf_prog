# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Шетање лоптице тастатуром")

# podešavamo događaje tastaturom - prvi događaj se generise nakon
# 50ms, a svaki naredni nakon 25ms
pg.key.set_repeat(50, 25)

# -*- acsection: main -*-

(x, y) = (sirina // 2, visina // 2)  # koordinate centra prozora
r = 40                               # poluprečnik loptice
(dx, dy) = (10, 10)                  # pomeraji po x i y koordinati

def crtaj():
    # bojimo prozor u belo
    prozor.fill(pg.Color("white"))
    # crtamo lopticu
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), r)

def obradi_dogadjaj(dogadjaj):
    global x, y
    if dogadjaj.type == pg.KEYDOWN:      # pritisak tastera na tastaturi
        if dogadjaj.key == pg.K_LEFT:    # strelica na levo
            x -= dx                      # pomeramo lopticu na levo
            return True                  # treba ponovo nacrtati ekran
        if dogadjaj.key == pg.K_RIGHT:   # strelica na desno
            x += dx                      # pomeramo lopticu na desno
            return True                  # treba ponovo nacrtati ekran
        if dogadjaj.key == pg.K_UP:      # strelica na gore
            y -= dy                      # pomeramo lopticu na gore
            return True                  # treba ponovo nacrtati ekran
        if dogadjaj.key == pg.K_DOWN:    # strelica na dole
            y += dy                      # pomeramo lotpicu na dole
            return True                  # treba ponovo nacrtati ekran
    return False                         # ne treba ponovo nacrtati ekran

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)
