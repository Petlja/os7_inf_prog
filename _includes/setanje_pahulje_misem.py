# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Setanje pahulje misem") # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

pahulja_slika = pg.image.load("pahulja.png")
mis = (sirina // 2, visina // 2)
pg.mouse.set_pos(mis)

def crtanje():
    # bojimo prozor u belo
    prozor.fill(pg.Color("white"))
    # crtamo pahulju
    slika_sirina = pahulja_slika.get_width()
    slika_visina = pahulja_slika.get_height()
    (x, y) = mis
    centar = (x - slika_sirina // 2, y - slika_visina // 2)
    prozor.blit(pahulja_slika, centar)

def obradi_dogadjaj(dogadjaj):
    global mis
    if dogadjaj.type == pg.MOUSEMOTION:
        mis = dogadjaj.pos
        return True
    return False

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključujemo rad biblioteke PyGame
