# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Cica Glisa")

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

# iscrtavamo glavu
pg.draw.circle(prozor, pg.Color("black"), (150, 70), 20, 2)
# iscrtavamo šešir
pg.draw.line(prozor, pg.Color("blue"), (120, 50), (180,50), 3)
pg.draw.rect(prozor, pg.Color("blue"), (130, 10, 40, 40))
# iscrtavamo oči
pg.draw.circle(prozor, pg.Color("black"), (145, 60), 2, 2)
pg.draw.circle(prozor, pg.Color("black"), (155, 60), 2, 2)
# iscrtavamo usta
pg.draw.ellipse(prozor, pg.Color("red"), (140, 75, 20, 10))
# iscrtavamo telo
pg.draw.line(prozor, pg.Color("black"), (150, 90), (150,170), 3)
# iscrtavamo levu ruku
pg.draw.line(prozor, pg.Color("black"), (150, 110), (100, 120), 3)
pg.draw.line(prozor, pg.Color("black"), (100, 120), (80, 100), 3)
# iscrtavamo desnu ruku
pg.draw.line(prozor, pg.Color("black"), (150, 110), (200, 150), 3)
pg.draw.line(prozor, pg.Color("black"), (200, 150), (210, 170), 3)
# iscrtavamo levu nogu
pg.draw.line(prozor, pg.Color("black"), (150, 170), (130, 200), 3)
pg.draw.line(prozor, pg.Color("black"), (130, 200), (140, 250), 3)
# iscrtavamo desnu nogu
pg.draw.line(prozor, pg.Color("black"), (150, 170), (170, 200), 3)
pg.draw.line(prozor, pg.Color("black"), (170, 200), (160, 250), 3)

# -*- acsection: after-main -*-

# prikazujemo nacrtano na ekranu
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()
