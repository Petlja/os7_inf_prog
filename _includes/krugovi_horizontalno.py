# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (600, 100) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Horizontalno rasporedjeni krugovi")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
   
# crtamo 10 krugova
r = 30  # poluprečnik krugova
x = r   # x koordinata centra kruga
for i in range(10):
    # crtamo krug
    pg.draw.circle(prozor, pg.Color("black"), (x, visina // 2), r, 1)
    x += 2 * r  # centar narednog kruga je udaljen za 2 * r od centra tekućeg kruga 

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
