# -*- acsection: general-init -*-
import math, random
import pygame as pg

# inicijalizujemo biblioteku PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Кругови на дијагонали")
# otvaramo prozor dimenzije 300x300 piksela
(sirina, visina) = (400, 500)
prozor = pg.display.set_mode((sirina, visina))

# funkcija kojom se generiše nasumična boja
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# -*- acsection: main -*-

n = 5  # broja krugova na dijagonali 

def crtaj():
    # crtanje n krugova duž sporedne dijagonale prozora
    d = math.sqrt(sirina**2 + visina**2)   # dužina dijagonale prozora
    r = d / (2 * n)                        # poluprečnik jednog kruga
    kx = sirina / (2 * n)                  # horizontalno rastojanje centara
    ky = visina / (2 * n)                  # vertikalno rastojanje centara
    prozor.fill(pg.Color("white"))
    for i in range(n):
        (cx, cy) = ((2*i+1)*kx, visina - (2*i+1)*ky)
        pg.draw.circle(prozor, nasumicna_boja(), (round(cx), round(cy)), round(r))

def obradi_dogadjaj(dogadjaj):
    global n
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisak dugmeta miša
        if dogadjaj.button == 1:              # oznaka za levi taster miša je 1
            n += 1                            # uvećavamo broj krugova
            return True                       # treba ponovo nacrtati scenu
        elif dogadjaj.button == 3 and n > 1:  # oznaka za desni taster miša je 3
            n -= 1                            # smanjujemo broj krugova
            return True                       # treba ponovo nacrtati scenu
    elif dogadjaj.type == pg.KEYDOWN:         # pritisak tastera na tastaturi
        if dogadjaj.key == pg.K_UP:           # strelica na gore
            n += 1                            # uvećavamo broj krugova
            return True                       # treba ponovo nacrtati scenu
        elif dogadjaj.key == pg.K_DOWN and n > 1:  # strelica na dole
            n -= 1                            # smanjujemo broj krugova
            return True                       # treba ponovo nacrtati scenu
    return False                              # ne treba ponovo crtati scenu
    
# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg
    dogadjaj = pg.event.wait()        # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:      # isklučivanje prozora
        kraj = True
    else:                             # ostali događaji
        treba_crtati = obradi_dogadjaj(dogadjaj)
        
pg.quit()   # isključujemo rad biblioteke PyGame
