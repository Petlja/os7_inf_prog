Квиз - гранање
==============


Питање 1.
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
        prozor = pygamebg.open_window(sirina, visina, "pygame-quiz3")
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

Питање 2.
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
        prozor = pygamebg.open_window(sirina, visina, "pygame-quiz2")
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



Питање 3.
~~~~~~~~~       

.. mchoice:: smena3
    :answer_a: код 1 
    :feedback_a: Нетачно
    :answer_b: код 2
    :feedback_b: Нетачно
    :answer_c: код 3
    :feedback_c: Тачно
    :answer_d: код 4
    :feedback_d: Нетачно
    :correct: c
    
    Које две линије кода могу заменити ``if`` наредбу у следећем коду. 

    .. code-block:: python

        import pygame as pg
        import pygamebg

        (sirina, visina) = (500, 100) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "pygame-quiz1")
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

    (1)
    
        .. code-block:: python
            
            boje = [pg.Color("blue"), pg.Color("red")]
            for i in range(boje):
                boja = boje[i % 0]

    (2)
        .. code-block:: python

            for i in range(n+1):
                boja = i

    (3)
        .. code-block:: python

            boje = [pg.Color("blue"), pg.Color("red")]
            boja = boje[i % len(boje)]

    (4)
        .. code-block:: python

                
            boja1, boja2 = pg.Color("blue"), pg.Color("red")
            boja1 = not boja2


    Изабери тачан одговор:

Питање 4.
~~~~~~~~~       

.. mchoice:: smena4
    :answer_a: Исцртава се 15 квадрата који насумично мењају боју
    :feedback_a: Нетачно
    :answer_b: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави, црвени, браон и наранџасти, а низ почиње црвеним квадратом.
    :feedback_b: Нетачно
    :answer_c: Исцртава се 15 квадрата у низу. Квадрати су наизменично плави, црвени, браон и наранџасти, а низ почиње плавим квадратом.
    :feedback_c: Тачно
    :answer_d: Ниједан од осталих понуђених одговора није тачан.
    :feedback_d: Нетачно
    :correct: c
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg
        import pygamebg

        (sirina, visina) = (500, 100) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "pygame-quiz")

        broj_kvadrata = 15
        dimenzija_kvadrata = sirina / broj_kvadrata
        sredina = visina / 2

        boje = [pg.Color("blue"), pg.Color("red"), pg.Color("brown"), pg.Color("orange")]
        for i in range(0, broj_kvadrata):
            boja = boje[i % len(boje)]
            (levo, gore) = (i*dimenzija_kvadrata, sredina - dimenzija_kvadrata / 2)
            pg.draw.rect(prozor, boja, (levo, gore, dimenzija_kvadrata, dimenzija_kvadrata))

        pygamebg.wait_loop()


    Изабери тачан одговор:

