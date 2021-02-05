# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()                                # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Boja pozadine")  # otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

boje = ["red", "green", "blue"]  # boje koje ćemo postavljati
broj_boje = 0                                                  # pozicija tekuće boje

def crtaj():
    prozor.fill(pg.Color(boje[broj_boje]))  # postavljanje boje pozadine na tekući element liste

def na_otkucaj_tajmera():
    global broj_boje # menjaćemo ovu globalnu promenljivu
    broj_boje = (broj_boje + 1) % len(boje)  # prelazimo na narednu boju

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
