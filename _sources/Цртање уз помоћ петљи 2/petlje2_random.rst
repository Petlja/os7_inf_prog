12.1. Употреба генератора случајних бројева 
===========================================

Функцијом ``random.randint(a, b)`` можемо добити насумично одабран цео
број из интервала :math:`[a, b]`. Ово може бити веома корисно када је
потребно да цртеж испунимо са већим бројем неправилно распоређених
облика. Слично, функцијом ``random.uniform(a, b)`` добијамо насумично
одабрани реалан број из интервала :math:`[a, b]`.

Ноћно небо
''''''''''

.. questionnote::

   Смркнуло се и небо је препуно звездица. Уз звездице се види и млад
   месец. Нацртај такав цртеж.

.. activecode:: nocno_nebo
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/mesec_i_zvezdice.py

   # bojimo pozadinu prozora u crno
   prozor.fill(pg.Color("black"))

   # crtamo 100 nasumično raspoređenih zvezdica
   for i in range(100):
       # nasumično određujemo koordinate
       x = random.randint(0, sirina)
       y = ???
       # crtamo zvezdicu kao mali krug
       ???

   # crtamo mlad mesec pomoću jednog crnog i jednog belog kruga
   pg.draw.circle(prozor, pg.Color("white"), (100, 100),  30)
   pg.draw.circle(prozor, pg.Color("black"), (???, ???),  30)

   
Насумичне боје
''''''''''''''

.. questionnote::

   Украсићемо собу тако што ћемо на плафон окачити 5 балона у
   насумично одабраним бојама. Напиши програм који исцртава овакав
   цртеж, при чему сваки балон црта у облику елипсе.

Генератор случајних бројева можемо употребити и да насумично одаберемо
боју. Довољно је да за сваку од црвене, зелене и плаве компоненте
насумично одаберемо број између 0 и 255. Ово можемо издвојити у
посебну функцију коју ћемо позвати када год нам затреба насумична
боја.

Прикажимо и како да равномерно распоредимо балоне по
плафону. Претпоставимо да треба да распоредимо :math:`n` балона.
Ширину прозора ћемо поделити на :math:`n` једнаких делова. Сваки балон
ћемо закачити на средину њему одговарајућег дела. Ширину једног дела
можемо израчунати тако што ширину прозора поделимо са бројем делова, x
координату левог краја i-тог дела (где бројање креће од 0) добијамо
тако што ширину једног дела помножимо са i, док x координату средине
тог дела (тачке у којој се налази врх балона) добијамо тако што на
леви крај додамо још пола ширине дела. На основу те тачке лако
израчунавамо горњу леву тачку правоугаоника описаног око елипсе (x
координату добијамо тако што од x координате средине поља одузмемо пола
ширине елипсе, док је y координата једнака нули).

.. activecode:: baloni
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/baloni.py

   # funkcija koja na nasumičan način određuje boju
   def nasumicna_boja():
       return (random.randint(0, 255), ???,  random.randint(0, 255))

   # bojimo pozadinu prozora u crno
   prozor.fill(pg.Color("yellow"))

   # crtamo balone
   broj_balona = 5
   sirina_polja = ???
   sirina_balona = 50
   visina_balona = 70
   for i in range(broj_balona):
       centar_polja = i*sirina_polja + sirina_polja / 2
       pg.draw.ellipse(prozor, ???, (???, ???, ???, ???))
