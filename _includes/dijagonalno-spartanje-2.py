# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Дијагонално шпартање")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))

# broj podeoka
n = 10
# prirastaj
dx = sirina / n
dy = visina / n

# Crtamo n linija iznad sporedne dijagonale (ukljucujuci i nju)
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (0, i*dy), (i*dx, 0), 1)

# Crtamo n linija iznad sporedne dijagonale (ukljucujuci i nju)
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("black"), (0, i*dy), (i*dx, 0), 1)
# Crtamo n-1 linija ispod sporedne dijagonale (bez nje)
for i in range(1, n):
    pg.draw.line(prozor, pg.Color("black"), (i*dx, visina), (sirina, i*dy), 1)

# Crtamo n linija ispod glavne dijagonale (ukljucujuci i nju)
for i in range(n + 1):
    pg.draw.line(prozor, pg.Color("red"), (i*dx, visina), (0, visina-i*dy), 1)
# Crtamo n-1 linija iznad glavne dijagonale (bez nje)
for i in range(1, n):
    pg.draw.line(prozor, pg.Color("red"), (i*dx, 0), (sirina, visina-i*dy), 1)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
