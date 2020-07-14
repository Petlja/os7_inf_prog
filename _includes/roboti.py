# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (800, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Роботица Мица")


# definišemo boje koje cemo koristiti
SIVA = (250, 250, 250)
CRVENA = (255, 0, 0)
PLAVA = (0, 0, 255)

# debiljina linije
debljina = 3

prozor.fill(SIVA)

# -*- acsection: main -*-

def robot(cx, cy, telo):
    telo_x = cx - telo / 2
    telo_y = cy - telo / 2
    pg.draw.rect(prozor, PLAVA, (telo_x, telo_y, telo, telo), debljina)
    # haljina
    haljina_x = telo_x
    haljina_visina = telo / 8
    haljina_y = telo_y + telo - haljina_visina
    pg.draw.rect(prozor, CRVENA, (haljina_x, haljina_y, telo, haljina_visina))
    # glava
    glava = 3 * telo / 4
    glava_x = cx - glava / 2
    glava_y = telo_y - glava
    pg.draw.rect(prozor, PLAVA, (glava_x, glava_y, glava, glava), debljina)
    # oci
    oko = glava / 5
    zenica = oko / 3
    oko_y = glava_y + glava / 3 - oko / 2
    levo_oko_x = cx - oko / 2 - oko
    desno_oko_x = cx + oko / 2
    pg.draw.rect(prozor, CRVENA, (levo_oko_x, oko_y, oko, zenica), 1)
    pg.draw.rect(prozor, CRVENA, (desno_oko_x, oko_y, oko, zenica), 1)
    # usta
    usta_sirina = glava / 3
    usta_visina = usta_sirina / 3
    usta_y = glava_y + 2 * glava / 3 - usta_visina / 2
    pg.draw.rect(prozor, CRVENA, (glava_x + usta_sirina, usta_y, usta_sirina, usta_visina))
    # zenice
    pg.draw.rect(prozor, CRVENA, (levo_oko_x + zenica, oko_y, zenica, zenica))
    pg.draw.rect(prozor, CRVENA, (desno_oko_x + zenica, oko_y, zenica, zenica))
    # noge
    noga_sirina = telo / 3
    noga_duzina = noga_sirina * 3
    leva_noga_x = cx - noga_sirina
    leva_noga_y = telo_y + telo
    desna_noga_x = cx
    desna_noga_y = telo_y + telo
    pg.draw.rect(prozor, PLAVA, (leva_noga_x, leva_noga_y, noga_sirina, noga_duzina), debljina)
    pg.draw.rect(prozor, PLAVA, (desna_noga_x, desna_noga_y, noga_sirina, noga_duzina), debljina)
    # ruke
    ruka_sirina = telo / 6
    ruka_duzina = ruka_sirina * 4
    ruka_y = telo_y + ruka_sirina
    leva_ruka_x = telo_x - ruka_duzina
    desna_ruka_x = telo_x + telo
    pg.draw.rect(prozor, PLAVA, (leva_ruka_x, ruka_y, ruka_duzina, ruka_sirina), debljina)
    pg.draw.rect(prozor, PLAVA, (desna_ruka_x, ruka_y, ruka_duzina, ruka_sirina), debljina)

cy = visina // 2
robot(120, cy, 100)
robot(400, cy, 120)
robot(680, cy, 100)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
