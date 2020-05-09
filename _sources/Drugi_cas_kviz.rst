Кругови, правоугаоници, елипсе - квиз
=====================================

Провери своје познавање цртања кургова, правоугаоника и елипси одговарајући на следећа питања. 

Питање 1.
~~~~~~~~~


.. mchoice:: kvadrat
    :answer_a: 200 x 230
    :feedback_a: Нетачно    
    :answer_b: 50 x 40
    :feedback_b: Нетачно    
    :answer_c: 250 x 270
    :feedback_c: Тачно
    :answer_d: 30 x 20
    :feedback_d: Нетачно    
    :correct: c
    
    
    Следећом наредбом се у прозору црта правоугаоник:

    .. code-block:: python

      pygame.draw.rect(prozor, pygame.Color("red"), (200, 230, 250, 270))

    Које су његове димензије?


    Изабери тачан одговор:

Питање 2.
~~~~~~~~~


.. mchoice:: krugkruznica
    :answer_a: Круг попуњен бојом
    :feedback_a: Нетачно    
    :answer_b: Кружница - линија
    :feedback_b: Тачно
    :answer_c: Елипса (која није круг) попуњена бојом
    :feedback_c: Нетачно    
    :answer_d: Елипса - линија (која није кружница)
    :feedback_d: Нетачно
    :correct: b
    
    Шта се исцртава следећом наредбом?

    .. code-block:: python
  
      pygame.draw.ellipse(prozor, pygame.Color("orange"), (120, 80, 40, 40), 1)

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: kvadrat1
    :answer_a: Слика 1
    :feedback_a: Нетачно    
    :answer_b: Слика 2
    :feedback_b: Тачно
    :answer_c: Слика 3
    :feedback_c: Нетачно    
    :answer_d: Слика 4
    :feedback_d: Нетачно    
    :correct: b
    
    Шта ће бити приказано покретањем наредног програма?


    .. code-block:: python
  
      import pygame, pygamebg
      prozor = pygamebg.open_window(800, 600, "")
      prozor.fill(pygame.Color("white"))
      pygame.draw.rect(prozor, pygame.Color("red"), (40, 40, 40, 40))
      pygame.draw.rect(prozor, pygame.Color("blue"), (80, 40, 40, 40))
      pygamebg.wait_loop()

    Упиши ознаку једног од понуђених одговора који сматраш тачним.

    1) .. image:: ../_images/pg_figure_kvadrati11.png

    2) .. image:: ../_images/pg_figure_kvadrati12.png

    3) .. image:: ../_images/pg_figure_kvadrati13.png

    4) .. image:: ../_images/pg_figure_kvadrati14.png


    Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: elipsa_pravougaonik
    :answer_a: pygame.draw.rect(prozor, pygame.Color("red"), (280, 240, 80, 40), 1)
    :feedback_a: Тачно
    :answer_b: pygame.draw.rect(prozor, pygame.Color("red"), (280, 240, 160, 80), 1)
    :feedback_b: Нетачно    
    :answer_c: pygame.draw.rect(prozor, pygame.Color("red"), (280, 240, 360, 280), 1)
    :feedback_c: Нетачно    
    :answer_d: pygame.draw.rect(prozor, pygame.Color("red"), (200, 200, 160, 80), 1)
    :feedback_d: Нетачно    
    :correct: a
    
    Којом наредбом се може исцртати правоугаоник, у који је уписана елипса задата наредбом

    .. code-block:: python
  
      pygame.draw.ellipse(prozor, pygame.Color("black"), (280, 240, 80, 40), 1)



    Изабери тачан одговор:

Питање 5.
~~~~~~~~~


.. mchoice:: krug1
    :multiple_answers:
    :answer_a: Полупречник кружнице је 150.
    :feedback_a: Нетачно    
    :answer_b: Полупречник кружнице је 100.
    :feedback_b: Тачно
    :answer_c: Центар кружнице је у тачки са координатама (100,1).
    :feedback_c: Нетачно    
    :answer_d: Ако су ширина и висина прозора по 150 пиксела, кружница ће бити делимично видљива.
    :feedback_d: Тачно
    :correct: ['b', 'd']

    Следећом наредбом се у прозору црта једна кружница:

    .. code-block:: python
  
      pygame.draw.circle(prozor, pygame.Color("blue"), (150, 150), 100, 1)

    Међу понуђеним тврђењима означи тачна.

Питање 6.
~~~~~~~~~

.. mchoice:: krug2
    :answer_a: Координате центра су (300, 300), а полупречник је једнак 600.
    :feedback_a: Нетачно    
    :answer_b: Координате центра су (300, 300), а полупречник је једнак 300.
    :feedback_b: Нетачно    
    :answer_c: Координате центра су (600, 600), а полупречник је једнак 300.
    :feedback_c: Тачно
    :answer_d: Ниједан од понуђених одговора није тачан.
    :feedback_d: Нетачно    
    :correct: c
    
    
    Нека је квадрат дефинисан следећом наредбом.

    .. code-block:: python
  
      pygame.draw.rect(prozor, pygame.Color("black"), (300, 300, 600, 600), 1)

    Уколико је круг уписан у квадрат, које су координате центра круга, а чему је једнака дужина полупречника круга?

    Изабери тачан одговор:
