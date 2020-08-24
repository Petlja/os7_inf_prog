# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()                                # pokrećemo biblioteku PyGame
pg.display.set_caption("Боја позадине")  # postavljamo naslov prozora
(sirina, visina) = (200, 200)            # otvaramo prozor dimenzije 200x200 piksela
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# funkcija koja vraća nasumično određenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

boja = nasumicna_boja()  # postavljamo nasumično početnu boju

# funkcija koja se izvržava svaki put kada se iscrtava ekran
def crtaj():
    prozor.fill(boja) # bojimo pozadinu na tekuću boju

# funkcija koja se izvršava na svaki otkucaj tajmera
def na_otkucaj_tajmera():
    global boja
    boja = nasumicna_boja()  # postavljamo nasumično tekuću boju

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
