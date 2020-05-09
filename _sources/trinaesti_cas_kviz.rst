Анимације - квиз
================


Питање 1.
~~~~~~~~~

.. mchoice:: pg_slika_kroz_ivice1
    :answer_a: if x < 0:
    :feedback_a: Нетачно    
    :answer_b: if y + sl_visina < 0:
    :feedback_b: Нетачно    
    :answer_c: if x + sl_sirina < 0:
    :feedback_c: Тачно
    :answer_d: if y < 0:
    :feedback_d: Нетачно    
    :correct: c
    
    Нека су димензије дате слике sl_sirina и sl_visina, а њен горњи леви угао (x, y). Како проверавамо да ли је слика у потпуности прошла кроз леву ивицу прозора и више се не види ни један њен део?

    Изабери тачан одговор:


Питање 2.
~~~~~~~~~

.. mchoice:: pg_ciklicno1
    :answer_a: if x - 10 > sirina
    :feedback_a: Нетачно    
    :answer_b: if x - 100 > sirina 
    :feedback_b: Нетачно    
    :answer_c: if x - 110 > sirina
    :feedback_c: Нетачно    
    :answer_d: Ниједан од понуђених одговора није тачан.  
    :feedback_d: Тачно
    :correct: d
    
    Како треба допунити if наредбу у програму, да би се извршавањем тог програма приказивао квадрат који се креће с лева на десно, а у тренутку када више не би био у целости видљив, поново се појављује на почетној позицији и наставља да се креће на исти начин?

    .. code-block:: python

        import pygame as pg, pygamebg
        (sirina, visina) = (200, 200)
        prozor = pygamebg.open_window(sirina, visina, "")
        pocetna = 100
        x = pocetna
        def nov_frejm():
            global x
            if _____________________:
                x = x + 10
            else:
                x = pocetna
            prozor.fill(pg.Color("white"))
            pg.draw.rect(prozor, pg.Color("red"), (x, 100, 100, 100))
        pygamebg.frame_loop(10, nov_frejm)

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: pg_krug_kroz_ivice
    :answer_a: y + r < 0
    :feedback_a: Тачно
    :answer_b: y - r < 0
    :feedback_b: Нетачно    
    :answer_c: y  < 0
    :feedback_c: Нетачно    
    :answer_d: y - dy < 0
    :feedback_d: Нетачно    
    :correct: a

    Нека се круг полупречника r са центром у (x, y) помера за по *dy* пиксела на горе. Услов да је цео круг прошао кроз горњу ивицу екрана гласи:
    
    Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: pg_tamovamo
    :answer_a: x = sirina-r
    :feedback_a: Нетачно    
    :answer_b: dx = -dx
    :feedback_b: Тачно
    :answer_c: x = r
    :feedback_c: Нетачно    
    :answer_d: dx = -2
    :feedback_d: Нетачно    
    :correct: b
    
    Шта треба уписати на означено место у програму, да би његовим извршавањем био приказиван круг који се креће лево-десно одбијајући се о ивице прозора?

    .. code-block:: python

        import pygame as pg, pygamebg

        (sirina, visina) = (200, 100)
        prozor = pygamebg.open_window(sirina, visina, "pygame")
        x, y, dx, r = 30, 50, 2, 30

        def nov_frejm():
            global x, dx
            if x > sirina-r or x < r:
                ______________

            x = x + dx
            prozor.fill(pg.Color("skyblue"))
            pg.draw.circle(prozor, pg.Color("yellow"), (x, y), r)

        pygamebg.frame_loop(50, nov_frejm)

    Изабери тачан одговор:

Питање 5.
~~~~~~~~~


.. mchoice:: pg_animacija1
    :answer_a: 1) па 2)
    :feedback_a: Нетачно    
    :answer_b: 1) па 3)
    :feedback_b: Нетачно    
    :answer_c: 2) 
    :feedback_c: Нетачно    
    :answer_d: 1) и 2) у било ком редоследу
    :feedback_d: Нетачно    
    :answer_e: 1) и 3) у било ком редоследу     
    :feedback_e: Тачно
    :correct: e
    
    Следећи недовршени програм треба сваке секунде да промени боју позадине прозора.

    .. code-block:: python

        import pygame as pg, random
        pg.init()
        prozor = pg.display.set_mode((200,200))

        def nasumicna_boja():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        pg.time.set_timer(pg.USEREVENT,1000)

        kraj = False
        treba_crtati = True
        while not kraj:
        if treba_crtati:
            prozor.fill(nasumicna_boja())
            ___________
        dogadjaj = pg.event.wait()
        if dogadjaj.type == pg.QUIT:
            kraj = True
        elif dogadjaj.type == pg.USEREVENT:
            treba_crtati = True
        
        pg.quit()

    Које од наредних команди и у ком редоследу треба додати на означено место да би програм радио како је очекивано?

    1)
        .. code-block:: python

            pg.display.update()

    2)
        .. code-block:: python

            treba_crtati = True

    3)
        .. code-block:: python

            treba_crtati = False



    Изабери тачан одговор:


