# -*- acsection: general-init -*-
import pygame as pg, datetime

# inicijalizujemo biblioteku PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Дигитални сат")
# otvaramo prozor dimenzije 200x200 piksela
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def tekst_centriran(poruka, x, y):
    font = pg.font.SysFont("Arial", 40)     # font kojim će biti prikazan tekst
    # gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
    tekst = font.render(poruka, True, pg.Color("black"))
    # određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    # položaj određujemo tako da tekst bude centriran
    (x, y) = (x - sirina_teksta / 2, y - visina_teksta / 2)
    # prikazujemo sličicu na odgovarajućem mestu na ekranu
    prozor.blit(tekst, (x, y))

def crtaj():
    prozor.fill(pg.Color("white"))          # bojimo pozadinu u belo
    vreme = datetime.datetime.now()         # određujemo trenutno vreme
    sati = vreme.hour
    minuta = vreme.minute
    sekundi = vreme.second
    # tekst koja će se ispisivati    
    poruka = str(sati).rjust(2, "0") + ":" + \
             str(minuta).rjust(2, "0") + ":" + \
             str(sekundi).rjust(2, "0")
    tekst_centriran(poruka, sirina / 2, visina / 2)

def na_otkucaj_tajmera():
    pass

# -*- acsection: after-main -*-

pg.time.set_timer(pg.USEREVENT, 1000)  # navijamo tajmer tako da otkucava svake sekunde
kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()
        treba_crtati = False

    dogadjaj = pg.event.wait()  # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:
        kraj = True
    elif dogadjaj.type == pg.USEREVENT:
        na_otkucaj_tajmera()
        treba_crtati = True

pg.quit() # isključujemo rad biblioteke PyGame
