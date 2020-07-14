# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Кућа")     # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u svetlo plavo

pg.draw.polygon(prozor, pg.Color("red"), [(50, 150), (120, 100), (190, 150)]) # krov
pg.draw.rect(prozor, pg.Color("khaki"), ( 50, 150, 140, 100))  # kuca
pg.draw.rect(prozor, pg.Color("brown"), ( 60, 170,  30,  30))  # levi prozor
pg.draw.rect(prozor, pg.Color("brown"), (150, 170,  30,  30))  # desni prozor
pg.draw.rect(prozor, pg.Color("brown"), (100, 180,  40,  70))  # vrata

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
