# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg
import math

(sirina, visina) = (700, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "")

# -*- acsection: main -*-

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("white"))

duzina_linije = 150    # dužina linije rajsferšlusa
razmak_od_ivice = 30

# x koordinate početaka linija sa leve i desne strane
y_dole = visina-razmak_od_ivice
y_gore = razmak_od_ivice

# koordinate početka tekuće linije
x_poc = 30
y1 = y_dole
y2 = y_gore
x_pomeraj = math.sqrt((duzina_linije**2)-((y_dole-y_gore)**2))
x_kraj = x_poc+x_pomeraj
while x_kraj<sirina:
    
    pg.draw.line(prozor, pg.Color("yellow"), (x_poc, y1), (x_kraj, y2), 6);
    
    # pripremamo crtanje sledece linije
    x_poc=x_kraj
    x_kraj+=x_pomeraj
    if y1 == y_dole: # x_poc je suprotno od prethodnog
        y1 = y_gore
        y2 = y_dole
    else:
        y1 = y_dole
        y2 = y_gore
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
