Varaston tiivis yleiskatsaus – Odoo 19
====================================

Tekijä: Devoca Oy

Versio 19.0.1.0.2 lisää moduulin tekijätiedon Odoon moduulitietoihin.

Moduuli pienentää Varasto > Yleiskatsaus -näkymän kortteja:

* Pylväskaaviot piilotetaan. Näkymän tarvitsema kaaviotieto ladataan edelleen.
* Korttien tavoiteleveys pienenee 480 pikselistä 360 pikseliin.
  Odoo sovittaa todellisen leveyden käytettävissä olevaan tilaan.
* Korttien sisävälejä ja otsikoita pienennetään.
* Lukumäärälinkkien sisennykset ja varattu tyhjä korkeus poistetaan.
* Nykyiset toimintopainikkeet, lukumäärät ja kortin valikko säilyvät.
* Puhelimella painike ja lukumäärät sijoitetaan allekkain.

Asennus
-------

1. Pura ZIP. Kopioi ``stock_overview_compact`` palvelimen omaan
   lisämoduulihakemistoon, joka on Odoon ``addons_path``-asetuksessa.
2. Käynnistä Odoo-palvelu uudelleen.
3. Aktivoi kehittäjätila, avaa Sovellukset ja päivitä sovellusluettelo.
4. Poista tarvittaessa Sovellukset-suodatin ja etsi
   ``Compact Inventory Overview``. Asenna moduuli.
5. Päivitä selain ja avaa Varasto > Yleiskatsaus.

Vaihtoehtoinen asennus ylläpitäjälle:

::

    odoo-bin -c /polku/odoo.conf -d TIETOKANTA -i stock_overview_compact --stop-after-init

Palvelun tulee käyttää samaa asetustiedostoa ja moduulihakemistoa.
Asennetun moduulin päivityksessä käytä ``-u stock_overview_compact``.

Korjauspäivitys 19.0.1.0.1
------------------------

Ensimmäisessä versiossa kaaviokenttä poistettiin kokonaan näkymästä.
Odoon dashboard-renderöijä tarvitsee kentän arvon myös ilman näkyvää
kaaviota. Tästä aiheutui OwlError ja virhe
``r.data.kanban_dashboard_graph.includes``.

Korjatussa versiossa kenttä ilmoitetaan kanban-näkymän ladattavaksi
taustakentäksi. Vain kortissa näkyvä kaaviokomponentti poistetaan.

Päivitä olemassa oleva asennus näin:

1. Korvaa palvelimen vanha ``stock_overview_compact``-hakemisto tämän
   paketin saman nimisellä hakemistolla.
2. Päivitä moduuli tietokantaan. Pelkkä tiedostojen kopiointi tai palvelun
   uudelleenkäynnistys ei päivitä XML-näkymää.
   Ylläpitäjä voi käyttää alla olevaa komentoa Odoon normaalin
   ylläpitomenettelyn mukaisesti, tai käynnistää palvelun uudelleen ja
   valita moduulin Sovellukset-sivulta Päivitä / Upgrade.

::

    odoo-bin -c /polku/odoo.conf -d TIETOKANTA -u stock_overview_compact --stop-after-init

3. Käynnistä normaali Odoo-palvelu tarvittaessa ja lataa selain uudelleen.
4. Varmista Varaston yleiskatsauksesta, että kortit latautuvat ilman
   OwlError-virhettä ja kaaviot pysyvät piilossa.

Moduulia ei tarvitse poistaa ja asentaa uudelleen.

Käyttö ja palautus
-----------------

Tiivistys on automaattisesti käytössä kaikille käyttäjille tässä
yleiskatsausnäkymässä. Erillistä käyttäjäkohtaista valintaa ei ole.
Poistamalla moduulin asennuksen alkuperäinen näkymä palautuu.
Selaimen päivitys voi olla tarpeen ulkoasutiedostojen vaihtumisen jälkeen.

Yhteensopivuus
-------------

Tarkoitettu Odoo 19.0:n vakio-stock-moduulin näkymään
``stock.stock_picking_type_kanban``. Käyttö vaatii ympäristön, jossa
omia lisämoduuleja voidaan asentaa, esimerkiksi oma palvelin tai Odoo.sh.
Odoo Online ei tue tämän palvelinmoduulin asennusta.

Moduuli perii vakionäkymän ja lisää rajatun CSS-tiedoston.
Se ei lisää tietomalleja, käyttöoikeuksia tai tietokantakenttiä.
Muut samaa näkymää muuttavat lisämoduulit voivat edellyttää yhteensovitusta.
Jos käytössä on muu Odoon pääversio, yhteensopivuus tulee tarkistaa erikseen.

Tarkistukset
------------

Pakettia laadittaessa XML-kohdistukset on tarkistettu Odoon julkisen
19.0-haaran alkuperäiseen näkymään. Korjauspäivityksessä on lisäksi
tarkistettu, että yhdistetyssä näkymässä kaaviokenttä on mukana
ladattavana taustakenttänä, näkyvä kaaviokomponentti puuttuu ja alkuperäiset
toimintolinkit säilyvät. Manifestin rakenne, tiedostoviittaukset
ja ZIP-paketti on tarkistettu. Varsinaista asennusta Odoo-tietokantaan
ei ole tässä ympäristössä tehty.

Tarkista testiympäristössä asennuksen jälkeen:

* Kaaviot poistuvat ja kortteja mahtuu aiempaa enemmän näytölle.
* Vastaanottojen, toimitusten ja sisäisten siirtojen painikkeet toimivat.
* Odottaa-, Myöhässä-, Jälkitoimitukset- ja Toiminta-linkit toimivat.
* Tyhjät kortit, pitkät nimet, suuret luvut ja mobiilileveys näkyvät oikein.
* Varastoittain ryhmittely ja korttien valikot toimivat.
* Muut korttinäkymät säilyttävät alkuperäisen ulkoasunsa.

Lähde: https://github.com/odoo/odoo/tree/19.0/addons/stock

Lisenssi: LGPL-3
