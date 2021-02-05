# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Koncentricni krugovi")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))
# centar kruga je u centru prozora
centar = (sirina // 2, visina // 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 10, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 20, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 30, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 40, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 50, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 60, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 70, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 80, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 90, 5)
pg.draw.circle(prozor, pg.Color("red"), centar, 100, 5)

# -*- acsection: after-main -*-

# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
