# Tag 11 · 🎰 Poker-Mathematik I 🔴

**Ziel:** Outs, Equity, Pot Odds und EV so verinnerlichen, dass du am Tisch in Sekunden entscheiden kannst — und die "Rule of 4 and 2" nicht nur anwendest, sondern *herleiten* kannst.

**Zeitbudget:** Kern ~2–3 h (Teil A + B), Stretch ~1 h (Teil C + D).

---

## Teil A — Werkzeugkasten (~30 min lesen & nachvollziehen)

Nimm dir das hier nicht als Auswendiglern-Stoff, sondern rechne jede Formel einmal an einem Mini-Beispiel nach.

### A.1 Notation (halt dich konsequent daran, sonst verrechnest du dich)

| Symbol | Bedeutung |
|---|---|
| `P` | Pot **nachdem** der Gegner gesetzt hat (inkl. seines Bets) |
| `C` | Betrag, den du callen musst |
| `o` | Anzahl deiner Outs |
| `E` | deine Equity (Gewinnwahrscheinlichkeit), als Dezimalzahl |

### A.2 Pot Odds → benötigte Equity

```
E_benötigt = C / (P + C)
```

Das ist der Break-even-Punkt. Liegt deine echte Equity darüber → Call ist +EV.

### A.3 EV eines Calls

```
EV(Call) = E · P  −  (1 − E) · C
```

Gewinnst du, nimmst du `P` mit (dein eigener Call ist da noch nicht drin — den zahlst du ja aus deinem Stack). Verlierst du, sind `C` weg.

> **Sanity-Check, den du einmal machen solltest:** Setze `E = C/(P+C)` in die EV-Formel ein und zeig, dass `EV = 0` rauskommt. Wenn das aufgeht, hast du die beiden Formeln als *dasselbe* verstanden und musst nie wieder überlegen, welche du brauchst.

### A.4 Exakte Equity aus Outs

Nach dem Flop sind **47** Karten unbekannt (52 − 2 Hole − 3 Board), nach dem Turn **46**.

| Situation | Exakte Formel |
|---|---|
| 1 Karte kommt (Flop → Turn) | `o / 47` |
| 1 Karte kommt (Turn → River) | `o / 46` |
| 2 Karten kommen (Flop → River) | `1 − (47−o)/47 · (46−o)/46` |

**Wichtiger Denkfehler, den fast alle machen:** Die 2-Karten-Formel gilt nur, wenn du garantiert beide Karten siehst — also praktisch nur **all-in**. Wenn der Gegner am Turn nochmal setzen kann, rechnest du am Flop mit der **1-Karten**-Zahl (plus Implied Odds, siehe A.6).

### A.5 Die "Rule of 4 and 2"

```
2 Karten kommen:  E ≈ o · 4 %
1 Karte kommt:    E ≈ o · 2 %
```

### A.6 Implied Odds

Wenn der direkte Call −EV ist, kann er trotzdem richtig sein, falls du bei einem Treffer später noch Chips gewinnst. Sei `X` der Betrag, den du im Schnitt zusätzlich gewinnst:

```
E · (P + X)  −  (1 − E) · C  =  0     →     nach X auflösen
```

`X` ist dann die Frage: *"Kriege ich das realistisch aus dem Gegner raus?"*

---

## Teil B — Die 10 Spots (Kernaufgabe)

**Für jeden Spot berechne und notiere:**

1. Outs `o` (welche Karten genau? Aufzählen, nicht raten)
2. Exakte Equity (Formel aus A.4)
3. Näherung nach Rule of 4/2 — und die **Abweichung** in Prozentpunkten
4. Benötigte Equity aus den Pot Odds
5. `EV(Call)` in Chips
6. Entscheidung: **Call / Fold** + ein Satz Begründung

Alle Spots: No-Limit Hold'em, Heads-up, du bist Hero.

---

### Spot 1 — Der Standard
**Hero:** A♠ 7♠ · **Flop:** K♠ 9♠ 2♥
**Pot:** 100 · Gegner setzt **25**. Stacks tief.

---

### Spot 2 — Open-Ender gegen großen Bet
**Hero:** 8♦ 9♦ · **Flop:** 7♣ T♠ 2♥
**Pot:** 60 · Gegner setzt **30**.

---

### Spot 3 — Gutshot
**Hero:** Q♠ J♠ · **Flop:** 9♥ 8♦ 2♣
**Pot:** 50 · Gegner setzt **20**.

> Zusatzfrage: Zähl einmal *mit* deinen Overcards (Q, J) als Outs und einmal ohne. Wann darfst du Overcards als Outs zählen, wann sind sie wertlos?

---

### Spot 4 — Turn, nur noch eine Karte
**Hero:** A♣ 5♣ · **Board:** K♣ 8♣ 3♦ **7♥** (Turn)
**Pot:** 200 · Gegner setzt **50**.

> Achtung: unbekannte Karten = 46, nicht 47.

---

### Spot 5 — Combo-Draw, All-in
**Hero:** J♥ T♥ · **Flop:** 9♥ 8♣ 2♥
**Pot:** 100 · Gegner geht **all-in mit 100**, du hast genau 100 hinter dir.

> Hier zählt die 2-Karten-Formel (all-in = du siehst Turn und River garantiert). Pass beim Outs-Zählen auf **Doppelzählung** auf: Q♥ und 7♥ sind sowohl Flush- als auch Straight-Outs.
> Rechne hier die Rule of 4 bewusst aus und schau dir den Fehler an — er ist groß.

---

### Spot 6 — Implied Odds
**Hero:** 5♥ 6♥ · **Flop:** 7♣ 8♦ K♠
**Pot:** 40 · Gegner setzt **30**. Beide haben noch **500** hinter sich.

Zusätzliche Frage: **Wie viel `X` musst du im Schnitt an Turn+River zusätzlich gewinnen, damit der Call break-even wird?** Und dann ehrlich: Ist das realistisch gegen einen Gegner, der bei einer 4 oder 9 auf dem Board Alarm schlägt?

---

### Spot 7 — Semi-Bluff mit Fold Equity
**Hero:** A♠ 4♠ · **Flop:** K♠ 9♠ 3♦
**Pot:** 100 · Gegner checkt. Du überlegst, **100 all-in** zu setzen (beide haben 100).

Nimm an, der Gegner foldet in **50 %** der Fälle. Wenn er callt, hast du ~35 % Equity.

Berechne:
- `EV(Shove)` = P(Fold) · Pot + P(Call) · EV(gecallt)
- `EV(Check-behind)` ≈ 0 als Vergleichsbasis
- Ab welcher Fold-Häufigkeit ist der Shove profitabel?

> Das ist der Moment, an dem du merkst: Poker ist nicht nur "hab ich die besseren Karten", sondern **zwei Wege zu gewinnen**.

---

### Spot 8 — Set-Mining (Preflop)
**Hero:** 5♣ 5♦ im Big Blind. Gegner raist auf **30**, du musst **20** callen. Pot danach: **65**. Stacks: **1000**.

- Berechne exakt: **Wie oft floppst du ein Set (oder besser)?** Tipp: `1 − C(48,3)/C(50,3)`, oder als Kettenwahrscheinlichkeit über drei Karten.
- Direkte Pot Odds sagen: Fold. Wie viel musst du bei einem Set im Schnitt gewinnen, damit der Call break-even ist?
- Daraus folgt die bekannte Faustregel "**Implied Odds von ca. 7,5 : 1**" — leite sie aus deiner Rechnung her.

---

### Spot 9 — Viele Outs, aber der Turn ist nicht geschenkt
**Hero:** A♦ K♦ · **Flop:** Q♦ J♠ 5♦
**Pot:** 120 · Gegner setzt **120** (Pot-Size-Bet). Stacks tief, es kann am Turn nochmal gesetzt werden.

- Zähl die Outs sauber (Flush-Outs, Straight-Outs, Overpair-Outs — welche überschneiden sich?)
- Rechne die Equity **einmal für 2 Karten** und **einmal für 1 Karte**.
- Welche der beiden ist hier die richtige Zahl für die Entscheidung? Begründe.

> Das ist der wichtigste konzeptionelle Spot des Tages.

---

### Spot 10 — River: der Bluffcatcher
**Hero:** 9♠ 9♦ · **Board:** A♣ 7♦ 4♥ 2♠ K♥ (River)
**Pot:** 200 · Gegner setzt **100**.

Du schlägst jeden Bluff und verlierst gegen jede Value-Hand — deine Equity ist also nicht mehr "Outs", sondern **wie oft der Gegner blufft**.

- Wie oft muss er mindestens bluffen, damit dein Call break-even ist?
- Er hat 12 Value-Kombos in seiner Range. Wie viele Bluff-Kombos braucht er mindestens?
- Berechne die **MDF** (Minimum Defense Frequency): `MDF = Pot / (Pot + Bet)`. Was sagt die dir über *seine* Seite der Rechnung?

---

## Teil C — Die Herleitung (Kernaufgabe, nicht optional!)

Der Challenge-Text sagt explizit: *verstehen* **und** *herleiten, warum sie funktioniert*.

### C.1 Woher kommt die "2"?
Zeig, warum `o/47 ≈ o · 2 %` gilt. (Hinweis: `1/47 ≈ 1/50 = 2 %`.) In welche Richtung liegt die Regel systematisch daneben — zu hoch oder zu niedrig? Warum?

### C.2 Woher kommt die "4"?
Naiv würde man sagen: zwei Chancen à 2 % pro Out, also `o · 4 %`. Aber das ist eine **Vereinigung zweier Ereignisse**:

```
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```

Der Term `P(A ∩ B)` — "ich treffe an *beiden* Straßen" — wird beim einfachen Verdoppeln unterschlagen. Deshalb überschätzt die Regel bei vielen Outs. Zeig das rechnerisch.

### C.3 Die Fehlertabelle
Fülle sie aus (exakt vs. Näherung), Flop, 2 Karten kommen:

| Outs | Exakt (%) | Rule of 4 (%) | Fehler (pp) |
|---|---|---|---|
| 4 | 16,46% | 16 | 0,46% |
| 8 | 31,45% | 32 | 0,55% |
| 9 | 34,97% | 36 / 35 | 1,03% |
| 12 | 44,96% | 48 / 44 | 3,04% |
| 15 | 54,12% | 60 / 53 | 5,58% |

Dann: **Ab wie vielen Outs wird der Fehler unakzeptabel?** Es gibt eine gängige Korrektur — *"bei mehr als 8 Outs ziehe (Outs − 8) ab"*. Prüfe an deiner Tabelle, wie gut die funktioniert.

---

## Teil D — 20 Hände am Tisch (Kernaufgabe, Praxis)

**Nur Play Money.** Ziel ist nicht Gewinn, sondern bewusste Anwendung.

Führe während des Spiels ein Mini-Log. Für jede Hand, in der du eine Draw-Entscheidung hattest:

```
Hand #  | Meine Hand | Board | Pot | Bet | Outs | Equity | E_benötigt | Entscheidung | War sie richtig?
```

**"War sie richtig?"** heißt: war die *Entscheidung* richtig, nicht das *Ergebnis*. Ein +EV-Call, der verliert, ist eine gute Entscheidung. Wenn du das durchhältst, hast du den mit Abstand wertvollsten Transfer des Tages gemacht — das gilt genauso für Trading (Tag 35) und für jede Entscheidung unter Unsicherheit.

**Wo spielen (kostenlos, ohne Echtgeld):**
- **PokerStars Play** — reines Play-Money-Produkt, App & Browser
- **Replay Poker** — Browser, kein Download, gute Anfänger-Tische
- **PokerTH** — Open Source, offline gegen Bots, ideal wenn du in Ruhe rechnen willst

---

## 🔧 Materialien & Tools

**Equity-Rechner (zum *Prüfen*, nicht zum Ersetzen deiner Handrechnung!)**
- **Equilab** (kostenlos, Windows) — der Standard für Hand-vs-Hand und Hand-vs-Range
- **ProPokerTools Odds Oracle** (`propokertools.com/simulations`) — browserbasiert, auch für Ranges
- **CardPlayer Poker Odds Calculator** — schnell, browserbasiert, für einzelne Spots

> Regel für heute: **erst selbst rechnen, dann prüfen.** Sonst lernst du das Tool statt der Mathematik.

**Zum Nachlesen**
- *The Mathematics of Poker* — Bill Chen & Jerrod Ankenman (das seriöse Buch, mathematisch anspruchsvoll)
- *Applications of No-Limit Hold'em* — Matthew Janda (Ranges & Frequenzen, bereitet Tag 38 vor)
- Wikipedia: "Poker probability" — die Kombinatorik-Tabellen zum Gegenrechnen

**Kombinatorik-Auffrischung**
Wenn dir Teil C oder Spot 8 zäh vorkommt: das ist genau der Stoff von **Tag 10**. Blätter zurück in deine Aufgaben — `C(n,k)` und bedingte Wahrscheinlichkeit sind hier das ganze Werkzeug.

---

## 📦 Deliverable

Ins Repo unter `tag11-poker/`:

1. `spots.md` — 10 durchgerechnete Spots mit allen 6 Punkten aus Teil B
2. `herleitung.md` — Teil C inkl. ausgefüllter Fehlertabelle
3. `handlog.md` — deine 20 Play-Money-Hände
4. *(Stretch)* `outs.py` — ein kleines Script, das aus `outs` und `Straße` die exakte Equity ausgibt und die Rule-of-4/2-Näherung danebenstellt

**Punkte:** 10 (Kern) · +5 (Stretch-Script) · +3 (committet) · +5 Grit, falls du bei Spot 9 oder der C.2-Herleitung wirklich gestockt hast

---

## 🔮 Anschluss

- **Tag 31 (Monte Carlo):** Du simulierst genau diese Equities mit 100.000 Runs — und vergleichst mit dem, was du heute per Hand gerechnet hast. Heb deine Zahlen also gut auf.
- **Tag 21 (Kelly):** Heute lernst du, *ob* eine Wette gut ist. An Tag 21 lernst du, *wie viel* du setzen darfst.
- **Tag 38 (Ranges & GTO):** Du nimmst 15 deiner heutigen Hände nochmal auseinander — dann nicht mehr "meine Karten gegen seine Karten", sondern gegen seine ganze Range.

---

<details>
<summary><b>🔒 Lösungsschlüssel — erst öffnen, wenn du alle 10 Spots gerechnet hast</b></summary>

Nur Endergebnisse. Wenn eine Zahl abweicht, such den Fehler selbst — das ist der lehrreiche Teil.

| Spot | Outs | Equity | E_benötigt | EV(Call) | Entscheidung |
|---|---|---|---|---|---|
| 1 | 9 | 19,1 % (1 Karte) | 16,7 % | ≈ +3,7 | **Call** |
| 2 | 8 | 17,0 % (1 Karte) | 25,0 % | ≈ −13,0 | **Fold** |
| 3 | 4 | 8,5 % (1 Karte) | 22,2 % | ≈ −12,3 | **Fold** |
| 4 | 9 | 19,6 % (1 Karte, /46) | 16,7 % | ≈ +8,7 | **Call** |
| 5 | 15 | 54,1 % (2 Karten) | 33,3 % | ≈ +62,3 | **Call** |
| 6 | 8 | 17,0 % (1 Karte) | 30,0 % | ≈ −13,0 direkt | X ≈ 76 nötig |
| 7 | 9 | 35 % gecallt | — | ≈ +52,5 (Shove) | **Shove**; break-even ab ≈ 4,8 % Folds |
| 8 | — | 11,8 % Set am Flop | 23,5 % (20/85) | — | Call nur mit Implied Odds ≈ 7,5:1 |
| 9 | 12 | 45,0 % (2 K.) / 25,5 % (1 K.) | 33,3 % | 1-Karten-Zahl zählt → knapp **−** | siehe Hinweis |
| 10 | — | Bluff-Anteil ≥ 25 % | 25,0 % | — | ≥ 4 Bluff-Kombos; MDF = 66,7 % |

**Hinweise zu den Knackpunkten:**
- **Spot 5:** Rule of 4 sagt 60 %, exakt sind 54,1 % — 6 Prozentpunkte daneben. Mit der Korrektur (60 − 7) landest du bei 53 %, deutlich besser.
- **Spot 9:** Mit 1 Karte (25,5 %) liegst du unter den benötigten 33,3 % → direkter Call ist −EV. Rettbar wird er nur über Implied Odds oder wenn du stattdessen selbst aggressiv wirst (Semi-Bluff-Raise, vgl. Spot 7). Der Fehler, hier mit 45 % zu rechnen, kostet auf Dauer sehr viel Geld.
- **Spot 7:** Break-even-Fold-Frequenz: löse `f · 100 + (1−f) · 5 = 0` nach `f`. Dass die Zahl so niedrig ist, liegt daran, dass der Shove auch gecallt schon leicht +EV ist.

</details>
