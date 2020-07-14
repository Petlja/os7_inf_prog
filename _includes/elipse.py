# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Елипсе")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# crtamo crvenu elipsu
pg.draw.ellipse(prozor, pg.Color("red"), (0, 0, 100, 150), 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("red"), (0, 0, 100, 150), 1)

# crtamo plavu elipsu
pg.draw.ellipse(prozor, pg.Color("blue"), (100, 0, 100, 100), 2)
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("blue"), (100, 0, 100, 100), 1)

# crtamo zelenu elipsu
pg.draw.ellipse(prozor, pg.Color("green"), (0, 150, 200, 50))
# crtamo opisani pravougaonik
pg.draw.rect(prozor, pg.Color("green"), (0, 150, 200, 50), 1)

# -*- acsection: after-main -*-
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
