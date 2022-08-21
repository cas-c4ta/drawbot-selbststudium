"""
Variablen schreiben
"""

newPage(1000, 1000)

rect1x = 200 + 200
rect1y = 5 * 100
rect1width = 1000 - 500
rect1height = 1000 - 600

rect2x = 900 / 30
rect2y = 5 * 24
rect2width = width() // 2
rect2height = height() / 3

rect(rect1x, rect1y, rect1width, rect1height)
rect(rect2x, rect2y, rect2width, rect2height)

"""
Die Beispiele hier sind zwar nicht besonders sinvoll.
Aber du siehst, dass es möglich ist, ganze Rechnungen
statt einzelner Werte zu schreiben. Beim Ausführen des
Scripts werden die Rechungen durch ihr Resultat ersetzt.

- Kannst du zwei Rechtecke so positionieren, dass das eine immer
  das untere linke Viertel der Fläche ausfüllt und das andere
  jeweils das obere rechte Viertel?
- Kannst du es so einrichten, dass es auch funktioniert, wenn es
  newPage("A4") heisst?


Namen von Variablen:
    - beginnen mit kleinbuchstaben
    - keine Zahl als erstes Zeichen
    - erlaubt: a-z, A-Z, 0-9, _ 
    - Camel case: fooBarBaz 🐫
    - Snake case: foo_bar_baz 🐍

Abgesehen davon, dass keine Sonderzeichen erlaubt sind und
dass sie nicht mit einer Ziffer beginnen dürfen, kannst du
Variablen so benennen wie du willst.

Du musst allenfalls beachten, dass du kein «reserviertes» Wort
verwendest (siehe Cheatsheet).

Meist ist es gut, den Namen einer Variablen so zu wählen,
dass du ihren Zweck daran ablesen kannst.

Wenn dir gerade nichts einfällt, sind Nonsens-Namen wie
"foo" und "bar" zuverlässige Helfer. Aber vergiss nicht,
sie später mit Suchen/Ersetzen mit etwas sinvollerem zu
ersetzen.
"""