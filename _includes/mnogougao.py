# -*- acsection: general-init -*-
import pygame as pg, math  

# uključivanje rada biblioteke PyGame
pg.init()  
  
# podešavamo naslov prozora
pg.display.set_caption("Многоугао")

# otvaramo prozor dimenzije 300x350
(sirina, visina) = (300, 350)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu ekrana u belo
prozor.fill(pg.Color("white"))

# temena mnogougla
temena = [(50, 300), (50, 150), (150, 50), (250, 150), (250, 300)]
# crtamo mnogougao popunjen crvenom bojom
pg.draw.polygon(prozor, pg.Color("red"), temena)
# crtamo crni okvir oko mnogougla
pg.draw.polygon(prozor, pg.Color("black"), temena, 3)


# -*- acsection: after-main -*-
# prikazujemo nacrtano na ekranu
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
