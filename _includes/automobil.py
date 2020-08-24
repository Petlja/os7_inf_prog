# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (500, 500)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Аутомобил")

# -*- acsection: main -*-

# dimenzije automobila
donji_deo_sirina = 240   # širina donjeg dela
donji_deo_visina = 50    # visina donjeg dela
gornji_deo_sirina = 160   # širina gornjeg dela
gornji_deo_visina = 50   # visina gornjeg dela
r_tocka = 30             # poluprečnik točka

auto_v = 100          # brzina auta (broj piksela u sekundi)
auto_cx = 0            # početni polozaj - x koordinata
auto_cy = visina / 2   # početni polozaj - y koordinata
frejmova_u_sekundi = 50
dt = 1 / frejmova_u_sekundi

def crtaj():
    donji_deo_vrh = auto_cy - donji_deo_visina            # vrh donjeg dela auta
    donji_deo_levo  = auto_cx - donji_deo_sirina / 2      # levi kraj donjeg dela auta
    gornji_deo_vrh  = donji_deo_vrh - gornji_deo_visina   # vrh gornjeg dela auta
    gornji_deo_levo = auto_cx - gornji_deo_sirina / 2     # levi kraj gornjeg dela auta
    levi_tocak_cx   = auto_cx - gornji_deo_sirina / 2     # centar levog točka
    desni_tocak_cx  = auto_cx + gornji_deo_sirina / 2     # centar desnog točka

    # bojimo pozadinu prozora u plavo
    prozor.fill(pg.Color("skyblue"))

    # crtamo donji deo auta
    pg.draw.rect(prozor, pg.Color("yellow"),
                 (donji_deo_levo, donji_deo_vrh, donji_deo_sirina, donji_deo_visina))
    pg.draw.rect(prozor, pg.Color("black"),
                 (donji_deo_levo, donji_deo_vrh, donji_deo_sirina, donji_deo_visina), 2)

    # crtamo gornji deo auta
    pg.draw.rect(prozor, pg.Color("yellow"),
                 (gornji_deo_levo, gornji_deo_vrh, gornji_deo_sirina, gornji_deo_visina))
    pg.draw.rect(prozor, pg.Color("black"),
                 (gornji_deo_levo, gornji_deo_vrh, gornji_deo_sirina, gornji_deo_visina), 2)

    # crtamo točkove
    pg.draw.circle(prozor, pg.Color("black"), (round(levi_tocak_cx), round(auto_cy)), r_tocka)
    pg.draw.circle(prozor, pg.Color("white"), (round(levi_tocak_cx), round(auto_cy)), 3)

    pg.draw.circle(prozor, pg.Color("black"), (round(desni_tocak_cx), round(auto_cy)), r_tocka)
    pg.draw.circle(prozor, pg.Color("white"), (round(desni_tocak_cx), round(auto_cy)), 3)

def novi_frejm():
    global auto_cx           # menjaćemo horizontalni položaj auta
    auto_cx += auto_v * dt   # pomeramo auto nadesno
    levi_kraj = auto_cx - donji_deo_sirina / 2 # pozicija levog kraja automobila
    if levi_kraj > sirina:                     # ako je ispao van prozora
        auto_cx = - donji_deo_sirina / 2       #    vraćamo ga na početak
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(frejmova_u_sekundi, novi_frejm)
