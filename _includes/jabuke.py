import random
import pygame as pg
import pygamebg

(sirina, visina) = (500, 300)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Хватање јабука")

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature


korpa  = pg.image.load("korpa.png")   # učitavamo sliku korpe
jabuka = pg.image.load("jabuka.png")  # učitavamo sliku jabuke
zivot  = jabuka   # slicica zivota je slicica jabuke

MAKS_JABUKE = 3 # maksimalni broj jabuka koje mogu biti istovremeno na ekranu
jabuke = []     # koordinate jabuka trenutno na ekranu
poeni = 0       # trenutni broj poena
zivoti = 3      # trenutni broj zivota
(korpa_x, korpa_y) = (0, visina - korpa.get_height()) # koordinate gornjeg levo ugla korpe

# postavljamo jabuku na vrh ekrana, na nasumično određenu koordinatu x 
def dodaj_jabuku():
    x = random.randint(0, sirina - jabuka.get_width())
    jabuke.append([x, 25])

# dodajemo jabuke nasumično
def dodaj_jabuke():
    # ako je korpa prazna obavezno dodajemo novu jabuku ako u korpi
    # ima manje od tri jabuke tada bacamo kockicu tako da ocekujemo da
    # se jabuka doda u 1% slučajeva
    if len(jabuke) == 0 or (len(jabuke) < MAKS_JABUKE and random.randint(1, 100) == 1):
        dodaj_jabuku()

# sve jabuke pomeramo naniže        
def pomeri_jabuke():
    for jabuka in jabuke:
        jabuka[1] += 1

# kupimo jabuke koje su upale u korpu ili pale na zemlju i ažuriramo
# broj poena i života
def pokupi_jabuke():
    global jabuke, poeni, zivoti
    # pošto će se neke jabuke ukloniti iz liste, prepisujemo sadržaj
    # liste u novu
    nove_jabuke = []
    for [x, y] in jabuke:
        # jabuka je upala u korpu
        if (y > visina - korpa.get_height() and
           korpa_x <= x and x <= korpa_x + korpa.get_width()):
            poeni += 1
        # jabuka je pala na zemlju
        elif y > visina:
            zivoti -= 1
        else:
            nove_jabuke.append([x, y])
    # preostaju samo one jabuke su koje su prepisane u novu listu
    jabuke = nove_jabuke

# prikazujemo sadržaj prozora
def crtaj():
    prozor.fill(pg.Color("white"))
    # prikazujemo broj poena
    font = pg.font.SysFont("Arial", 20) # font kojim će biti prikazan broj poena
    tekst = font.render("Поени: " + str(poeni), True, pg.Color("black"))
    prozor.blit(tekst, (5, 5))
    # prikazujemo preostale zivote
    for i in range(1, zivoti + 1):
        prozor.blit(zivot, (sirina - 5 - i*zivot.get_width(), 5))
    # prikazujemo sve jabuke
    for [x, y] in jabuke:
        prozor.blit(jabuka, (x, y))
    # prikazujemo korpu
    prozor.blit(korpa, (korpa_x, korpa_y))

def obradi_dogadjaj(dogadjaj):
    global korpa_x
    if dogadjaj.type == pg.KEYDOWN: # tastaturom pomeramo korpu
        if dogadjaj.key == pg.K_LEFT:     # strelica na levo
            korpa_x -= 10
            crtaj()
        elif dogadjaj.key == pg.K_RIGHT:  # strelica na desno
            korpa_x += 10
            crtaj()
    
def novi_frejm():
    global kraj
    dodaj_jabuke()
    pomeri_jabuke()
    pokupi_jabuke()
    # proveravamo da li smo izgubili sve živote
    if zivoti <= 0:
        kraj = True
    crtaj()


pygamebg.frame_loop(25, novi_frejm, obradi_dogadjaj)
