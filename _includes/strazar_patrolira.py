# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 300)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Стражар који патролира")

# -*- acsection: main -*-

# učitavamo dve slike -
# stražara okrenutog na levo i stražara okrenutog na desno
strazar_levo  = pg.image.load('strazar_levo.png').convert()
strazar_desno = pg.image.load('strazar_desno.png').convert()

# izračunavamo dimenzije slika (obe slike su istih dimenzija)
strazar_sirina = strazar_levo.get_width()
strazar_visina = strazar_levo.get_height()

# početni polozaj stražara (gornjeg levog ugla slike)
x = 0
y = (visina - strazar_visina) / 2
# horizontalni pomeraj stražara u pikselima u svakom koraku
dx = 2

def crtaj():
    prozor.fill(pg.Color("white"))    # bojimo pozadinu u belo
    # u zavisnosti od smera kretanja biramo sliku koja će se prikazivati
    if dx > 0:
        slika = strazar_desno
    else:
        slika = strazar_levo
    prozor.blit(slika, (x, y))      # prikazujemo sliku na prozoru
    

def novi_frejm():
    global x, dx  # globalne promenljive koje se mogu promeniti
    x += dx       # pomeramo stražara
    if x < 0 or x + strazar_sirina > sirina: # ako je stražar ispao van prozora
        dx = -dx  # menjamo mu smer kretanja
    crtaj()
    
# -*- acsection: after-main -*-

pygamebg.frame_loop(50, novi_frejm)
