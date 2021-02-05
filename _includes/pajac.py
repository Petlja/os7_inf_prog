# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pajac")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.circle(prozor, pg.Color("pink"), (150, 150), 150)
pg.draw.circle(prozor, pg.Color("white"), (70, 150), 50)
pg.draw.circle(prozor, pg.Color("black"), (100, 150), 20)
pg.draw.circle(prozor, pg.Color("white"), (230, 150), 50)
pg.draw.circle(prozor, pg.Color("black"), (200, 150), 20)
pg.draw.circle(prozor, pg.Color("red"), (150, 220), 40)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
