# -*- acsection: general-init -*-
import pygame as pg, math
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Мачкица")

# -*- acsection: main -*-

# učitavamo slicicu iz datoteke macka.png
slika = pg.image.load("macka.png")
# prikazujemo sličicu u gornjem levom uglu prozora
prozor.blit(slika, (0, 0))

# -*- acsection: after-main -*-

pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
