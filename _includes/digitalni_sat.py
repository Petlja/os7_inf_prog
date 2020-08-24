# -*- acsection: general-init -*-
import pygame as pg, datetime

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Дигитални сат") # otvaramo prozor
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
    poruka = (str(sati).rjust(2, "0") + ":" + 
              str(minuta).rjust(2, "0") + ":" +
              str(sekundi).rjust(2, "0"))
    tekst_centriran(poruka, sirina / 2, visina / 2)

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
    sat.tick(1)

pg.quit() # isključujemo rad biblioteke PyGame
