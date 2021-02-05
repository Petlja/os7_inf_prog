# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # uključujemo rad biblioteke PyGame
pg.display.set_caption("Crtanje misem")  # otvaramo prozor
(sirina, visina) = (400, 500)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

duzi = []  # lista duži koje sačinjavaju crtež (duži su uređeni parovi tačaka)

def crtaj():
    prozor.fill(pg.Color("white"))  # bojimo pozadinu prozora u belo
    for (A, B) in duzi:
        pg.draw.line(prozor, pg.Color("black"), A, B, 2)

def obradi_dogadjaj(dogadjaj):
    # pomeranje miša
    if dogadjaj.type == pg.MOUSEMOTION:
       if dogadjaj.buttons[0]:         # ako je pritisnuto levo dugme
           (px, py) = dogadjaj.pos     # položaj miša nakon pomeranja
           (rx, ry) = dogadjaj.rel     # pomeranje u odnosu na prethodni položaj
           # dodajemo linijicu izmedju prethodnog i tekućeg položaja miša
           duzi.append(((px, py), (px + rx, py + ry)))
           return True # ponovo treba iscrtati sliku
    return False # ne treba ponovo crtati


# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()             # osvežavamo prikaz prozora
        treba_crtati = False
    dogadjaj = pg.event.wait()        # čekamo da se dogodi neki događaj
    if dogadjaj.type == pg.QUIT:      # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)
pg.quit()  # isključujemo rad biblioteke PyGame

