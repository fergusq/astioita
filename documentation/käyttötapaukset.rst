##########################
 Ohjelman käyttötapaukset
##########################

Käyttäjät
=========

Ohjelmaan voi rekisteröityä
---------------------------

Ohjelmaan voi kirjautua sisään
------------------------------

Ohjelmassa on lista käyttäjistä ja heille määrättyjen tehtävien määrättyjen
---------------------------------------------------------------------------

::

    SELECT account.id, account.name, COUNT(astia.id) AS astia_count
    FROM account
    LEFT JOIN astia
    ON astia.assignee_id = account.id
    GROUP BY account.id
    ORDER BY astia_count;

Astiat
======

Käyttäjä voi saada listaukset astioista
---------------------------------------

Ohjelmassa on sivu, joka sisältää listaukset astioista.

::

    SELECT
        astia.id AS astia_id,
        astia.date_created AS astia_date_created,
        astia.date_modified AS astia_date_modified,
        astia.title AS astia_title,
        astia.description AS astia_description,
        astia.creator_id AS astia_creator_id,
        astia.assignee_id AS astia_assignee_id,
        astia.status_id AS astia_status_id 
    FROM astia

Käyttäjä voi luoda uuden astian
-------------------------------

Uusi astia on alussa merkitty tekemättömäksi.

Käyttäjä voi muuttaa astian statusta
---------------------------------------

Käyttäjä voi antaa astialle prioriteetin
----------------------------------------

ei toteutettu :(

Astian voi määrätä käyttäjälle
------------------------------

Astian voi liittää osaksi kokonaisuutta
---------------------------------------

Minimissään tekstikenttä, joka kertoo mistä kokonaisuudesta on kyse

Statukset
=========

Käyttäjä voi lisätä uusia mahdollisia statuksia
-----------------------------------------------

Käyttäjä voi järjestää olemassaolevat statukset
-----------------------------------------------

ei toteutettu :(

Kokonaisuudet
=============

Käyttäjä voi luoda kokonaisuuden
--------------------------------

Käyttäjä voi listata Kokonaisuudet
----------------------------------

::

    SELECT
        epic.id AS epic_id,
        epic.date_created AS epic_date_created,
        epic.date_modified AS epic_date_modified,
        epic.name AS epic_name 
    FROM epic

Raportit
========

ei toteutettu :(

Ohjelma osaa luoda raportin PDF-tiedostona
------------------------------------------

- Raportti sisältää kaavion tehtyjen ja tekemättömien astioiden määristä
- Raportti sisältää listan astioista järjestettynä valmiuden sekä prioriteetin mukaan