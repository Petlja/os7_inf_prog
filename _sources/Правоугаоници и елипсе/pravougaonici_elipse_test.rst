5.4. Квиз - правоугаоници и елипсе
==================================

Питање 1.
~~~~~~~~~

.. fillintheblank:: pygame_quiz_crtanje_elipsi_1

    Наведи уређени пар координата центра елипсе нацртане са:
    ``pg.draw.ellipse(50, 60, 70, 80)``.

    - :\(85,[ ]*100\): Тачно!
      :\(85,[ ]*[0-9]+\): Пажљивије израчунај координату y.
      :\([0-9]+,[ ]*100\): Пажљивије израчунај координату x.
      :\([0-9]+,[ ]*[0-9]+\): Пажљивије израчунај обе координате.
      :.*: Резултат запиши у облику уређеног пара: (x, y).


Питање 2.
~~~~~~~~~

.. mchoice:: pygame_quiz_argumenti_crtanja_elipsi_2
   :multiple_answers:
   :answer_a: pg.draw.ellipse(prozor, pg.Color("red"), (100, 100, 40, 30))
   :answer_b: pg.draw.ellipse(prozor, pg.Color("red"), (30,  40,  40, 30))
   :answer_c: pg.draw.ellipse(prozor, pg.Color("red"), (100, 100, 60, 80))
   :answer_d: pg.draw.ellipse(prozor, pg.Color("red"), (50, 70, 80, 60))
   :answer_e: pg.draw.ellipse(prozor, pg.Color("red"), (80, 60, 100, 120))
   :correct: c, d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Тачно
   :feedback_e: Покушај поново

   Круг има свој полупречник, а елипсе имају своје полуосе. Мала
   полуоса је најмање растојање од центра до линије елипсе, а велика
   полуоса је највеће растојање од центра до линије елипсе. Које од
   наредних елипси имају малу полуосу 30, а велику 40 пиксела?


Питање 3.
~~~~~~~~~

.. mchoice:: pygame_quiz_argumenti_crtanja_elipsi_3
   :answer_a: pg.draw.ellipse(prozor, pg.Color("red"), (100, 100, 40, 30))
   :answer_b: pg.draw.ellipse(prozor, pg.Color("red"), (30,  40,  50, 50), 2)
   :answer_c: pg.draw.ellipse(prozor, pg.Color("red"), (100, 100, 60, 80), 3)
   :answer_d: pg.draw.ellipse(prozor, pg.Color("red"), (50, 70, 60, 60))
   :correct: b
   :feedback_a: Покушај поново
   :feedback_b: Тачно
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Којом наредбом се исцртава кружна линија?
   

Питање 4.
~~~~~~~~~

.. mchoice:: pygame_quiz_argumenti_crtanja_pravougaonika_1
   :answer_a: Координате горњег левог темена
   :answer_b: Дебљина
   :answer_c: Ширина
   :answer_d: Висина
   :answer_e: Координате центра
   :correct: e
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново
   :feedback_e: Тачно

   Шта се НЕ задаје приликом цртања правоугаоника?


Питање 5.
~~~~~~~~~

.. mchoice:: pygame_quiz_argumenti_crtanja_pravougaonika_2
   :answer_a: pg.draw.rect(prozor, boja, 100, 100, 30, 50)
   :answer_b: pg.draw.rect(prozor, boja, (100, 100), (30, 50))
   :answer_c: pg.draw.rect(prozor, boja, (100, 100), 30, 50)
   :answer_d: pg.draw.rect(prozor, boja, (100, 100, 30, 50))
   :correct: d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно

   Да би се нацртао правоугаоник испуњен бојом чије је горње лево теме у тачки
   :math:`(100, 100)`, чија је ширина :math:`30`, а висина :math:`50`
   пиксела, потребно је извршити позив функције:


Питање 6.
~~~~~~~~~

.. mchoice:: pygame_quiz_argumenti_crtanja_pravougaonika_3
   :answer_a: pg.draw.rect(prozor, boja, (80, 80, 50, 80))
   :answer_b: pg.draw.rect(prozor, boja, (80, 80), (130, 160))
   :answer_c: pg.draw.rect(prozor, boja, (80, 80, 130, 160))
   :answer_d: pg.draw.rect(prozor, boja, (80, 80), (50, 80))
   :correct: a
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Да би се нацртао правоугаоник чије је горње лево теме у тачки
   :math:`(80, 80)`, а доње десно теме у тачки :math:`(130, 160)`,
   потребно је извршити позив функције:
