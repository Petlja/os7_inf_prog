# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Krugovi simetricni")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (600, 300)
prozor = pg.display.set_mode((sirina, visina))

prozor.fill(pg.Color("white"))
pg.draw.line(prozor, pg.Color("black"), (sirina/2, 0), (sirina/2, visina), 0.5)
pg.draw.line(prozor, pg.Color("black"), (0, 150), (sirina, 150), 0.5)

# font kojim će biti prikazan tekst
font = pg.font.SysFont("Arial", 9)

# gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst1 = font.render("150", True, pg.Color("black"))
tekst2 = font.render("300", True, pg.Color("black"))
tekst3 = font.render("M1(150, 100)", True, pg.Color("black"))
tekst4 = font.render("M2(450, 100)", True, pg.Color("black"))

prozor.blit(tekst1, (0, 150))
prozor.blit(tekst2, (300, 0))
prozor.blit(tekst3, (130, 85))
prozor.blit(tekst4, (430, 85))


# -*- acsection: main -*-

# crtamo crveni pravougaonik
pg.draw.rect(prozor, pg.Color("red"), (370, 100, 80, 100), 1)
# crtamo plavi pravougaonik
pg.draw.rect(prozor, pg.Color("blue"), (150, 100, 80, 100), 1)
# crtamo crvenu elipsu
pg.draw.ellipse(prozor, pg.Color("red"), (370, 100, 80, 100), 1)
# crtamo plavu elipsu
pg.draw.ellipse(prozor, pg.Color("blue"), (150, 100, 80, 100), 1)
# -*- acsection: after-main -*-

# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
