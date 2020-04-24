Догађаји - квиз
================

Питање 1.
~~~~~~~~~

.. fillintheblank:: mis_u_rect

   Следећа недовршена функција за обраду догађаја треба да провери да ли је кликнуто мишем на правоугаону слику димензија *w_sl* x *h_sl*, са горњим левим теменом у тачки (*x_sl*, *y_sl*).

   .. code-block:: python

      def obradi_dogadjaj(dogadjaj):
          global __________ # А
          if dogadjaj.type == __________: # B
              x_mis, y_mis = __________ # C
              if (x_sl < x_mis and x_mis < x_sl + w_sl and
                      __________): # D
                  kliknuto_na_sliku = True

   Делови који недостају функцији су набројани у наставку. Упиши редне бројеве делова који недостају функцији у редоследу у ком их треба убацити на места A, B, C, D редом (дакле, прво редни број дела који треба убацити на место A, итд.)

   (1)
      .. code-block:: python
    
         pg.MOUSEBUTTONDOWN

   (2)
      .. code-block:: python
    
         y_sl < y_mis and y_mis < y_sl + h_sl

   (3)
      .. code-block:: python
    
         kliknuto_na_sliku

   (4)
      .. code-block:: python
    
         dogadjaj.pos

   Одговор: |blank|

   - :^\s*3142\s*$: Тачно
     :x: Одговор није тачан.


Питање 2.
~~~~~~~~~

.. mchoice:: prevlacenje
    :answer_a: Да променимо слику када корисник кликне на њу
    :feedback_a: Нетачно    
    :answer_b: Да престанемо да приказујемо слику када корисник кликне на њу
    :feedback_b: Нетачно    
    :answer_c: Да превлачимо мишем слику по прозору
    :feedback_c: Тачно
    :answer_d: Да преврнемо слику наопако када корисник кликне на њу.
    :feedback_d: Нетачно    
    :correct: c
    
    Нека je *sl* слика коју програм у сваком фрејму приказује на позицији (*x_sl*, *y_sl*), а *w_sl* и *h_sl* нека су редом ширина и висина те слике.

    .. code-block:: python
    
        def nov_frejm():
            prozor.fill(pg.Color("skyblue"))
            prozor.blit(sl, (x_sl, x_sl))

    Шта нам омогућава следећа функција за обраду догађаја?

    .. code-block:: python
    
        def obradi_dogadjaj(dogadjaj):
            global x_sl, y_sl, w_sl, h_sl, pr
            if dogadjaj.type == pg.MOUSEBUTTONDOWN:
                x_mis, y_mis = dogadjaj.pos
                if (x_sl < x_mis and x_mis < x_sl + w_sl and
                        y_sl < y_mis and y_mis < y_sl + h_sl):
                    pr = True
            elif dogadjaj.type == pg.MOUSEBUTTONUP:
                pr = False
            elif dogadjaj.type == pg.MOUSEMOTION:
                if pr:
                    x_sl = x_mis - w_sl // 2
                    y_sl = y_mis - h_sl // 2
    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: quit
    :answer_a: pygame.QUIT
    :feedback_a: Тачно
    :answer_b: pygame.EXIT
    :feedback_b: Нетачно    
    :answer_c: pygame.CLOSE
    :feedback_c: Нетачно    
    :correct: a
    
    Догађај затварања прозора је у PyGame библиотеци означен са:

Питање 4.
~~~~~~~~~

.. mchoice:: dkeypojedinacnolevo
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a
    
    Којим од понуђених линија кода се врши провера да ли је притиснут тастер стрелице лево?

    1)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) and (dogadjaj.key == pygame.K_LEFT):  

    2)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) or (dogadjaj.key == pygame.LEFT):

    3)
        .. code-block:: python

            if (dogadjaj.type == pygame.K_LEFT):

    Изабери тачан одговор:

Питање 5.
~~~~~~~~~

.. mchoice:: timer
    :answer_a: pg.time.set_timer
    :feedback_a: Тачно
    :answer_b: pg.USEREVENT.timer_set
    :feedback_b: Нетачно    
    :answer_c: pg.clock.set_time
    :feedback_c: Нетачно    
    :correct: a
    
    Помоћу које функције уклључујемо тајмер?
    
    Изабери тачан одговор:

