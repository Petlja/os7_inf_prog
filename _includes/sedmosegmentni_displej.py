# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (180, 300)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Седмосегментни дисплеј")

# -*- acsection: main -*-

broj = 0  # broj

def crtaj():
    prozor.fill(pg.Color("white"))
    signali = ["1110111", "0010010", "1011101", "1011011", "0111010",
               "1101011", "1101111", "1010010", "1111111", "1111011"]
    signal = signali[broj]

    margina = 20
    debljina = 20
    visina = 100
    sirina = 100

    x1 = margina + debljina / 2
    x2 = x1 + sirina + debljina
    y1 = margina + debljina / 2
    y2 = y1 + visina + debljina
    y3 = y2 + visina + debljina

    if signal[0] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x1 + debljina / 2, y1), (x1 + debljina / 2 + sirina, y1), debljina)
    if signal[1] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x1, y1 + debljina / 2), (x1, y1 + debljina / 2 + visina), debljina)
    if signal[2] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x2, y1 + debljina / 2), (x2, y1 + debljina / 2 + visina), debljina)
    if signal[3] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x1 + debljina / 2, y2), (x1 + debljina / 2 + sirina, y2), debljina)
    if signal[4] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x1, y2 + debljina / 2), (x1, y2 + debljina / 2 + visina), debljina)
    if signal[5] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x2, y2 + debljina / 2), (x2, y2 + debljina / 2 + visina), debljina)
    if signal[6] == '1':
        pg.draw.line(prozor, pg.Color("black"), (x1 + debljina / 2, y3), (x1 + debljina / 2 + sirina, y3), debljina)

def novi_frejm():
    global broj
    broj = (broj + 1) % 10  # brojimo od 0 do 9 u krug
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 2 puta u sekundi
pygamebg.frame_loop(2, novi_frejm)
