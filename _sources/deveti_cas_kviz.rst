Pонављање облика коришћењем петљи - квиз
========================================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~

.. mchoice:: for_rect_3
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Нетачно    
    :answer_c: слика 3
    :feedback_c: Нетачно    
    :answer_d: слика 4
    :feedback_d: Тачно
    :correct: d
    
    Која од датих слика настаје извршавањем следећег кода?

    .. code-block:: python

        for a in range(5):
            for b in range(3):
                pygame.draw.rect(prozor, pygame.Color("black"), (x+20*a, y+20*b, 10, 10), 1)


    .. image:: ../_images/pg_petlje_rect03.png

    Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: for_resetka
    :answer_a: код 1
    :feedback_a: Нетачно    
    :answer_b: код 2
    :feedback_b: Нетачно    
    :answer_c: код 3
    :feedback_c: Тачно
    :answer_d: код 4
    :feedback_d: Нетачно    
    :correct: c
    
    Којим од датих кодова се може нацртати решетка од *n* x *n* квадрата странице дужине *a* (по n+1 усправних и водоравних линија)?

    (1)
    
        .. code-block:: python

            for i in range(n+1):
                pygame.draw.line(prozor, pygame.Color("black"), (x, y+i*a), (x+a, y+i*a), 1)
                pygame.draw.line(prozor, pygame.Color("black"), (x+i*a, y), (x+i*a, y+a), 1)

    (2)
        .. code-block:: python

            for i in range(n+1):
                pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+a, y), 1)
                pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x, y+a), 1)

    (3)
        .. code-block:: python

            for i in range(n+1):
                pygame.draw.line(prozor, pygame.Color("black"), (x, y+i*a), (x+n*a, y+i*a), 1)
                pygame.draw.line(prozor, pygame.Color("black"), (x+i*a, y), (x+i*a, y+n*a), 1)

    (4)
        .. code-block:: python

            for i in range(n+1):
                pygame.draw.line(prozor, pygame.Color("black"), (x, y+i*a), (x, y+(i+1)*a), 1)
                pygame.draw.line(prozor, pygame.Color("black"), (x+i*a, y), (x+(i+1)*a, y), 1)



    Изабери тачан одговор:


Питање 3.
~~~~~~~~~       

.. fillintheblank:: for_rect_4
    
    Ове четири слике су креиране помоћу четири петље дате у наставку, али не у том редоследу. 

    .. image:: /../_images/pg_petlje_rect04.png

    Испиши редне бројеве петљи у редоследу у коме су дате резултујуће слике.

    (1)
    
        .. code-block:: python

            for a in range(0, 75, 15):
                pygame.draw.rect(prozor, pygame.Color("black"), (x, y+a, 50, 10), 1)

    (2)
        .. code-block:: python

            for a in range(10, 60, 10):
                pygame.draw.rect(prozor, pygame.Color("black"), (x, y, a, a), 1)

    (3)
        .. code-block:: python

            for a in range(10, 60, 10):
                pygame.draw.rect(prozor, pygame.Color("black"), (x-a, y-a, a, a), 1)

    (4)
        .. code-block:: python

            for a in range(0, 75, 15):
                pygame.draw.rect(prozor, pygame.Color("black"), (x+a, y, 10, 50), 1)



    Одговор: |blank|

   - :^\s*2413\s*$: Тачно
     :x: Одговор није тачан.


Питање 4.
~~~~~~~~~       

.. mchoice:: smena1
    :answer_a: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави и црвени, а низ почиње плавим квадратом.
    :feedback_a: Тачно
    :answer_b: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави и црвени, а низ почиње црвеним квадратом.
    :feedback_b: Нетачно
    :answer_c: Исцртава се 15 квадрата у низу, који насумично мењају боју 
    :feedback_c: Нетачно
    :answer_d: Ниједан од осталих понуђених одговора није тачан.  
    :feedback_d: Нетачно
    :correct: a
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg

        (sirina, visina) = (500, 100) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "Квадрати")
        broj_kvadrata = 15
        dimenzija_kvadrata = sirina / broj_kvadrata
        sredina = visina / 2
        for i in range(0, broj_kvadrata):
            if i % 2 == 0:
                boja = pg.Color("blue")
            else:
                boja = pg.Color("red")
            (x, y) = (i * dimenzija_kvadrata, sredina - dimenzija_kvadrata / 2)
            pg.draw.rect(prozor, boja, (x, y, dimenzija_kvadrata, dimenzija_kvadrata))
        pygamebg.wait_loop()



    Изабери тачан одговор:

Питање 5.
~~~~~~~~~       

.. mchoice:: smena2
    :answer_a: Исцртава се 15 квадрата који насумично мењају боју
    :feedback_a: Нетачно
    :answer_b: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави и црвени, а низ почиње црвеним квадратом.
    :feedback_b: Нетачно
    :answer_c: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави и црвени, а низ почиње плавим квадратом.
    :feedback_c: Тачно
    :answer_d: Ниједан од осталих понуђених одговора није тачан.
    :feedback_d: Нетачно
    :correct: c
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg

        (sirina, visina) = (500, 100)
        prozor = pygamebg.open_window(sirina, visina, "Квадрати")
        broj_kvadrata = 15
        dimenzija_kvadrata = sirina / broj_kvadrata
        sredina = visina / 2
        plavo = True
        for i in range(0, broj_kvadrata):
            if plavo:
                boja = pg.Color("blue")
            else:
                boja = pg.Color("red")
            plavo=not plavo
            (x, y) = (i * dimenzija_kvadrata, sredina - dimenzija_kvadrata / 2)
            pg.draw.rect(prozor, boja, (x, y, dimenzija_kvadrata, dimenzija_kvadrata))
        pygamebg.wait_loop()



    Изабери тачан одговор:



