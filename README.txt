Dokumentation f�r Informationsapp.
Projektmedlemmar: Johan, Maria, Tommi, Jonna, Aaron
WU15 - Kurs: ME1580



Produkten:
En webb- och mobilapplikation som ska ge och visa information som �r kopplad till skateprojektet. Detta f�r att underl�tta f�r utst�llningens bes�kare och ge underh�llning genom foto, film och ljud

Produktens syfte:
Att med hj�lp av en digital plattform f�rb�ttra en utst�llning som �r en analog plattform.
 
V�r fr�gest�llning: 
Hur skapar vi en stabil och s�ker DB och ett tillh�rande API?
 
Varf�r:
F�r att skapa f�rst�else f�r arkitekturen och kommunikationen mellan de olika delarna



Projektmetod: Scrumban med inspiration fr�n XP (eXtreme programming).

Scrummaster: Johan



Spr�k vi kommer anv�nda:
?     Python
?    flask ? API

Databas:
?     Mysql
?     Json
?     AJAX

Stack:
?     LAMP // Alla ska s�tta sig in lite mer i detta (Linux, Apache, MySQL, PHP)


Analogt:
?        UML
?        Loggbok/dokumentation
?        ER-modell

Ev. h�rdvara:
?       RPi



Features:
Foto:
? Gallerifunktion
? Koppling till instagram och hashtag-fl�de
? Webbappen kommer visa de senaste 1-5 fotona som laddats upp, ist�llet f�r alla p� en g�ng.
? Mobilappen kommer att ha ett eget galleri d�r bilder kan laddas upp direkt utan att g� genom instagram.
? Lagra bilder i DB tillsammans med namn p� fotografer.


Film: 
? Koppling till YouTube / koppling med Bucketlist-projektet / koppling med webbapplikation?
? Namn p� filmskapare och medverkande i DB.
? L�nk till filmer/intervjuer i DB
? Film uppdelat i tv� kategorier: film/intervju och film/event.

Hitta:
? Google Maps-API
? Karta �ver omr�det d�r utst�llningen kommer vara, med utmarkerade platser samt v�gbeskrivning (gps/orienteringsfunktion).

Schema:
? �Spelschema� d�r varje anv�ndare kan favoritmarkera en speciell h�ndelse.
? Tid, datum, plats, vad.
? Egen, sj�lvst�ndig tabell i DB (tid, datum, plats, vad).
? Information om vilken stad utst�llningen bes�ker under en specifik vecka.


SkateWiki:
? Ordlista med olika slang och uttryck som �r specifika f�r skateboardkulturen.
? Koppling till Bucketlist-projketet? (Nyb�rjarapp-projektet tar detta ist�llet, m�ndag 19/9)

Nyheter:
? Senast inlagda foto, film, intervju (dessa tre kopplas ihop med Foto/Film), samt text och koppling till Twitter.
Vi hade f�rst en id� om att det skulle g� att l�nka till blogginl�gg, men vi �ndrade oss och tog ist�llet med en koppling till Twitter eftersom det k�nns mer relevant f�r oss att anv�nda till detta projektet. Hashtaggen som anv�nds p� instagram kan �ven anv�ndas p� Twitter, vilket underl�ttar.

S�kfunktion:
? S�ka nyckelord p� sidan



Struktur f�r DB - vad som ska lagras.

Media:
Foto:
- ID (primary key)
- URL
- Time/date
- Text (null)
- P_ID (foreign key)
- St_ID (foreign key)
- M_ID (Samma som ID)(PK?)
    
Film:
- ID (primary key)
- URL
- Time/date
- Typ (Film eller foto)

Schema:
- ID (primary key)
- Dagar
- Time/date
- Plats (var p� utst�llningen)
- Text som beskriver vad som ska h�nda
- St_ID (foreign key)

Nyheter:
- ID (pirmary key)
- Text
- M_ID (foreign key) ?
- St_ID (foreign key) ?


Personer:
- ID (primary key)
- F�rnamn
- Efternamn
- Nickname
Denna tabellen kopplas ihop med foto och film.

St�der:
- ID (primary key)
- Stad (Namn p� staden)
- Veckor
- Plats (var i staden)



Funktioner f�r API / Application Programming Interface.

Media:
GET:
URL
P_ID
St_ID
time/date
typ
text


POST:
URL
P_ID
St_ID
typ
text

Schema:
        GET:
        time/date
        plats
        text

        POST:
        time/date
        plats
        text
        St_ID

        PUT:
        time/date
        plats
text

Nyheter:
GET:
        St_ID
        M_ID
        text

        POST:
        text

Personer:
POST:    
F�rnamn
Efternamn
Nickname

St�der:
    GET:
    Stad
    Vecka
    Plats

    POST:
    Stad
    Vecka
    Plats

    PUT:
    Vecka
    Plats



Veckoplanering

Vecka 37 / kursvecka 3 av 9:
VAD?
Vad ska unders�kas - fr�gest�llning? - Fredag 16/9
 Planera sprintar � dela upp i mindre stories - (P�g�ende)


Vecka 38 / kursvecka 4 av 9 / Sprint 0:
VAD?
Prio 1:
Best�mma spr�k - M�ndag 19/9
Utveckla v�ra features - M�ndag 19/9 
Struktur f�r DB, vad som ska lagras - Tisdag 20/9
Funktioner f�r API - Tisdag 20/9

Prio 2:
L�sa/unders�ka DB och API, hur funkar det?
Hur optimeras de?
UML, rita upp
Planera Sprint 1


Vecka 39 / kursvecka 5 av 9 / Sprint 1:
VAD?
Prio 1:



L�ngre fram (kanske v.39/40?):
Ta kontakt med skejtare.
Koppling till Web of Things?
