# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Срце")

# -*- acsection: main -*-

# parametarske jednačine
def f(t):
    return (16*math.sin(t)**3,
            13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))

# prevodi koordinate date tačke iz koordinatnog sistema sveta u
# ekranski koordinatni sistem
def u_ekranske(tacka):
    (x, y) = tacka # ekstrahujemo x i y iz uređenog para
    k = 7 # koeficijent skaliranja
    return (round(sirina / 2 + k*x), round(visina / 2 - k*y))

# izracunava i-tu tacku u podeli intervala [a, b] na n jednako
# razmaknutih tačaka
def podela_intervala(a, b, i, n):
    return a + i * (b - a) / (n - 1)

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
# broj tačaka podele
n = 100
# parametarski interval 
(a, b) = (0, 2*math.pi)
# prethodna tačka
prethodna = f(a)
for i in range(1, n+1):
    # tekuca tačka
    tekuca = f(podela_intervala(a, b, i, n))
    # crtamo duž između prethodne i tekuće tačke
    pg.draw.line(prozor, pg.Color("red"), u_ekranske(prethodna), u_ekranske(tekuca), 3)
    # prelazimo na narednu duž
    prethodna = tekuca

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
    
