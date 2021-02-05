# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Krugovi")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# crtamo crveni krug
pg.draw.circle(prozor, pg.Color("red"), (50, 50), 30, 2)

# crtamo plavi krug
pg.draw.circle(prozor, pg.Color("blue"), (150, 150), 30)

# -*- acsection: after-main -*-

# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
