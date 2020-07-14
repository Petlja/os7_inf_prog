# -*- acsection: general-init -*-
import pygame as pg, math
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Паткица")

# -*- acsection: main -*



#definišemo naše boje
plava = (154, 209, 229)
zuta = (255, 221, 62)
# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
#crtamo rukice
#leva
pg.draw.ellipse(prozor, plava, (50, 220, 60, 30))
pg.draw.ellipse(prozor, pg.Color("black") , (50, 220, 60, 30), 7)
#desna
pg.draw.ellipse(prozor, plava, (290, 220, 60, 30))
pg.draw.ellipse(prozor, pg.Color("black") , (290, 220, 60, 30), 7)
# crtamo glavu
pg.draw.rect(prozor, plava, (75, 75, 250, 250))
pg.draw.rect(prozor, pg.Color("black"), (75, 75, 250, 250), 7)
# crtamo oči
pg.draw.ellipse(prozor, pg.Color("black"), (100, 180, 60, 80))
pg.draw.ellipse(prozor, pg.Color("black"), (240, 180, 60, 80))
# crtamo usta
pg.draw.ellipse(prozor, zuta, (170, 230, 60, 30))
pg.draw.ellipse(prozor, pg.Color("black") , (170, 230, 60, 30), 7)
#crtamo nogice

#leva
pg.draw.circle(prozor, zuta, (90, 305), 30)
pg.draw.circle(prozor, pg.Color("black"), (90, 305), 30, 7)
#desna
pg.draw.circle(prozor, zuta, (310, 305), 30)
pg.draw.circle(prozor, pg.Color("black"), (310, 305), 30, 7)
#crtamo obraščiće
pg.draw.circle(prozor, zuta, (100, 260), 10)
pg.draw.circle(prozor, pg.Color("black"), (100, 260), 10, 3)
# -*- acsection: after-main -*-


# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
