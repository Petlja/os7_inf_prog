# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Macka")

# -*- acsection: main -*-

prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("gray"), (150, 160), 100) # glava
pg.draw.polygon(prozor, pg.Color("gray"), [(50, 30), (70, 100), (110, 100)]) # levo uvo
pg.draw.polygon(prozor, pg.Color("gray"), [(250, 30), (230, 100), (190, 100)]) # desno uvo
pg.draw.ellipse(prozor, pg.Color("yellow"), ( 90, 110, 40, 60)) # levo oko
pg.draw.ellipse(prozor, pg.Color("yellow"), (170, 110, 40, 60)) # desno oko
pg.draw.ellipse(prozor, pg.Color("green"),  (105, 135, 20, 30)) # leva zenica
pg.draw.ellipse(prozor, pg.Color("green"),  (175, 135, 20, 30)) # desna zenica
pg.draw.ellipse(prozor, pg.Color("darkgray"),  (80, 180, 70, 30)) # levi deo njuske
pg.draw.ellipse(prozor, pg.Color("darkgray"),  (150, 180, 70, 30)) # desni deo njuske
pg.draw.circle(prozor, pg.Color("black"), (150, 190), 10) # vrh njuske
pg.draw.line(prozor, pg.Color("black"), (90, 190), (20, 160), 2) # levi gornji brk
pg.draw.line(prozor, pg.Color("black"), (90, 195), (20, 195), 2) # levi srednji brk
pg.draw.line(prozor, pg.Color("black"), (90, 200), (20, 220), 2) # levi donji brk
pg.draw.line(prozor, pg.Color("black"), (210, 190), (280, 160), 2) # desni gornji brk
pg.draw.line(prozor, pg.Color("black"), (210, 195), (280, 195), 2) # desni srednji brk
pg.draw.line(prozor, pg.Color("black"), (210, 200), (280, 220), 2) # desni donji brk

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
