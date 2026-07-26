# Die 15 Aufgaben — von warm bis schmerzhaft

Alle von Hand rechnen, Bruchform stehen lassen (Dezimalzahlen nur zum Vergleich). Notiere zu jeder Aufgabe: (a) Was ist Ω? (b) Welche Formel? (c) Rechnung. (d) Sanity-Check.

## Ereignisraum & Grundregeln

1. Zwei faire Würfel werden geworfen. Berechne P(Augensumme = 7) und P(beide Würfel zeigen dieselbe Zahl).
2. Aus einem Standard-Skatblatt (32 Karten, 4 Farben à 8 Werte) wird eine Karte gezogen. Berechne P(Herz ∪ Bube) — Additionsregel mit Schnittmenge sauber anwenden.
3. Eine faire Münze wird 4-mal geworfen. Berechne P(mindestens einmal Kopf) über das Gegenereignis. Warum ist der Umweg über das Komplement hier praktisch?

## Kombinatorik

4. Auf 8 Stühlen sollen 8 Personen platziert werden. (a) Wie viele Sitzordnungen gibt es insgesamt? (b) Wie viele, wenn zwei bestimmte Personen (Alice & Bob) nebeneinander sitzen müssen?
5. Aus einem 12-köpfigen Kurs wird eine 5er-Arbeitsgruppe zufällig gezogen. (a) Anzahl möglicher Gruppen? (b) Wie viele davon enthalten dich?
6. Lotto 6 aus 49. Berechne (a) P(6 Richtige) und (b) P(genau 3 Richtige). Bei (b): C(6,3) · C(43,3) / C(49,6) — verstehe warum.
7. Beim Draw-Poker werden 5 Karten aus 52 gezogen. Berechne P(Flush) = alle 5 Karten dieselbe Farbe (Straight Flushes eingeschlossen). Formel: 4·C(13,5) / C(52,5). Vergleiche mit deinem Bauchgefühl.

## Bedingte Wahrscheinlichkeit

8. Aus 52 Karten werden nacheinander zwei ohne Zurücklegen gezogen. Berechne P(beide Asse). Einmal direkt (Multiplikationssatz), einmal kombinatorisch (C(4,2)/C(52,2)) — die Ergebnisse müssen identisch sein.
9. Urne mit 5 roten und 3 blauen Kugeln. Es werden 3 Kugeln ohne Zurücklegen gezogen. Berechne P(genau 2 rote). Löse zweimal: (a) über Baumdiagramm, (b) hypergeometrisch mit Binomialkoeffizienten.
10. Junge-Junge-Problem. Eine Familie hat zwei Kinder. Du erfährst: mindestens eines ist ein Junge. Berechne P(beide Jungen | mindestens ein Junge). Achtung — die intuitive Antwort ist falsch. Schreib Ω explizit auf.

## Satz von Bayes

11. Bayes-Warmup. Urne 1 enthält 7 rote & 3 weiße Kugeln, Urne 2 enthält 4 rote & 6 weiße. Du wählst zufällig eine Urne (50/50) und ziehst eine Kugel. Sie ist rot. Berechne P(Urne 1 | rot) und P(Urne 2 | rot). Summe = 1?
12. Ziegenproblem (Monty Hall). Drei Türen, hinter einer ist das Auto, hinter zweien eine Ziege. Du wählst Tür 1. Der Moderator (der weiß, wo das Auto steht) öffnet Tür 3 und zeigt eine Ziege. Berechne P(Auto hinter 1 | Moderator öffnet 3) und P(Auto hinter 2 | Moderator öffnet 3) formal mit Bayes. Welche Strategie ist besser — und um welchen Faktor?
13. Medizinischer Test mit Basisrate. Eine seltene Krankheit hat eine Prävalenz von 0,1 % in der Bevölkerung. Der Test hat eine Sensitivität von 99 % (P(positiv | krank) = 0,99) und eine Spezifität von 95 % (P(negativ | gesund) = 0,95). Eine zufällig getestete Person ist positiv. Berechne P(krank | positiv). Das Ergebnis wird dich überraschen — genau das ist die Lektion. Erkläre in einem Satz, warum die Antwort so weit von 99 % entfernt ist. Das ist die Bayes-Antwort, die du am Ende erklären können sollst (Deliverable).

## Anwendungen & Schluss-Bosse

14. Geburtstagsparadoxon. In einer Gruppe von n Personen — ab welchem n ist P(mindestens zwei am selben Tag Geburtstag) > 50 %? Berechne die Wahrscheinlichkeit für n = 10, 23, 30. Nutze das Komplement (kein Match bei allen Paaren) und ignoriere Schaltjahre. Bonus: Warum ist die Antwort so viel kleiner als die meisten schätzen?
15. Bayes-Update mit mehreren Evidenzen (Mini-Spam-Filter, Preview auf Tag 41). Prior: P(Spam) = 0,3. Eine Mail enthält das Wort "Gewinn" mit P("Gewinn" | Spam) = 0,4 und P("Gewinn" | Ham) = 0,02. (a) Berechne P(Spam | "Gewinn"). (b) Dieselbe Mail enthält zusätzlich das Wort "sofort" mit P("sofort" | Spam) = 0,3 und P("sofort" | Ham) = 0,01. Update deinen Posterior aus (a) mit dieser zweiten Evidenz unter der Annahme, dass die Wörter bedingt unabhängig sind (Naive-Bayes-Annahme). Wo könnte diese Annahme in der Realität brechen?