# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Једнакостранични троугао")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# dužina stranice trougla
a = 100
# visina trougla
h = a * math.sqrt(3) / 2

# koordinate sredine prozora
sredina = sirina / 2

# koordinate temena - težiste deli visinu u odnosu 1 : 2
A = (sredina - a / 2, sredina + h / 3)
B = (sredina + a / 2, sredina + h / 3)
C = (sredina, sredina - 2 * h / 3)
 
# debljina linije
debljina = 2

# crtamo tri duži različitih boja
pg.draw.line(prozor, pg.Color("red"), A, B, debljina)
pg.draw.line(prozor, pg.Color("green"), B, C, debljina)
pg.draw.line(prozor, pg.Color("blue"), C, A, debljina)
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
