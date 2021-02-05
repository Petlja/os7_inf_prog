# -*- acsection: general-init -*-
import pygame as pg
pg.init()  # uključujemo rad biblioteke pygame
pg.display.set_caption("Crtanje misem")  # otvaramo prozor
(sirina, visina) = (400, 500)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

dugme_pritisnuto = False              # da li je dugme miša pritisnuto
platno = pg.Surface((sirina, visina)) # platno na kome je slika nacrtana
platno.fill(pg.Color("white"))        # bojimo pozadinu platno u belo

def crtaj():
    prozor.blit(platno, (0, 0))       # prikazujemo platno sa slikom na prozoru

def obradi_dogadjaj(dogadjaj):
    global crtanje, prethodna_pos, dugme_pritisnuto
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:                                           # pritisak na dugme miša
        prethodna_pos = dogadjaj.pos                                                  #   početak prve linije je na mestu pritska dugmeta
        dugme_pritisnuto = True                                                       #   dugme je pritisnuto
    elif dogadjaj.type == pg.MOUSEBUTTONUP:                                           # otpuštanje dugmeta miša
        dugme_pritisnuto = False                                                      #   dugme više nije pritisnuto
    elif dogadjaj.type == pg.MOUSEMOTION:                                             # pomeranje miša
        if dugme_pritisnuto:                                                          #   ako je dugme pritisnuto
            pg.draw.line(platno, pg.Color("black"), prethodna_pos, dogadjaj.pos)      #     dodajemo na platno linijicu između prethodnog i tekućeg položaja miša
            prethodna_pos = dogadjaj.pos                                              #     pamtimo tekuću poziciju kao početak naredne linije
            return True                                                               #     treba ponovo iscrati sliku
    return False                                                                      # ne treba ponovo crtati sliku

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()           # osvežavamo prikaz prozora
        treba_crtati = False
    dogadjaj = pg.event.wait()        # čekamo da se dogodi neki događaj
    if dogadjaj.type == pg.QUIT:      # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)
pg.quit()  # isključujemo rad biblioteke PyGame
