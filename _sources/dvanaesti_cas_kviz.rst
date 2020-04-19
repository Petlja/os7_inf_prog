Анимације - квиз
================

Питање 1.
~~~~~~~~~

.. mchoice:: pg_brzi_krug
    :answer_a: Брже се креће круг у првом програму
    :feedback_a: Нетачно    
    :answer_b: Истом брзином, али у првом програму је кретање испрекидано а у другом глатко
    :feedback_b: Тачно
    :answer_c: Брже се креће круг у другом програму
    :feedback_c: Нетачно    
    :answer_d: Кругови се крећу истом брзином и на исти начин
    :feedback_d: Нетачно    
    :correct: b
    
    У којем од два дата програмска сегмента се круг брже креће по екрану (у пикселима по секунди)?

    (1)
        .. code-block:: python

            def novi_frejm():
                global x
                x += 5
                prozor.fill(pg.Color("white"))
                pg.draw.circle(prozor, pg.Color("red"), (x, y), 30)
      
            pygamebg.frame_loop(10, novi_frejm)    

    (2)
        .. code-block:: python

            def novi_frejm():
                global x
                x += 1
                prozor.fill(pg.Color("white"))
                pg.draw.circle(prozor, pg.Color("red"), (x, y), 30)
      
            pygamebg.frame_loop(50, novi_frejm)    
    
    Изабери тачан одговор:


Питање 2.
~~~~~~~~~

.. mchoice:: pg_brzina_pixpersec
    :answer_a: 3 пиксела по секунди
    :feedback_a: Нетачно    
    :answer_b: 20 пиксела по секунди
    :feedback_b: Нетачно    
    :answer_c: 60 пиксела по секунди
    :feedback_c: Тачно
    :answer_d: не помера се
    :feedback_d: Нетачно    
    :correct: c
    
    Дат је део програма којим се анимира кретање црвеног круга

    .. code-block:: python

          def novi_frejm():
              global x
              x += 3
              prozor.fill(pg.Color("white"))
              pg.draw.circle(prozor, pg.Color("red"), (x, y), 30)
      
          pygamebg.frame_loop(20, novi_frejm)    

    Којом брзином се помера круг по екрану?

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: pg_krug_raste
    :answer_a: На сваких 100 милисекунди круг се помера за 10 пиксела на десно.
    :feedback_a: Нетачно    
    :answer_b: На сваких 100 милисекунди круг се помера за 10 пиксела на доле.
    :feedback_b: Нетачно    
    :answer_c: На сваких 100 милисекунди полупречник круга (који је на почетку 20 пиксела) се повећава за 10 пиксела.
    :feedback_c: Тачно
    :answer_d: Ниједан од осталих понуђених одговора није тачан.  
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg, pygamebg
        prozor = pygamebg.open_window(200,200, "")
        a = 20
        def nov_frejm():
            global a
            prozor.fill(pg.Color("white"))
            pg.draw.circle(prozor, pg.Color("red"), (100, 100), a)
            a = a + 10
        pygamebg.frame_loop(10, nov_frejm)


    Изабери тачан одговор:


Питање 4.
~~~~~~~~~

.. mchoice:: pg_kretanje_vise_objekata_2
    :multiple_answers:
    :answer_a: Сваки круг има своју брзину
    :feedback_a: Тачно
    :answer_b: Брзина кругова се мења
    :feedback_b: Нетачно    
    :answer_c: Кругови се одбијају о ивице прозора
    :feedback_c: Нетачно    
    :answer_d: кругови мењају боју при сваком исцртавању фрејма
    :feedback_d: Нетачно    
    :correct: ['a']
    
    Дата је функција *nov_frejm*, која се позива одређени број пута у секунди и анимира кретање *n* кругова (изостављена је иницијализација глобалних података, али треба претпоставити да су сви подаци на почетку различити). Сваки елемент листе *krugovi* је торка која описује један круг.

    .. code-block:: python

        def nov_frejm():
            global krugovi
            prozor.fill(pg.Color("white"))
            for i in range(n):
                x, y, dx, dy, boja, r = krugovi[i]
                x += dx
                y += dy
                krugovi[i] = (x, y, dx, dy, boja, r)
                pg.draw.circle(prozor, boja, (x, y), r)

    Која од наредних тврђења су тачна за ову функцију?

    Изабери тачан одговор:


Питање 5.
~~~~~~~~~

.. mchoice:: pg_krug_raste2
    :answer_a: На сваких 100 милисекунди круг се помера за 10 пиксела на десно.
    :feedback_a: Нетачно    
    :answer_b: Круг пролази преко екрана и у сваком проласку мења брзину.
    :feedback_b: Тачно    
    :answer_c: На сваких 100 милисекунди полупречник круга (који је на почетку 20 пиксела) се повећава за 10 пиксела.
    :feedback_c: Нетачно
    :answer_d: Ниједан од осталих понуђених одговора није тачан.  
    :feedback_d: Нетачно    
    :correct: b
    
    Шта је резултат извршавања следећег програма?

    .. code-block:: python

        import pygame as pg, pygamebg
        import random
        prozor = pygamebg.open_window(200,100, "")
        x = 0
        z = 15
        r = 30
        def novi_frejm():
            global x, z
            x += z
            prozor.fill(pg.Color("white"))
            pg.draw.circle(prozor, pg.Color("red"), (x, 50), r)
            if x - r > 200:
                    x = -r
                    z = random.randint(10, 30)
        pygamebg.frame_loop(10, novi_frejm)



    Изабери тачан одговор:
