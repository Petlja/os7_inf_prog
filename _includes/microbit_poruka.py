# -*- acsection: general-init -*-
import random, math
import pygame as pg
import pygamebg

(sirina, visina) = (250, 250)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Microbit дисплеј")

def niz_crteza(str):
    A = [".11..",
         "1..1.",
         "1111.",
         "1..1.",
         "1..1."]
    B = ["111..",
         "1..1.",
         "111..",
         "1..1.",
         "111.."]
    V = ["1...1",
         "1...1",
         "1...1",
         ".1.1.",
         "..1.."]
    G = [".111.",
         "1....",
         "1..11",
         "1...1",
         ".111."]
    D = ["111..",
         "1..1.",
         "1..1.",
         "1..1.",
         "111.."]
    Dj= ["111..",
         "1..1.",
         "11.1.",
         "1..1.",
         "111.."]
    E = ["1111.",
         "1....",
         "111..",
         "1....",
         "1111."]
    Zx= [".1.1.",
         "1111.",
         "...1.",
         "..1..",
         "1111."]
    Z = ["1111.",
         "..1..",
         ".1...",
         "1....",
         "1111."]
    I = [".111.",
         "..1..",
         "..1..",
         "..1..",
         ".111."]
    J = ["11111",
         "...1.",
         "...1.",
         "1..1.",
         ".111."]
    K = ["1..1.",
         "1.1..",
         "11...",
         "1.1..",
         "1..1."]
    L = ["1....",
         "1....",
         "1....",
         "1....",
         "1111."]
    M = ["1...1",
         "11.11",
         "1.1.1",
         "1...1",
         "1...1"]
    N = ["1...1",
         "11..1",
         "1.1.1",
         "1..11",
         "1...1"]
    O = [".111.",
         "1...1",
         "1...1",
         "1...1",
         ".111."]
    P = ["111..",
         "1..1.",
         "111..",
         "1....",
         "1...."]
    R = ["111..",
         "1..1.",
         "111..",
         "1..1.",
         "1...1"]
    S = [".111.",
         "1....",
         ".11..",
         "...1.",
         "111.."]
    T = ["11111",
         "..1..",
         "..1..",
         "..1..",
         "..1.."]
    Cy= ["..1..",
         ".111.",
         "1....",
         "1....",
         ".111."]
    U = ["1..1.",
         "1..1.",
         "1..1.",
         "1..1.",
         ".11.."]
    F = ["1111.",
         "1....",
         "111..",
         "1....",
         "1...."]
    H = ["1..1.",
         "1..1.",
         "1111.",
         "1..1.",
         "1..1."]
    C = [".111.",
         "1....",
         "1....",
         "1....",
         ".111."]
    Cx= [".1.1.",
         ".111.",
         "1....",
         "1....",
         ".111."]
    Sx= [".1.1.",
         ".111.",
         "11...",
         "..11.",
         "111.."]
    Y = ["1..1.",
         "1..1.",
         ".11..",
         ".11..",
         ".11.."]
    razmak = [".....",
              ".....",
              ".....",
              ".....",
              "....."]
    slova = {"A" : A,
             "B" : B,
             "V" : V,
             "G" : G,
             "D" : D,
             "Đ" : Dj,
             "E" : E,
             "Ž" : Zx,
             "Z" : Z,
             "I" : I,
             "J" : J,
             "K" : K,
             "L" : L,
             "M" : M,
             "N" : N,
             "O" : O,
             "P" : P,
             "R" : R,
             "S" : S,
             "T" : T,
             "Ć" : Cy,
             "U" : U,
             "F" : F,
             "H" : H,
             "C" : C,
             "Č" : Cx,
             "Š" : Sx,
             "Y" : Y,
             " ": razmak}

    return [slova[slovo] for slovo in str]

def spoji_slova(tekst):
    matrica = []
    for v in range(5):
        vrsta = ""
        for slovo in tekst:
            vrsta += slovo[v] + " "
        matrica.append(vrsta)
    return matrica

def napravi_matricu(str):
    return spoji_slova(niz_crteza(str + " "))

# -*- acsection: main -*-

# matrica predstavlja niz od pet niski koje sadrže nule i jedinice (isključene i uključene diode)
# svaka niska predstavlja jednu vrstu teksta na displeja
matrica = napravi_matricu("PYGAME I MICROBIT")
# na displeju se prikazuju kolone k, k+1, k+2, k+3 i k+4
k = 0

# funkcija koja iz matrice izdvaja deo koji treba da se prikaže na
# displeju (to su kolone od k do k+4, pri čemu treba voditi računa da
# se kod poslednjih kolona odmah prelazi na početne).
def izdvoj_displej(k, matrica):
    displej = []
    for v in range(5):  # obrađujemo svaku od 5 vrsta
        vrsta = matrica[v] + matrica[v][0:5]  # zbog pomeranja u krug pre izdvajanja kolona matricu proširujemo sa 5 početnih kolona
        displej.append(vrsta[k:k+5])          # dodajemo kolone izdvojene iz tekuće vrste
    return displej

def crtaj_displej_5x5(displej):
    prozor.fill(pg.Color("white"))
    R = sirina // 5   # prečnik kruga u kome se nalazi dioda
    for i in range(5):
        for j in range(5):
            if displej[i][j] == '1':          # ako je dioda uključena
                r = R // 2                    # poluprečnik kruga u kome se nalazi dioda
                (x, y) = (j*R + r, i*R + r)   # centar pravougaonika koji predstavlja diodu (poklapa se sa centrom kruga)
                pg.draw.rect(prozor, pg.Color("red"), 
                             (x - 10, y - r + 10, 20, 2*r - 20)) # crtamo pravougaonik

def crtaj():
    displej = izdvoj_displej(k, matrica)   # izdvajamo relevantan deo matrice
    crtaj_displej_5x5(displej)             # crtamo ga

def novi_frejm():
    global k
    k = (k + 1) % len(matrica[0])    # prikaz pomeramo za jednu kolonu udesno
    crtaj()

# -*- acsection: after-main -*-

# funkcija novi_frejm se poziva 3 puta u sekundi
pygamebg.frame_loop(3, novi_frejm)
