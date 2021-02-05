# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Kruzni lukovi")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# crtamo crveni luk
pg.draw.arc(prozor, pg.Color("red"), (0, 0, 100, 100), math.radians(0), math.radians(120), 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("black"), (0, 0, 100, 100), 1)

# crtamo plavi luk
pg.draw.arc(prozor, pg.Color("blue"), (100, 0, 100, 100), math.radians(-180), math.radians(-30), 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("black"), (100, 0, 100, 100), 1)

# crtamo zeleni luk
pg.draw.arc(prozor, pg.Color("green"), (0, 100, 100, 100), 0, 1, 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("black"), (0, 100, 100, 100), 1)

# crtamo zuti luk
pg.draw.arc(prozor, pg.Color("yellow"), (100, 100, 100, 100), 0, math.pi, 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("black"), (100, 100, 100, 100), 1)

# -*- acsection: after-main -*-
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
