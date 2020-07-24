Тест - Релативно задавање координата и димензија
================================================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~

.. mchoice:: pomeranje_duzi
    :answer_a: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+100), (x, y2))
    :feedback_a: Нетачно    
    :answer_b: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+100), (x+100, y2+100))
    :feedback_b: Нетачно    
    :answer_c: pygame.draw.line(prozor, pygame.Color("black"), (x, y1+100), (x, y2+100))
    :feedback_c: Нетачно    
    :answer_d: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1), (x+100, y2))
    :feedback_d: Тачно
    :answer_e: pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x+100, y2+100))
    :feedback_e: Нетачно    
    :correct: d
    
    Једна усправна дуж је нацртана наредбом

    .. code-block:: python

        pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x, y2))

    Којом наредбом ћемо нацртати исту такву дуж, померену 100 пиксела удесно?

    Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: cifra_osam
    :answer_a: Секу се
    :feedback_a: Нетачно    
    :answer_b: Додирују се
    :feedback_b: Тачно
    :answer_c: Немају заједничких тачака
    :feedback_c: Нетачно    
    :answer_d: Први се налази унутар другог
    :feedback_d: Нетачно    
    :correct: b
    
    Какав је међусобни положај кругова нацртаних овим наредбама?

    .. code-block:: python

        pygame.draw.circle(prozor, pygame.Color("black"), (x, y-r), r, 1)
        pygame.draw.circle(prozor, pygame.Color("black"), (x, y+r), r, 1)


    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: cifra_jedan
    :answer_a: У тачки "A"
    :feedback_a: Нетачно    
    :answer_b: У тачки "B"
    :feedback_b: Тачно
    :answer_c: У тачки "C"
    :feedback_c: Нетачно    
    :answer_d: У тачки "D"
    :feedback_d: Нетачно    
    :correct: b
    
    Извршавањем следеће две наредбе исцртава се облик цифре 1.

    .. code-block:: python

        pygame.draw.line(prozor, pygame.Color("black"), (x, y+2*a), (x+a, y), 3)
        pygame.draw.line(prozor, pygame.Color("black"), (x+a, y), (x+a, y+4*a), 3)
      
    Где je при томе тачка (x, y)?

        .. image:: ../_images/pg_rel_koord_cifra1.png


    Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: iks_oks_zuta
    :answer_a: (x, y+2*d), (x+3*d, y+2*d)
    :feedback_a: Тачно
    :answer_b: (x, y+d), (x+3*d, y+d)
    :feedback_b: Нетачно    
    :answer_c: (x+2*d, y), (x+2*d, y+3*d)
    :feedback_c: Нетачно    
    :answer_d: (x, y+2*d), (x+2*d, y+2*d)
    :feedback_d: Нетачно    
    :correct: a
    
    Нека је на следећој слици горње лево теме решетке у тачки (x, y), а страница малих квадрата нека је дужине *d*.

        .. image:: ../_images/pg_rel_koord_iksoks_zuta.png

    Које су координате крајева жуте дужи?

    Изабери тачан одговор:
 

Питање 5.
~~~~~~~~~

.. mchoice:: cifra_cetiri
    :answer_a: T1, T3
    :feedback_a: Тачно
    :answer_b: T2, T3
    :feedback_b: Нетачно    
    :answer_c: T1, T4
    :feedback_c: Нетачно    
    :answer_d: T2, T4
    :feedback_d: Нетачно    
    :correct: a
    
    Извршавањем следећих наредби треба да се исцрта облик цифре 4.

    .. code-block:: python

        T1 = (x, y+3*a)
        T2 = (x+3*a, y+3*a)
        T3 = (x+2*a, y)
        T4 = (x+2*a, y+4*a)
        pygame.draw.line(prozor, pygame.Color("black"),  T1,  T2, 1) # vodoravna
        pygame.draw.line(prozor, pygame.Color("black"),  T3,  T4, 1) # uspravna
        pygame.draw.line(prozor, pygame.Color("black"), ___, ___, 1) # kosa

    Шта треба да стоји уместо линија у последњој наредби да би била исцртана четворка?

    Изабери тачан одговор:


Питање 6.
~~~~~~~~~

.. mchoice:: cifra_sest
    :answer_a: T12 = (x+2*a, y); T23 = (x, y+4*a)
    :feedback_a: Нетачно    
    :answer_b: T12 = (x+2*a, y+a); T23 = (x+a, y+2*a)
    :feedback_b: Нетачно    
    :answer_c: T12 = (x, y+a); T23 = (x+a, y+2*a)
    :feedback_c: Тачно
    :answer_d: T12 = (x, y+a); T23 = (x+2*a, y+2*a)
    :feedback_d: Нетачно    
    :correct: c
    
    Допуњавањем датог кода може се нацртати цифра 6 као на слици (без црвених тачака).

        .. image:: ../_images/pg_rel_koord_cifra6.png

    Шта треба да стоји уместо линија?

    .. code-block:: python

        T11 = (x, y)
        T21 = (x+a, y)
        T12 = __________
        T22 = (x+a, y+a)
        T13 = (x, y+2*a)
        T23 = __________
        pygame.draw.line(prozor, pygame.Color("black"), T11, T21, 3) # gornja
        pygame.draw.line(prozor, pygame.Color("black"), T12, T22, 3) # srednja
        pygame.draw.line(prozor, pygame.Color("black"), T13, T23, 3) # donja
        pygame.draw.line(prozor, pygame.Color("black"), T11, T13, 3) # leva
        pygame.draw.line(prozor, pygame.Color("black"), T22, T23, 3) # desna



    Изабери тачан одговор: