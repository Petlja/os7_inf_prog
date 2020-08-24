# -*- acsection: general-init -*-
import datetime, math
import pygame as pg

import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Аналогни сат")

# -*- acsection: main -*-

# funkcija koja izrаčunava koordinate tacke na krugu sa centrom
# u (x, y), poluprečnika r, koja zaklapa ugao alpha sa položajem
# 12 sati
def tacka_na_krugu(cx, cy, r, alpha):
    alpha_rad = math.radians(alpha)
    x = cx + r * math.sin(alpha_rad)
    y = cy - r * math.cos(alpha_rad)
    return (x, y)

def crtaj():
    # bojimo pozadinu u belo
    prozor.fill(pg.Color("white"))

    # crtamo krug sata
    (cx, cy) = (sirina // 2, visina // 2)
    r = round(0.9 * min(sirina // 2, visina // 2))
    pg.draw.circle(prozor, pg.Color("black"), (cx, cy), r, 5)

    # crtamo male podeoke za svaki minut
    for ugao in range(0, 360, 360 // 60):
        (x1, y1) = tacka_na_krugu(cx, cy, 0.9*r, ugao)
        (x2, y2) = tacka_na_krugu(cx, cy, r, ugao)
        pg.draw.line(prozor, pg.Color("black"), (x1, y1), (x2, y2), 1)

    # crtamo malo vece podeoke za svaki sat
    for ugao in range(0, 360, 360 // 12):
        (x1, y1) = tacka_na_krugu(cx, cy, 0.8*r, ugao)
        (x2, y2) = tacka_na_krugu(cx, cy, r, ugao)
        pg.draw.line(prozor, pg.Color("black"), (x1, y1), (x2, y2), 1)

    # ispisujemo brojeve
    font = pg.font.SysFont('Arial', 15)     # font kojim cemo pisati brojeve
    for i in range(1, 12+1):
        ugao = i * (360 // 12)
        tekst = font.render(str(i), True, pg.Color("black"))         # tekst koji se ispisuje
        (tekst_sirina, tekst_visina) = (tekst.get_width(), tekst.get_height())   # dimenzije teksta
        (x, y) = tacka_na_krugu (cx, cy, 0.75*r, ugao)                           # prikazujemo tekst tako da mu je centar tacka na krugu
        prozor.blit(tekst, (x - tekst_sirina / 2, y - tekst_visina / 2))

    # crtamo kazaljke

    # određujemo trenutno vreme
    vreme = datetime.datetime.now()
    sati = vreme.hour % 12 # svodimo sate na interval [0, 12)
    minuta = vreme.minute
    sekundi = vreme.second

    # na osnovu vremena izračunavamo uglove koje kazaljke zaklapaju sa
    # položajem podneva
    ugao_sekundne_kazaljke = (sekundi * 360) // 60
    ugao_minutne_kazaljke = (minuta * 360) // 60
    ugao_satne_kazaljke = ((sati * 60 + minuta) * 360) // 720

    # crtamo jednu po jednu kazaljku
    (x, y) = tacka_na_krugu(cx, cy, round(0.9*r), ugao_sekundne_kazaljke)
    pg.draw.line(prozor, pg.Color("red"), (cx, cy), (x, y), 3)
    (x, y) = tacka_na_krugu(cx, cy, round(0.9*r), ugao_minutne_kazaljke)
    pg.draw.line(prozor, pg.Color("black"), (cx, cy), (x, y), 5)
    (x, y) = tacka_na_krugu(cx, cy, round(0.7*r), ugao_satne_kazaljke)
    pg.draw.line(prozor, pg.Color("black"), (cx, cy), (x, y), 10)

# -*- acsection: after-main -*-

# funkciju crtaj pozivamo svake sekunde
pygamebg.frame_loop(1, crtaj)
