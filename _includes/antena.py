# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

# otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pygamebg.open_window(sirina, visina, "Антена")

# -*- acsection: main -*-
prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo

pg.draw.line(prozor, pg.Color('black'), (150,  50), (150, 250), 4)
pg.draw.line(prozor, pg.Color('black'), (120,  75), (180,  75), 1)
pg.draw.line(prozor, pg.Color('black'), (110, 100), (190, 100), 1)
pg.draw.line(prozor, pg.Color('black'), (100, 125), (200, 125), 2)
pg.draw.line(prozor, pg.Color('black'), ( 90, 150), (210, 150), 2)
pg.draw.line(prozor, pg.Color('black'), ( 80, 175), (220, 175), 3)
pg.draw.line(prozor, pg.Color('black'), ( 70, 200), (230, 200), 3)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
