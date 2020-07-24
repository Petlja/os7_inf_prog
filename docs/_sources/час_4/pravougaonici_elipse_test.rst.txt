Oblici test
===========

.. fillintheblank:: pygame_quiz_crtanje_elipsi_1

    Наведи уређени пар координата центра елипсе нацртане са
    ``pg.draw.ellipse(50, 60, 70, 80)``.

    - :\(85,[ ]*100\): Тачно!
      :\(85,[ ]*[0-9]+\): Пажљивије израчунај координату y.
      :\([0-9]+,[ ]*100\): Пажљивије израчунај координату x.
      :\([0-9]+,[ ]*[0-9]+\): Пажљивије израчунај обе координате.
      :.*: Резултат запиши у облику уређеног пара.


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


.. mchoice:: pygame_quiz_argumenti_crtanja_kruga_1
   :multiple_answers:
   :answer_a: Координате горњег левог темена
   :answer_b: Полупречник
   :answer_c: Координате центра
   :answer_d: Ширина и висина
   :answer_e: Боја
   :correct: b, c, e
   :feedback_a: Координате горњег левог темена се задају код елипсе и правоугаоника
   :feedback_b: Тачно
   :feedback_c: Тачно 
   :feedback_d: Ширина и висина се задају код елипсе и правоугаоника
   :feedback_e: Тачно

   Шта се задаје приликом цртања круга?

.. mchoice:: pygame_quiz_argumenti_crtanja_kruga_2
   :answer_a: pg.draw.circle(prozor, boja, 100, 100, 30, 5)
   :answer_b: pg.draw.circle(prozor, boja, (100, 100), 30, 5)
   :answer_c: pg.draw.circle(prozor, boja, (100, 100, 30, 5))
   :answer_d: pg.draw.circle(prozor, boja, (100, 100), (30, 5))
   :correct: b
   :feedback_a: Покушај поново
   :feedback_b: Тачно
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Да би се нацртао круг са центром у тачки :math:`(100, 100)`,
   полупречника :math:`30` пиксела, дебљине :math:`5` пиксела,
   потребно је извршити позив функције:

.. mchoice:: pygame_quiz_argumenti_crtanja_kruga_3
   :answer_a: у другом случају црта елипса чије су полуосе r и 1.
   :answer_b: у другом случају круг попуњава бојом.
   :answer_c: у првом случају црта круг, а у другом само кружница.
   :answer_d: у првом случају црта само кружница, а у другом круг.
   :correct: c
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново

Провери своје знање о цртању правоугаоника тако што ћеш одговорити на
наредних неколико питања.

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

   Да би се нацртао правоугаоник чије је горње лево теме у тачки
   :math:`(100, 100)`, чија је ширина :math:`30`, а висина :math:`50`
   пиксела, потребно је извршити позив функције:

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
