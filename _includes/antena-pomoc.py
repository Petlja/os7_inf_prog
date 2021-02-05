# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

# otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pygamebg.open_window(sirina, visina, "Antena")

# -*- acsection: main -*-
def crtanje():
    prozor.blit(platno, (0, 0))  # crtanje onoga sto je zadato
    
    # ose
    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina), 1) # uspravna linija misa
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y), 1) # vodoravna linija misa

    # ispis koordinata
    str_x, str_y = str(mis_x), str(mis_y)
    xt_y, yt_y = (5, mis_y - 25) if 2 * mis_y > visina else (visina - 25, mis_y + 5)
    xt_x, yt_x = (mis_x - 50, 5) if 2 * mis_x > sirina else (mis_x + 5, sirina - 50)
    sl_x = font.render(str_x, True, pg.Color("black"))
    sl_y = font.render(str_y, True, pg.Color("black"))
    prozor.blit(sl_x, (xt_x, xt_y))
    prozor.blit(sl_y, (yt_x, yt_y))

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

################# crtez
platno = pg.Surface((sirina, visina)) # platno na kome je slika nacrtana
platno.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo

pg.draw.line(platno, pg.Color('black'), (150,  50), (150, 250), 4)
pg.draw.line(platno, pg.Color('black'), (120,  75), (180,  75), 1)
pg.draw.line(platno, pg.Color('black'), (110, 100), (190, 100), 1)
pg.draw.line(platno, pg.Color('black'), (100, 125), (200, 125), 2)
pg.draw.line(platno, pg.Color('black'), ( 90, 150), (210, 150), 2)
pg.draw.line(platno, pg.Color('black'), ( 80, 175), (220, 175), 3)
pg.draw.line(platno, pg.Color('black'), ( 70, 200), (230, 200), 3)
#################

font = pg.font.SysFont("Arial", 20)         # font kojim će biti prikazan tekst
font.set_bold(True)
mis_x, mis_y = 0, 0

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

# Zavrsetak skrivenog progrma, koji radi kao primer
pg.time.set_timer(pg.QUIT,50)
pg.time.wait(70)
pg.time.set_timer(pg.QUIT,0)

# Zavrsetak korisnickog programa je posebnoj sekciji

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
