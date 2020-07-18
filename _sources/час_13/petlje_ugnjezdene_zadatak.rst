Шаховска табла
''''''''''''''

.. questionnote::

   Напиши програм који исцртава шаховску таблу.

Овај задатак је веома сличан оном у ком смо цртали плесни
подијум. Главна разлика је у томе што се боја не одређује насумично,
већ се наизменично смењују црна и бела поља. Можемо позадину целе
табле обојити у бело, а затим исцртати само црна поља. Главни изазов у
овом задатку је како на основу редног броја врсте ``i`` и редног броја
колоне ``j`` одредити да ли се на том месту налази црни или бели
квадрат. Покушај да одредиш ово правило, а ако не успеш, онда погледај
решење.

   
.. activecode:: sahovska_tabla
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/sahovska_tabla.py

   # bojimo pozadinu u belo
   prozor.fill(pg.Color("white"))
                 
   # dimenzije table i polja
   broj_polja = 8
   sirina_polja = sirina / broj_polja
   visina_polja = visina / broj_polja

   # prolazimo kroz sva polja
   for i in range(broj_polja):
       for ???:
           # bojimo crna polja 
           if ???:
               pg.draw.rect(prozor, ???, (i*sirina_polja, j*visina_polja, sirina_polja, visina_polja))

.. reveal:: sahovska_tabla_resenje
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Примети да боја зависи од тога да ли је збир ``i+j`` паран или непаран.
   Дакле у ``if`` наредби треба да стоји услов ``(i+j) % 2 == 1``.
