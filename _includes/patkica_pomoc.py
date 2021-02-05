# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Patkica")

# -*- acsection: main -*-

mis_x, mis_y = 0, 0
plava = (154, 209, 229)
zuta = (255, 221, 62)
def tekst(s, x, y):
    # font kojim će biti prikazan tekst
    font = pg.font.SysFont("Arial", 25)
    tekst = font.render(s, True, pg.Color("white"))
    # određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    # položaj određujemo tako da tekst bude centriran
    (x, y) = (x - sirina_teksta * (x / sirina), y - visina_teksta * (y / visina))
    # prikazujemo sličicu na odgovarajućem mestu na ekranu
    prozor.blit(tekst, (x, y))

    
def crtanje():
  #definišemo naše boje
    #definišemo naše boje
    plava = (154, 209, 229)
    zuta = (255, 221, 62)
    # bojimo pozadinu u belo
    prozor.fill(pg.Color("white"))
    #crtamo rukice
    #leva
    pg.draw.ellipse(prozor, plava, (50, 220, 60, 30))
    pg.draw.ellipse(prozor, pg.Color("black") , (50, 220, 60, 30), 7)
    #desna
    pg.draw.ellipse(prozor, plava, (290, 220, 60, 30))
    pg.draw.ellipse(prozor, pg.Color("black") , (290, 220, 60, 30), 7)
    # crtamo glavu
    pg.draw.rect(prozor, plava, (75, 75, 250, 250))
    pg.draw.rect(prozor, pg.Color("black"), (75, 75, 250, 250), 7)
    # crtamo oči
    pg.draw.ellipse(prozor, pg.Color("black"), (100, 180, 60, 80))
    pg.draw.ellipse(prozor, pg.Color("black"), (240, 180, 60, 80))
    # crtamo usta
    pg.draw.ellipse(prozor, zuta, (170, 230, 60, 30))
    pg.draw.ellipse(prozor, pg.Color("black") , (170, 230, 60, 30), 7)
    #crtamo nogice
    #leva
    pg.draw.ellipse(prozor, zuta, (60, 280, 60, 60))
    pg.draw.ellipse(prozor, pg.Color("black"), (60, 280, 60, 60), 7)
    #desna
    pg.draw.ellipse(prozor, zuta, (280, 280, 60, 60))
    pg.draw.ellipse(prozor, pg.Color("black"), (280, 280, 60, 60), 7)
 
    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina))
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y))
    s = "(" + str(mis_x) + ", " + str(mis_y) + ")"
    pg.display.set_caption(s)

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

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

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
