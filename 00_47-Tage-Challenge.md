# 🎯 Die 47-Tage-Challenge
### Vom Abi in die Cybersecurity — dein Sommer als Trainingslager

> **Ziel:** Jeden Tag etwas Neues lernen oder etwas Kreatives schaffen. Schwierigkeit **mittel bis hoch** — du sollst regelmäßig an deine Grenzen stoßen, aber nicht ausbrennen.
> **Format:** Manche Tage sind Solo-Sprints, andere Themen ziehen sich über mehrere Tage. Einige Tage sind per Würfel **zufällig**.

---

## 📖 Wie du das hier benutzt

**Schwierigkeitsgrade**
- 🟢 **mittel** – fordernd, aber machbar
- 🟡 **mittel-hoch** – du wirst konzentriert arbeiten müssen
- 🔴 **hoch** – hier fängt es an wehzutun (im guten Sinne)
- ⚫ **extrem** – Grenzerfahrung. Wenn du hier nicht mindestens einmal fluchst, hast du es zu leicht genommen.

**Zeit:** Jeder Tag hat eine *Kernaufgabe* (~2–3 h) und optional einen **Stretch (Limit-Push)** obendrauf. Wenn du weniger Zeit hast: nur die Kernaufgabe. Mehr Zeit/Ehrgeiz: Stretch.

**🎲 Zufalls-Tage:** Bei diesen Tagen würfelst du das Thema aus. Echter Würfel oder im Terminal:
```bash
python -c "import random; print(random.randint(1,6))"
```

**Spielregeln**
1. **Beweis-Pflicht:** Jeder Tag hat ein *Deliverable* — Code, eine Zeichnung, eine Notiz, ein gelöstes Level. Kein "hab ich im Kopf gemacht". Alles kommt in einen Ordner / ein GitHub-Repo.
2. **Tausch erlaubt:** Du darfst zwei Tage gegeneinander tauschen, wenn dir grad nach was anderem ist. Aber nicht wegskippen.
3. **Ein echter Ruhetag pro Woche** ist keine Schwäche, sondern Teil des Plans. Leg ihn auf ein 🟢 oder das Buffer-Feld.
4. **Log führen:** Am Ende steht eine Log-Vorlage. 2 Sätze pro Tag reichen.

**⚙️ Setup vorab (Tag 1 erledigt das):** Python 3, Git, ein Editor (VS Code), eine Linux-Umgebung (Linux nativ, WSL2 unter Windows, oder Terminal unter macOS), ein GitHub-Account.

---

## 🧩 Die Tracks (Farbcode in der Übersicht)

| Track | Worum es geht |
|---|---|
| 💻 **Code** | Klassisches Programmieren, Datenstrukturen, Algorithmen, C |
| 🔐 **Security** | Kryptographie, CTFs, Hacking (nur legal!), Netzwerke |
| 🔢 **Zahlen** | Kopfrechnen, Überschlagen, Statistik, Wahrscheinlichkeit |
| 🎰 **Edge** | Poker, Gambling-Mathematik, Quant/Trading, Kelly |
| 🔧 **Hardware** | Arduino, Raspberry Pi |
| 🎨 **Kreativ** | Zeichnen, Malen, Musik am Computer |
| 🔎 **Neugier** | Detektivarbeit/OSINT, "Wie funktioniert das?" |

---

## 🔁 Tägliches Warmup (optional, ~15 min, JEDEN Tag)

Das läuft parallel zu allem und trainiert zwei deiner Interessen kontinuierlich statt nur an Einzeltagen:

- **Ungerade Tage:** Kopfrechnen. 5 min [arithmetic.zetamac.com](https://arithmetic.zetamac.com) (Default-Settings) + notiere deinen Score.
- **Gerade Tage:** Speed Reading. 10 min gezielte Übung (siehe Tag 15) + Text danach kurz in eigenen Worten zusammenfassen (Comprehension-Check).

> Diese zwei Zahlen (Zetamac-Score + Lese-WPM) trackst du und vergleichst sie am Tag 47 mit Tag 1. Das ist dein sichtbarer Fortschritt.

---

# 📅 Der Plan

## Phase 1 — Fundament & Kalibrierung (Tag 1–10)

### Tag 1 · 💻 Setup & Baseline 🟢
- **Ziel:** Werkzeug scharf machen, Startwerte messen.
- **Aufgabe:** Dev-Umgebung aufsetzen (Python, Git, VS Code, Linux/WSL, GitHub-Repo `47-days` anlegen). Dann Baselines nehmen: 3× Zetamac-Score, 1× Speed-Reading-Test mit WPM **und** Verständnisfragen ([z.B. readingsoft.com](https://www.readingsoft.com) oder ein Buchkapitel + selbst Fragen).
- **Deliverable:** Repo online, `baseline.md` mit deinen Startzahlen.

### Tag 2 · 🔐 Linux & Kommandozeile – Bootcamp 🟡
- **Ziel:** Die Shell soll sich nicht mehr fremd anfühlen.
- **Aufgabe:** `cd ls pwd cat grep find pipe |  > chmod sudo` verstehen und *anwenden*. Dann **OverTheWire Bandit Level 0–5** ([overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit/)).
- **Deliverable:** Passwörter der gelösten Level notiert + je eine Zeile, was das Level dir beigebracht hat.

### Tag 3 · 🔐 Bandit Fortsetzung + Shell-Scripting 🔴
- **Aufgabe:** Bandit **Level 6–14**. Danach schreib ein kleines Bash-Script, das etwas Nützliches tut (z.B. alle `.jpg` in einem Ordner umbenennt oder ein Backup zippt).
- **Stretch:** Bis Level 18 durchziehen.
- **Deliverable:** Script im Repo, Bandit-Fortschritt notiert.

### Tag 4 · 🔢 Kopfrechnen – Trickkiste 🟡
- **Ziel:** Aufhören, im Kopf schriftlich zu rechnen.
- **Aufgabe:** Lerne & übe: ×11-Trick, Quadrate von Zahlen auf 5 (`35² = 3·4|25 = 1225`), Komplement-Methode bei Subtraktion, Kreuzmultiplikation für zweistellige Produkte. Grundidee des **Trachtenberg-Systems** anschauen.
- **Deliverable:** 30 selbst gerechnete Aufgaben mit Methodenname daneben. Neuer Zetamac-Score.

### Tag 5 · 🔐 Kryptographie I – Klassische Chiffren 🟡
- **Aufgabe:** Caesar-Chiffre **per Hand** knacken über Häufigkeitsanalyse. Dann in Python (a) einen Caesar-Ver-/Entschlüssler und (b) einen automatischen Häufigkeits-Breaker schreiben, der eine deutsche/englische Buchstabenverteilung nutzt.
- **Deliverable:** `caesar.py`, das einen unbekannten Caesar-Text automatisch entschlüsselt.

### Tag 6 · 🎨 Zeichnen I – Fundament 🟢
- **Ziel:** Sehen lernen, nicht "schön" zeichnen.
- **Aufgabe:** Gesture-Drawing (30-Sek-Skizzen), Kontur-Zeichnen ohne aufs Blatt zu schauen, "zeichne was du siehst, nicht was du weißt". 20 kurze Übungen von echten Objekten auf deinem Schreibtisch.
- **Deliverable:** Foto deiner Übungsblätter ins Repo. (Nicht wegwerfen — Tag 30 & 47 vergleichen.)

### Tag 7 · 🔢 Fermi-Schätzen 🔴
- **Ziel:** Größenordnungen aus dem Nichts abschätzen — die Kernfähigkeit fürs Überschlagen.
- **Aufgabe:** Löse 10 Fermi-Fragen mit sauberer Zerlegung, z.B.: *Wie viele Klavierstimmer gibt es in Berlin? Wie viele Tröpfchen sind in einer Regenwolke? Wie viel Daten produziert die Menschheit pro Sekunde?* Immer: Annahmen aufschreiben → rechnen → mit Realität (googeln) vergleichen.
- **Deliverable:** `fermi.md` mit 10 Schätzungen inkl. Rechenweg und "wie nah dran war ich".

### Tag 8 · 🔐 Kryptographie II – Vigenère 🔴
- **Aufgabe:** Vigenère implementieren (ver-/entschlüsseln). Dann den Klassiker: einen Vigenère-Text **ohne Schlüssel knacken** via Kasiski-Test + Index of Coincidence zur Schlüssellängen-Bestimmung, dann Häufigkeitsanalyse pro Spalte.
- **Deliverable:** `vigenere_break.py`, das die Schlüssellänge selbst findet.
- **Optional-Track ab hier:** Die [Cryptopals Challenges](https://cryptopals.com) sind Gold — wenn dir Krypto liegt, arbeite Set 1 nebenbei durch.

### Tag 9 · 🎨 Musik aus Code – Sonic Pi 🟢
- **Ziel:** Der Beweis, dass Programmieren kreativ ist.
- **Aufgabe:** [Sonic Pi](https://sonic-pi.net) installieren, Tutorial-Basics (Samples, Loops, `live_loop`, Effekte). Baue einen Track aus mind. 3 sich überlagernden Loops mit Beat + Melodie.
- **Deliverable:** Der Sonic-Pi-Code + eine kurze Aufnahme.

### Tag 10 · 🔢 Wahrscheinlichkeit – Fundament ⚫
- **Ziel:** Das mathematische Rückgrat für Poker, Gambling, Quant, Statistik & Krypto.
- **Aufgabe:** Ereignisraum, Kombinatorik (Permutation/Kombination), bedingte Wahrscheinlichkeit, **Satz von Bayes**. Rechne 15 Aufgaben von Hand — steigende Schwierigkeit bis "Ziegenproblem" und "medizinischer Test mit Basisrate".
- **Deliverable:** Gelöste Aufgaben, sauber notiert. Das Bayes-Ergebnis solltest du am Ende jemandem erklären können.

---

## Phase 2 — Kernkompetenzen vertiefen (Tag 11–28)

### Tag 11 · 🎰 Poker-Mathematik I 🔴
- **Aufgabe:** Outs, Equity, Pot Odds, EV eines Calls. Rechne für 10 konkrete Hände aus, ob ein Call +EV ist. "Rule of 4 and 2" verstehen *und* herleiten, warum sie funktioniert.
- **Deliverable:** 10 durchgerechnete Spots. Danach 20 Hände am Play-Money-Tisch mit bewusster Pot-Odds-Anwendung.
- **Realismus-Note:** Die Mathe ist lernbar und macht Spaß. "Professionell" davon zu leben ist extrem hart — behandle es als Denk- und Entscheidungstraining, nicht als Gelddruckmaschine.

### Tag 12 · 💻 Datenstrukturen from Scratch I 🔴
- **Aufgabe:** Ohne fertige Bibliotheken selbst bauen: dynamisches Array, verkettete Liste, Stack, Queue. Verstehe, *warum* `append` amortisiert O(1) ist.
- **Deliverable:** Eine Datei pro Struktur mit Tests. Big-O jeder Operation als Kommentar.

### Tag 13 · 🔎 Wie funktioniert das Internet? 🟡
- **Aufgabe:** Verfolge, was passiert, wenn du eine URL eintippst: DNS → TCP/IP-Handshake → HTTP → TLS. Nutze `dig`, `traceroute`, und öffne einmal die Netzwerk-Tab der Browser-Devtools. Schreib eine klare Erklärung, als würdest du sie einem 15-Jährigen erzählen.
- **Deliverable:** `wie-das-internet-funktioniert.md`, in deinen eigenen Worten.

### Tag 14 · 🔐 Kryptographie III – XOR & One-Time-Pad ⚫
- **Aufgabe:** XOR-Cipher implementieren. Verstehe, warum das One-Time-Pad *perfekt* sicher ist — und warum Schlüssel-Wiederverwendung alles zerstört. Knacke einen **Two-Time-Pad** (zwei Nachrichten mit gleichem Key).
- **Deliverable:** Code + eine erfolgreich rekonstruierte Klartext-Nachricht.

### Tag 15 · 🔢 Speed Reading – Fokus-Tag 🟢
- **Aufgabe:** Techniken lernen: Subvokalisation reduzieren, Fixationen/Chunking, mit dem Finger/Pointer führen. Übe 3× 10 min mit einem Tool (Spritz-Style / Spreeder). Danach **immer Verständnistest**.
- **Ehrliche Einordnung:** Die "3000 WPM"-Versprechen sind Marketing. Realistisch holst du dir 1,3–1,6× mehr Tempo *bei gehaltenem Verständnis* raus — und das ist schon extrem viel wert übers Studium. Miss dein Verständnis mit, sonst betrügst du dich selbst.
- **Deliverable:** Neuer WPM-Wert + Verständnis-% notiert.

### Tag 16 · 🔧 Arduino I 🟡
- **Aufgabe:** Falls Hardware da: Blink → Sensor auslesen (z.B. Poti/Temperatur) → Output steuern (LED/Servo). **Keine Hardware?** Alles in [Wokwi](https://wokwi.com) oder Tinkercad simulieren — voll ausreichend.
- **Deliverable:** Ein funktionierendes Mini-Projekt (z.B. "LED-Helligkeit per Poti") + Foto/Sim-Link.

### Tag 17 · 🔢 Statistik-Projekt I – Datenanalyse 🔴
- **Aufgabe:** Echten Datensatz ziehen ([Our World in Data](https://ourworldindata.org), Kaggle, oder eigene). Mit `pandas` + `matplotlib` **3 konkrete Fragen** stellen und beantworten. Mindestens eine Visualisierung, die etwas *erklärt*.
- **Deliverable:** Ein Jupyter-Notebook oder Script + die 3 Erkenntnisse in Worten.

### Tag 18 · 💻 C lernen – Pointer & Speicher 🔴
- **Ziel:** Cybersecurity ohne C-Verständnis geht nicht (Buffer Overflows, Exploits — alles Speicher).
- **Aufgabe:** Variablen, Arrays, **Pointer**, Stack vs. Heap. Schreib 3 kleine C-Programme. Verstehe, was ein Pointer *wirklich* ist. (Referenz: [CS50 Woche zu Memory](https://cs50.harvard.edu/x/).)
- **Deliverable:** 3 kompilierte C-Programme + eine Skizze, wie der Stack bei einem Funktionsaufruf aussieht.

### Tag 19 · 🎨 Malen – Farbtheorie & Studie 🟡
- **Aufgabe:** Farbkreis, Wert (hell/dunkel), Temperatur, Komplementärfarben. Mach eine **Studie mit begrenzter Palette** (nur 3 Farben + Weiß) von einem einfachen Motiv (Apfel, Tasse). Wert schlägt Farbe — konzentrier dich auf Hell/Dunkel.
- **Deliverable:** Foto der Studie.

### Tag 20 · 🔐 CTF & Web-Security 🔴
- **Aufgabe:** Web-Grundangriffe in **sanktionierten Laboren** lernen: die [PortSwigger Web Security Academy](https://portswigger.net/web-security) (SQL Injection + XSS Einstiegs-Labs) oder [picoCTF](https://picoctf.org).
- **⚠️ Ethik & Recht:** Nur in dafür gebauten Umgebungen (CTFs, PortSwigger, TryHackMe/HackTheBox, eigene VMs). Angriffe auf fremde Systeme ohne Erlaubnis sind in Deutschland strafbar (§202a ff. StGB). Als Security-Studi ist genau diese Grenze dein Berufsethos.
- **Deliverable:** 2 gelöste Labs + je eine Zeile "so funktioniert die Lücke, so schließt man sie".

### Tag 21 · 🎰 Kelly-Kriterium ⚫ (der schönste Crossover)
- **Ziel:** Die Formel, die Gambling, Poker *und* Investieren verbindet: optimale Einsatzgröße.
- **Aufgabe:** Kelly herleiten/verstehen (`f* = edge / odds`). Dann in Python simulieren: 1000 Wetten, vergleiche Flat-Betting vs. Full-Kelly vs. Half-Kelly übers Bankroll-Wachstum. Verstehe, warum Overbetting *ruiniert*, obwohl der EV positiv ist.
- **Deliverable:** Simulations-Script + ein Plot der Bankroll-Kurven + dein Fazit.

### Tag 22–24 · 💻🔐 3-Tage-Projekt: "Wähle deine Waffe" 🔴🎲
- **Ziel:** Ein echtes, benutzbares Tool bauen — dein erstes Portfolio-Stück.
- **Würfle (oder wähle bewusst):**
  1. **Datei-Verschlüsselungs-CLI** (mit `cryptography`-Lib, echtes AES)
  2. **Port-Scanner + Netzwerk-Mapper** (nur eigenes Netz scannen!)
  3. **Passwort-Analyzer + -Generator** (Entropie berechnen, gegen Wortlisten prüfen)
  4. **Telegram/Discord-Bot** mit einer nützlichen Funktion
  5. **Backtest-/Finanz-Tool** (bereitet Tag 35 vor)
  6. **Freie Wahl** — dein eigenes Ding
- **Deliverable:** Lauffähiges Tool mit `README.md`, sauber im Repo. Tag 1 = planen, Tag 2 = bauen, Tag 3 = polieren + dokumentieren.

### Tag 25 · 🔐 Hashing & Passwort-Sicherheit 🔴
- **Aufgabe:** SHA-256 verstehen, Salting, bcrypt, warum Rainbow Tables funktionieren. Generiere selbst ein paar schwache Hashes und knacke sie mit `john` oder `hashcat` (auf **deinen eigenen** Test-Hashes).
- **Deliverable:** Notiz "warum ist ein gesalzener bcrypt-Hash so viel besser als plain SHA-256?" + geknackte Test-Hashes.

### Tag 26 · 💻 Algorithmen – Sortieren & Big-O 🔴
- **Aufgabe:** Implementiere Bubble-, Insertion-, Merge- und Quicksort selbst. Miss ihre Laufzeit bei wachsender Eingabe empirisch. Dann eine harte Nuss: ein Dynamic-Programming-Problem (z.B. Longest Common Subsequence).
- **Deliverable:** Code + ein Plot Laufzeit vs. Eingabegröße, der das O(n²) vs. O(n log n) sichtbar macht.

### Tag 27 · 🔎 Detektiv-Tag – OSINT 🔴
- **Ziel:** Öffentlich verfügbare Infos verknüpfen — legal und ethisch.
- **Aufgabe:** (a) Geolocation-Puzzles: [GeoGuessr](https://geoguessr.com) oder Foto-Geolokalisierung. (b) **Audit dich selbst:** Was findet man in 30 min öffentlich über dich? (c) Optional: eine sanktionierte OSINT-Challenge.
- **⚠️ Ethik:** OSINT nur an dir selbst, an frei gegebenen Puzzles oder mit Einwilligung. Kein Stalking, keine echten Personen ohne deren OK.
- **Deliverable:** Ein "Ermittlungsbericht" zu deinem eigenen digitalen Fußabdruck + eine Sache, die du danach privater stellst.

### Tag 28 · 🔐 Kryptographie IV – RSA von Hand ⚫ (Krypto-Gipfel)
- **Aufgabe:** RSA **mit kleinen Primzahlen komplett per Hand** durchrechnen: Schlüsselerzeugung, Ver- und Entschlüsselung. Dann Toy-RSA in Python implementieren. Verstehe, *warum* die Sicherheit auf der Schwierigkeit des Faktorisierens beruht.
- **Deliverable:** Handschriftliche Rechnung (Foto) + `rsa_toy.py`. Wenn du RSA jemandem erklären kannst, hast du gewonnen.

---

## Phase 3 — Anwenden & erschaffen (Tag 29–42)

### Tag 29 · 🔧 Raspberry-Pi-Projekt 🔴
- **Aufgabe:** Falls Pi vorhanden: aufsetzen + ein Projekt wählen — Pi-hole (Werbeblocker fürs ganze Netz), Netzwerk-Scanner, Retro-Emulator, kleiner Home-Server. **Kein Pi?** Mach das Äquivalent in einer VM/Docker (z.B. Pi-hole via Docker) oder erweitere das Arduino-Projekt von Tag 16.
- **Deliverable:** Etwas, das *läuft* + kurze Doku, was du eingerichtet hast.

### Tag 30 · 🎨 Zeichnen II – Perspektive 🔴
- **Aufgabe:** 1- und 2-Punkt-Perspektive verstehen. Zeichne einen Innenraum (dein Zimmer) und eine Straßenszene in korrekter Perspektive. Vergleich mit Tag 6 — du wirst den Unterschied sehen.
- **Deliverable:** 2 Perspektiv-Zeichnungen.

### Tag 31 · 🔢 Monte-Carlo-Simulation 🔴
- **Ziel:** Wenn du etwas nicht ausrechnen kannst, simulierst du es.
- **Aufgabe:** Schätze π per Zufall (Punkte im Quadrat/Kreis). Dann etwas Nützliches: simuliere die Equity einer Pokerhand gegen eine zufällige Gegnerhand über 100.000 Runs. Vergleiche mit deiner Tag-11-Handrechnung.
- **Deliverable:** Beide Simulationen + der Aha-Moment "simulieren > exakt rechnen, wenn's kompliziert wird".

### Tag 32 · 💻 Regex & Textverarbeitung 🟡
- **Aufgabe:** Reguläre Ausdrücke *richtig* lernen (nicht nur googeln). Löse [regexcrossword.com](https://regexcrossword.com). Dann bau einen Log-Parser, der aus einer Server-Logdatei alle fehlgeschlagenen Login-Versuche mit IP extrahiert.
- **Deliverable:** Der Log-Parser + gelöste Regex-Puzzles.

### Tag 33 · 🎰 Blackjack & Card Counting – die Theorie 🔴
- **Aufgabe:** Die Mathematik dahinter: Hausvorteil, das Hi-Lo-System, "True Count", warum Zählen den Edge kippt. Simuliere in Python den EV mit und ohne Zählen.
- **Realismus-Note:** Es funktioniert mathematisch — deshalb schmeißen Casinos Zähler raus, und es ist knochenharte, langweilige Arbeit für dünne Margen. Behandle es als angewandte Statistik, nicht als Karriereplan.
- **Deliverable:** Simulation, die den Edge-Flip durch Zählen zeigt.

### Tag 34 · 🔎 Wie funktioniert das? – Reverse Engineering 🟡🎲
- **Aufgabe:** Würfle ein Alltagsding/System und geh in die Tiefe, bis du es *wirklich* verstehst — dann schreib eine Erklärung:
  1. Ein **Türschloss** (Stiftzuhaltung) — optional: legales Lockpicking an eigenem Schloss
  2. Eine **Festplatte / SSD** — wie werden Bits physisch gespeichert?
  3. **GPS** — wie weiß dein Handy, wo es ist? (Relativität inklusive!)
  4. **Kompression** — warum wird eine ZIP kleiner? (Huffman-Coding)
  5. Ein **Lithium-Akku** — was passiert beim Laden?
  6. Freie Wahl
- **Deliverable:** Ein Explainer (Text oder Skizze), der es klar macht.

### Tag 35 · 🎰 Quant/Trading – Strategie backtesten 🔴
- **Aufgabe:** Historische Kursdaten ziehen (`yfinance`). Implementiere eine simple Strategie (z.B. Moving-Average-Crossover), backteste sie, berechne Rendite, Sharpe Ratio, Max Drawdown.
- **Ehrliche Einordnung:** Fast jede simple Strategie sieht im Backtest gut aus und versagt live (Overfitting, Kosten, Slippage). Das ist die *Lektion*, nicht ein Fehler. **Keine Anlageberatung** — das ist ein Mathe-/Coding-Übung.
- **Deliverable:** Backtest-Notebook + eine ehrliche Analyse "würde das echt funktionieren? Warum (nicht)?"

### Tag 36 · 💻 Datenstrukturen from Scratch II 🔴
- **Aufgabe:** Bau selbst: eine Hash-Table (mit Kollisionsbehandlung — Chaining oder Open Addressing) und einen binären Suchbaum (insert/search/delete). Verstehe, warum eine Hash-Table im Schnitt O(1) lookup schafft.
- **Deliverable:** Beide Strukturen mit Tests. Erklär, was bei einer schlechten Hash-Funktion passiert.

### Tag 37 · 🎨 Musik II – DAW / Produktion 🟡
- **Aufgabe:** Eine echte DAW ausprobieren (kostenlos: LMMS, GarageBand, oder Sonic Pi vertiefen). Baue einen vollständigeren Track: Beat + Bassline + Melodie + eine Struktur (Intro/Drop).
- **Deliverable:** Ein exportierter Track (min. 30 Sek).

### Tag 38 · 🎰 Poker II – Ranges & GTO-Basics 🔴
- **Aufgabe:** Von "welche Karten hab ich" zu "welche Range hat der Gegner". Hand-Ranges, Bluff-Frequenzen, GTO vs. exploitatives Spiel — die Grundidee. Analysiere 15 eigene Hände (aus Tag 11) neu mit Range-Denken.
- **Deliverable:** Range-Analyse von 5 interessanten Spots.

### Tag 39 · 🔐 Netzwerke & Packet-Analyse 🔴
- **Aufgabe:** Wireshark installieren. Fang deinen *eigenen* Traffic ein und analysiere: Wie sieht ein TCP-Handshake im Paket aus? Was ist bei HTTP sichtbar, was bei HTTPS nicht? Findest du eine unverschlüsselte Anfrage?
- **Deliverable:** Screenshot eines TCP-Handshakes + Erklärung, was du siehst.

### Tag 40 · 🎨 Kreativ-Wildcard 🟢🎲
- **Aufgabe:** Würfle:
  1. Comic-Strip (3–4 Panels, eigene Story)
  2. Generative Kunst per Code (z.B. mit `p5.js` oder Python/Turtle)
  3. Character-Design (3 Varianten einer Figur)
  4. Landschaft malen (aus Fantasie)
  5. Ein Album-Cover für deinen Tag-37-Track
  6. Freie Wahl
- **Deliverable:** Das fertige Werk.

### Tag 41 · 🔢 Bayesianisches Denken & Statistik II 🔴
- **Aufgabe:** Bayes in der Tiefe: ein reales Inferenz-Problem lösen (z.B. Spam-Filter-Logik, oder "wie sehr sollte ich meine Überzeugung nach Evidenz X ändern?"). Basisraten-Fehler verstehen und ein Beispiel durchrechnen.
- **Deliverable:** Ein durchgerechnetes Bayes-Problem + ein Satz, wie du Bayes im Alltag anwenden kannst.

### Tag 42 · ⚙️ Buffer / Deep-Dive / Aufholen 🎲
- **Aufgabe:** Flex-Tag. Wähle: das Härteste der letzten Wochen nochmal angehen und *wirklich* verstehen, ODER dein Lieblingsthema vertiefen, ODER aufholen was liegengeblieben ist, ODER echter Ruhetag.
- **Deliverable:** Was auch immer — kurz im Log festhalten warum.

---

## Phase 4 — Capstone & Brücke ins Studium (Tag 43–47)

### Tag 43–46 · 💻🔐 Capstone: "Die Integration" ⚫🎲
- **Ziel:** Ein Projekt, das mehrere Tracks verbindet — dein Vorzeige-Stück fürs erste Semester.
- **Würfle oder wähle:**
  1. **Eigene CTF-Challenge** designen *und* lösen: mit selbstgebauten Krypto-, Web- und Stego-Ebenen. (Andere könnten sie später spielen.)
  2. **Toy-Secure-Chat:** Diffie-Hellman-Schlüsselaustausch + verschlüsselte Nachrichten über Sockets zwischen zwei Terminals.
  3. **Poker-/Blackjack-Simulator** mit Strategie-Engine + statistischer Auswertung + Visualisierung (verbindet Zahlen + Edge + Code).
  4. **Security-Gadget** mit Arduino/Pi: RFID-Reader, bewegungsgetriggerte Kamera, oder Netzwerk-Monitor.
- **Ablauf:** Tag 43 planen & Architektur, Tag 44–45 bauen, Tag 46 testen + `README` schreiben + auf GitHub polieren.
- **Deliverable:** Ein dokumentiertes, lauffähiges Projekt. Dein bestes Stück der ganzen Challenge.

### Tag 47 · 🏁 Reflexion, Showcase & Übergang 🟢
- **Aufgabe:**
  1. **Baselines neu messen:** Zetamac + Speed-Reading-WPM. Vergleich mit Tag 1. Sieh deinen Fortschritt schwarz auf weiß.
  2. **Zeichnung** von einem Objekt wie an Tag 6 — vergleiche.
  3. **Retrospektive schreiben:** Was war am härtesten? Was hat am meisten Spaß gemacht? Was willst du im Studium weiterverfolgen?
  4. **Portfolio bauen:** Alle Projekte im GitHub-Repo mit einer sauberen Haupt-`README` als Landing Page.
  5. **Momentum-Plan:** 3 Gewohnheiten aus dieser Challenge, die du ins Semester mitnimmst.
- **Deliverable:** Repo aufgeräumt & öffentlich + `retrospektive.md`.

---

## 🏆 Punktesystem (optional, für die Extra-Motivation)

| Aktion | Punkte |
|---|---|
| Kernaufgabe erledigt | **10** |
| Stretch/Limit-Push geschafft | **+5** |
| Tägliches Warmup gemacht | **+2** |
| An eine echte Grenze gestoßen (geflucht, fast aufgegeben, doch geschafft) | **+5 "Grit-Bonus"** |
| Deliverable ins Repo committet | **+3** |

**Ziel:** ≥ 600 Punkte über 47 Tage. Bei 750+ hast du dir was Größeres verdient (Konzert, Gadget, ein richtig gutes Essen — leg's jetzt fest).

---

## 📓 Log-Vorlage (kopieren, täglich ausfüllen)

```markdown
### Tag X — [Thema]
- Zetamac / WPM heute:
- Gemacht (Kern):
- Stretch:  ja / nein
- Wo ich an die Grenze kam:
- Aha-Moment:
- Deliverable-Link:
- Punkte:
```

---

## 🔗 Ressourcen-Übersicht

**Security / CTF**
- OverTheWire Bandit — `overthewire.org/wargames/bandit`
- picoCTF — `picoctf.org`
- PortSwigger Web Security Academy — `portswigger.net/web-security`
- TryHackMe / HackTheBox — geführte Lernpfade
- Cryptopals — `cryptopals.com` (der Krypto-Klassiker)

**Code / CS**
- CS50 (Harvard, frei) — `cs50.harvard.edu/x`
- Project Euler — `projecteuler.net` (Mathe + Code, endlose Übung)

**Zahlen / Kopfrechnen**
- Zetamac — `arithmetic.zetamac.com`

**Hardware (auch ohne Board)**
- Wokwi — `wokwi.com` (Arduino/ESP-Simulator im Browser)

**Musik**
- Sonic Pi — `sonic-pi.net`

**Daten**
- Our World in Data, Kaggle Datasets

> **Wichtigste Regel von allen:** Dranbleiben schlägt Perfektion. Ein mittelmäßig erledigter Tag ist unendlich viel besser als ein übersprungener. Viel Erfolg — und viel Spaß am Limit. 🚀
```
