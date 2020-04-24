Догађаји - квиз
===============

Питање 1.
~~~~~~~~~

.. mchoice:: drzanje_tastera
    :answer_a: Догађај pygame.KEYDOWN се једном прослеђује функцији за обраду догађаја и то приликом спуштања тастера
    :feedback_a: Тачно
    :answer_b: Догађај pygame.KEYDOWN се за то време стално прослеђује функцији за обраду догађаја
    :feedback_b: Нетачно    
    :answer_c: Систем може да пропусти да проследи догађај pygame.KEYDOWN ако је био заузет у тренутку притиска на тастер
    :feedback_c: Нетачно    
    :correct: a
    
    Ако држимо притиснут неки тастер тастатуре (и нисмо претходно мењали подразумевани начин генерисања догађаја тастатуре)

    Изабери тачан одговор:


Питање 2.
~~~~~~~~~

.. mchoice:: dkeypress
    :multiple_answers:
    :answer_a: pygame.CLICKED
    :feedback_a: Нетачно    
    :answer_b: pygame.KEYDOWN
    :feedback_b: Тачно
    :answer_c: pygame.KEYPRESSED
    :feedback_c: Нетачно    
    :answer_d: pygame.KEYUP
    :feedback_d: Тачно
    :correct: ['b', 'd']
    
    Који догађаји настају када "откуцамо" неко слово на тастатури?

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: dkeydownup2
    :answer_a: Плави круг ће постати и остати видљив након првог клика било ког тастера.
    :feedback_a: Нетачно    
    :answer_b: Плави круг не може бити видљив, јер одмах по исцртавању бива прецртан црвеним кругом.
    :feedback_b: Тачно
    :answer_c: Плави круг ће бити видљив онолико дуго колико је тастер притиснут.
    :feedback_c: Нетачно    
    :correct: b

    Дата је функција за обраду догађаја:

    .. code-block:: python

        def obradi_dogadjaj(dogadjaj):
            if dogadjaj.type == pg.KEYDOWN:
                pg.draw.circle(prozor, pg.Color("blue"), (200, 200), 100)
            pg.draw.circle(prozor, pg.Color("red"), (200, 200), 100)

    Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: dkeydownup1
    :answer_a: Плави круг ће постати и остати видљив након првог притиска на било који тастер.
    :feedback_a: Нетачно    
    :answer_b: Плави круг не може бити видљив, јер одмах по исцртавању бива прецртан црвеним кругом.
    :feedback_b: Нетачно    
    :answer_c: Плави круг ће бити видљив онолико дуго колико је тастер притиснут.
    :feedback_c: Тачно
    :correct: c

    
    Ако је реакција на догађаје дефинисана наредним кодом, шта је потребно да корисник уради да би плави круг био видљив?

    .. code-block:: python

        def obradi_dogadjaj(dogadjaj):
            if dogadjaj.type == pg.KEYDOWN:
                pg.draw.circle(prozor, pg.Color("blue"), (200, 200), 100)
            elif dogadjaj.type == pg.KEYUP:
                pg.draw.circle(prozor, pg.Color("red"), (200, 200), 100)

    Изабери тачан одговор:

Питање 5.
~~~~~~~~~

.. mchoice:: dkeypojedinacno
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a

    Којим од понуђених линија кода се врши провера да ли је притиснут тастер слова A?

    1)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) and (dogadjaj.key == pygame.K_a):  

    2)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) or (dogadjaj.key == pygame.K_a):

    3)
        .. code-block:: python

            if (dogadjaj.type == pygame.K_a):

    Изабери тачан одговор:


