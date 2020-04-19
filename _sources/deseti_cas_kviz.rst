Понављање облика коришћењем петљи - квиз
========================================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~       

.. mchoice:: sahtabla
    :answer_a: исцртава се шаховска табла састављена од црвених и плавих квадрата насумичних димензија
    :feedback_a: Тачно  
    :answer_b: исцртава се шаховска табла 8х8 од црвених и плавих квадрата
    :feedback_b: Нетачно  
    :answer_c: исцртава се мрежа насумично распоређених плавих и црвених квадрата насумичних димензија
    :feedback_c: Нетачно
    :answer_d: ниједан од осталих понуђених одговора није тачан.  
    :feedback_d: Нетачно    
    :correct: a
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg
        import random

        (sirina, visina) = (400, 400) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "")
        broj_polja = random.randint(10, 100)
        sirina_polja = int(sirina / broj_polja)
        visina_polja = int(visina / broj_polja)
        for i in range(broj_polja):
            for j in range(broj_polja):
                if (i+j)%2 == 1:
                    pg.draw.rect(prozor, pg.Color("blue"), (i*sirina_polja, j*visina_polja, sirina_polja, visina_polja))
                else:
                    pg.draw.rect(prozor, pg.Color("red"), (i*sirina_polja, j*visina_polja, sirina_polja, visina_polja))
        pygamebg.wait_loop()

    Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. mchoice:: krstici2
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Нетaчно   
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :answer_d: водоравно поређани крстићи
    :feedback_d: Tачно
    :correct: d
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pg.draw.line(prozor, pg.Color("black"), (x, y), (x+10, y), 1)
            pg.draw.line(prozor, pg.Color("black"), (x+5, y-5), (x+5, y+10), 1)
            x = x+20 

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~       

.. mchoice:: linije_udaljavanje
    :answer_a: исцртаваju се четири плаве линије које се смањују и између којих је размак све већи
    :feedback_a: Нетачно  
    :answer_b: исцртаваju се четири плаве линије које се смањују и између којих је размак све мањи
    :feedback_b: Нетачно  
    :answer_c: исцртаваju се четири плаве линије које се повећавају и између којих је размак све већи
    :feedback_c: Тачно
    :answer_d: исцртаваju се четири плаве линије које се повећавају и између којих је размак све мањи
    :feedback_d: Нетачно   
    :correct: c
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg

        (sirina, visina) = (400, 400) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "")
        prozor.fill(pg.Color("white"))
        y0 = 50
        y1 = visina - 30
        x = 30
        z = 50
        for i in range(10):
            pg.draw.line(prozor, pg.Color("blue"), (x, y1), (x, y0));
            y1 -= 10
            y0 -= 10
            x += z
            z += z*0.5
        pygamebg.wait_loop()

    Изабери тачан одговор:

Питање 4.
~~~~~~~~~       

.. mchoice:: linije_dijagonala
    :answer_a: цео прозор је ишпартан дијагонално насумичним бројем линија између 1 и 20 
    :feedback_a: Нетачно  
    :answer_b: горња Половина прозора је ишпартана дијагонално насумичним бројем линија
    :feedback_b: Нетачно  
    :answer_c: доња половина прозора је ишпартана дијагонално са 20 линија 
    :feedback_c: Нетачно
    :answer_d: доња половина прозора је ишпартана дијагонално насумичним бројем линија између 1 и 20 
    :feedback_d: Tačno    
    :correct: d
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg
        import random

        (sirina, visina) = (400, 300) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "")
        prozor.fill(pg.Color("white"))
        n = random.randint(1,20)
        x = int(sirina / n)
        y = int(visina / n()
        for i in range(n + 1):
            pg.draw.line(prozor, pg.Color("black"), (i*x, visina),  (sirina, i*y), 1)
        pygamebg.wait_loop()

    Изабери тачан одговор:

Питање 5.
~~~~~~~~~

.. mchoice:: uspravna1
    :answer_a: усправна испрекидана линија
    :feedback_a: Тачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Нетaчно   
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :answer_d: водоравно поређани крстићи
    :feedback_d: Нетачно
    :correct: a
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pg.draw.line(prozor, pg.Color("black"), (x, y), (x, y+10), 1)
            y = y+20

    Изабери тачан одговор:
