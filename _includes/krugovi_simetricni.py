# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Кругови симетрични")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (300, 150)
prozor = pg.display.set_mode((sirina, visina))

prozor.fill(pg.Color("white"))
pg.draw.line(prozor, pg.Color("black"), (sirina/2, 0), (sirina/2, visina), 0.5)
pg.draw.line(prozor, pg.Color("black"), (0, 80), (sirina, 80), 0.5)
pg.draw.line(prozor, pg.Color("black"), (110, 0), (110, visina), 0.5)
pg.draw.line(prozor, pg.Color("black"), (190, 0), (190, visina), 0.5)
# font kojim će biti prikazan tekst
font = pg.font.SysFont("Arial", 9)

# gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst1 = font.render("80", True, pg.Color("black"))
tekst2 = font.render("150", True, pg.Color("black"))
tekst3 = font.render("(110,80)", True, pg.Color("black"))
tekst4 = font.render("(190,80)", True, pg.Color("black"))
tekst5 = font.render("110", True, pg.Color("black"))
tekst6 = font.render("190", True, pg.Color("black"))

prozor.blit(tekst1, (0, 80))
prozor.blit(tekst2, (150, 0))
prozor.blit(tekst3, (90, 85))
prozor.blit(tekst4, (170, 85))
prozor.blit(tekst5, (110, 0))
prozor.blit(tekst6, (190, 0))

# -*- acsection: main -*-

# crtamo crveni krug
pg.draw.circle(prozor, pg.Color("red"), (110, 80), 40, 1)

# crtamo plavi krug
pg.draw.circle(prozor, pg.Color("blue"), (190, 80), 40, 1)

# -*- acsection: after-main -*-

# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
