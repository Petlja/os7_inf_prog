# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (100, random.randint(150, 500)) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))   
   
r = 10  # poluprečnik krugova
dy = 30 # razmak između centara dva uzastopna kruga

y = r   # y koordinata centra tekućeg kruga
while y - r <= visina:
    # crtamo krug
    pg.draw.circle(prozor, pg.Color("red"), (sirina // 2, y), r)
    y += dy  # centar narednog kruga je udaljen za dy od centra tekućeg kruga 

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
