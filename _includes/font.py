# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Zdravo svete!")
# otvaramo prozor dimenzije 200x200
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
# -*- acsection: main -*-
# font kojim će biti prikazan tekst
font = pg.font.SysFont("Arial", 20)

# gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst = font.render("Zdravo svete!", True, pg.Color("black"))
# prikazujemo sličicu u gornjem levom uglu ekrana
prozor.blit(tekst, (0, 0))

# -*- acsection: after-main -*-
pg.time.delay(300)
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()

