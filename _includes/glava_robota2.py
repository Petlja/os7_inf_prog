# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Глава робота")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))

# sidro je u centru ekrana
(cx, cy) = (sirina / 2, visina / 2)
# dimenzija glave robota je 200x200 piksela
glava_dim = 200

# gornje levo teme glave određujemo tako da je centar glave u tački (cx, cy)
glava_x = cx - glava_dim / 2
glava_y = cy - glava_dim / 2
pg.draw.rect(prozor, pg.Color("orange"), (glava_x, glava_y, glava_dim, glava_dim))

# relativna dimenzija oka u odnosu na dimenziju glave
oko_dim = glava_dim / 5
# dimenzija razmaka oko očiju i oko usta
razmak = glava_dim / 5

# gornje levo teme levog oka u odnosu na gornje levo teme glave
levo_oko_x = glava_x + razmak
levo_oko_y = glava_y + razmak
pg.draw.rect(prozor, pg.Color("black"), (levo_oko_x, levo_oko_y, oko_dim, oko_dim))

# gornje levo teme desnog oka u odnosu na gornje levo teme levog oka
desno_oko_x = levo_oko_x + oko_dim + razmak
desno_oko_y = levo_oko_y
pg.draw.rect(prozor, pg.Color("black"), (desno_oko_x, desno_oko_y, oko_dim, oko_dim))

# dimenzije usta u odnosu na dimenziju oka
usta_visina = oko_dim
usta_sirina = 2 * oko_dim
# gornje levo teme usta u odnosu gornje levo teme glave
usta_x = glava_x + (glava_dim - usta_sirina) / 2
usta_y = glava_y + glava_dim - razmak - usta_visina
pg.draw.rect(prozor, pg.Color("black"), (usta_x, usta_y, usta_sirina, usta_visina))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
