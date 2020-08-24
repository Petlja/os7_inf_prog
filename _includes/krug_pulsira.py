# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Круг који пулсира") # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

(x, y) = (sirina // 2, visina // 2)  # pozicija loptice (u centru prozora)
(min_r, max_r) = (50, 100)           # najmanji i najveći dopusteni poluprečnik
r = min_r  # početni poluprečnik loptice
dr = 1     # porast poluprečnika

def crtaj():
    prozor.fill(pg.Color("white"))  # bojimo pozadinu u belo
    pg.draw.circle(prozor, pg.Color("red"), (x, y), r) # crtamo crveni krug

def novi_frejm():
    global r, dr   # globalne promenljive koje ćemo menjati
    r += dr        # menjamo poluprečnik kruga
    if r <= min_r or r >= max_r: # ako se on previše smanjio ili povećao
        dr = -dr   # obrćemo smer promene veličine

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
    sat.tick(40)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
