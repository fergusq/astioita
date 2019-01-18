================
Tietokantataulut
================

Käyttäjät
=========

::

    CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name TEXT NOT NULL, 
        username TEXT NOT NULL, 
        password TEXT NOT NULL, 
        PRIMARY KEY (id)
    );

Statukset
=========

::

    CREATE TABLE status (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name TEXT NOT NULL, 
        PRIMARY KEY (id)
    );

Kokonaisuudet
=============

::

    CREATE TABLE epic (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name TEXT NOT NULL, 
        PRIMARY KEY (id)
    );

Astiat
======

::

    CREATE TABLE astia (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        title TEXT NOT NULL, 
        description TEXT NOT NULL, 
        creator_id INTEGER NOT NULL, 
        assignee_id INTEGER NOT NULL, 
        status_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(creator_id) REFERENCES account (id), 
        FOREIGN KEY(assignee_id) REFERENCES account (id), 
        FOREIGN KEY(status_id) REFERENCES status (id)
    );

Kokonaisuus-Astia-liitostaulu
=============================

::

    CREATE TABLE IF NOT EXISTS "EpicAstia" (
        epic_id INTEGER, 
        astia_id INTEGER, 
        FOREIGN KEY(epic_id) REFERENCES epic (id), 
        FOREIGN KEY(astia_id) REFERENCES astia (id)
    );