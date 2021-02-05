# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Boja pozadine")

# -*- acsection: main -*-

# funkcija koja vraća nasumično određenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

boja = nasumicna_boja()  # postavljamo nasumično početnu boju

# funkcija koja se izvržava svaki put kada se iscrtava ekran
def crtaj():
    prozor.fill(boja) # bojimo pozadinu na tekuću boju

# funkcija koja se izvršava na svaki otkucaj tajmera
def novi_frejm():
    global boja
    boja = nasumicna_boja()  # postavljamo nasumično tekuću boju
    crtaj()

# -*- acsection: after-main -*-

# zapocinjemo animaciju tako sto svake sekunde pozivamo funkciju novi_frejm
pygamebg.frame_loop(1, novi_frejm)
