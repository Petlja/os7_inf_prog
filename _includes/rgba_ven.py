# -*- acsection: general-init -*-
import pygame as pg, math
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Венови дијаграми")

# -*- acsection: main -*-

r = 50
(cx, cy) = (visina / 2, sirina / 2)
h = r * math.sqrt(3) / 2

prozor.fill(pg.Color("white"))

surf1 = pg.Surface((sirina, visina))
surf1.set_colorkey((0, 0, 0))
surf1.set_alpha(200)
pg.draw.circle(surf1, (255, 0, 0), (round(cx - r/2), round(cy - h/3)), r)
prozor.blit(surf1, (0, 0))

surf2 = pg.Surface((sirina, visina))
surf2.set_colorkey((0, 0, 0))
surf2.set_alpha(200)
pg.draw.circle(surf2, (0, 255, 0), (round(cx + r/2), round(cy - h/3)), r)
prozor.blit(surf2, (0, 0))

surf3 = pg.Surface((sirina, visina))
surf3.set_colorkey((0, 0, 0))
surf3.set_alpha(200)
pg.draw.circle(surf3, (0, 0, 255), (round(cx), round(cy + 2*h/3)), r)
prozor.blit(surf3, (0, 0))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
