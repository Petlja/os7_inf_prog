# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (100, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "")

# -*- acsection: main -*-

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("black"))

duzina_linije = 50    # dužina linije rajsferšlusa
razmak_sa_strana = 15 # do leve i desne ivice prozora
razmak_gore_dole = 20 # do gornje i donje ivice prozora
razmak_izmedju_linija = 15 # između linija rasjferšlusa

# x koordinate početaka linija sa leve i desne strane
x_levo = razmak_sa_strana
x_desno = sirina - razmak_sa_strana - duzina_linije

# koordinate početka tekuće linije
x_poc = x_levo
y = razmak_gore_dole

while y < visina - razmak_gore_dole:
    x_kraj = x_poc + duzina_linije
    pg.draw.line(prozor, pg.Color("yellow"), (x_poc, y), (x_kraj, y), 6);
    
    # pripremamo crtanje sledece linije
    y += razmak_izmedju_linija # y je zadati broj piksela nize
    if x_poc == x_levo: # x_poc je suprotno od prethodnog
        x_poc = x_desno
    else:
        x_poc = x_levo

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
