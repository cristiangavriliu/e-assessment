# Deep Dive Questions
deepdive_questions = {
    "task1": {
        "questions": [
            {
                "template": "Was gibt die Modulo-Operation (%) zurück?",
                "type": "single_choice",
                "correct_answer": "a) {V1}",
                "wrong_answers": [
                    "b) {V2}",
                    "c) {V3}",
                    "d) {V4}"
                ],
                "variables": {
                    "V1": [
                        "Rest einer ganzzahligen Division",
                        "Restwert einer Berechnung",
                    ],
                    "V2": [
                        "Das Ergebnis einer Division",
                        "Teilung zweier Zahlen",
                        "Quotient einer Division"
                    ],
                    "V3": [
                        "Multiplikation zweier Zahlen",
                        "Produkt zweier Zahlen",
                        "Faktor"
                    ],
                    "V4": [
                        "Exponent",
                        "Potenz"
                    ]
                }
            },
            {
                "template": "Angenommen, {V1} in deiner Lösung ist 2. Wie wäre der Output, wenn in der if-Bedingung (Zahl % 2 == 1) stehen würde?",
                "type": "freitext",
                "answer": "Deine Zahl ist ungerade: 2",
                "variables": {
                    "V1": ["die Zahl", "der Variablenwert", "der Wert der Variablen"]
                }
            },
            {
                "template": "Als was fungiert die Variable `Zahl`?",
                "type": "freitext",
                "answer": "Die Variable 'Zahl' dient als Eingabevariable. (Die überprüft wird, ob sie gerade oder ungerade ist.)"
            },
            {
                "template": "Was ist das Ergebnis von 14 % 12?",
                "type": "single_choice",
                "correct_answer": "a) 2",
                "wrong_answers": [
                    "b) {V4}",
                    "c) {V5}",
                    "d) {V6}"
                ],
                "variables": {
                    "V4": ["0", "1", "3"],  
                    "V5": ["11", "6", "14"],  
                    "V6": ["12", "4", "5"]   
                }
            },
            {
                "template": "Fülle die Lücken im folgenden Text aus, um den Ablauf des Codes zu erklären: Der Code prüft, ob {V1} gerade oder ungerade ist. Wenn die {V1} durch {V2} ohne Rest teilbar ist, wird sie als gerade Zahl erkannt. Andernfalls wird sie als {V3} erkannt.",
                "type": "cloze",
                "answers": {
                    "V1": ["die eingegebene Zahl", "die eingegebene Nummer", "der eingegebene Wert", "Zahl", "zahl", "die Zahl", "die zahl"],
                    "V2": ["2", "zwei"],
                    "V3": ["ungerade", "nicht gerade", "Ungerade", "Nicht gerade"]
                }
            }
            # Weitere Feedbackfragen können hier hinzugefügt werden
        ]
    },
    "task2": {
        "questions": [
            {
                "template": "Was macht die Listen-Abstraktion in Python?",
                "type": "single_choice",
                "correct_answer": "a) {V1}",
                "wrong_answers": ["b) {V2}", "c) {V3}", "d) {V4}"],
                "variables": {
                    "V1": [
                        "Erstellt eine neue Liste durch Iteration über ein bestehendes Iterable.",
                        "Erstellt eine neue Liste durch Auswahl bestimmter Elemente aus einem bestehenden Iterable.",
                        "Erstellt eine neue Liste durch Filtern eines bestehenden Iterables."
                    ],
                    "V2": [
                        "Erstellt eine neue Variable.",
                        "Erstellt eine neue Liste durch Duplizieren der Elemente.",
                        "Erstellt eine neue Liste durch das Umkehren der Reihenfolge der Elemente."
                    ],
                    "V3": [
                        "Erstellt eine neue Liste durch Sortieren einer bestehenden Liste.",
                        "Erstellt eine neue Liste durch das direkte entfernen von Elementen aus einer bestehenden Liste.",
                        "Erstellt eine neue Liste durch das Zusammenfügen mehrerer Listen."
                    ],
                    "V4": [
                        "Erstellt eine neue Liste durch Löschen von Variablen.",
                        "Erstellt eine neue Liste durch Teilen der Liste in kleinere Teile.",
                        "Erstellt eine neue Liste durch das Ersetzen von Variablen."
                    ]
                }
            },
            {
                "template": "Was passiert, wenn `if x % 2 != 0` anstelle von `if x % 2 == 0` verwendet wird?",
                "type": "freitext",
                "answer": "Die Liste `gerade_zahlen` wird nur die ungeraden Zahlen aus der ursprünglichen Liste `zahlen` enthalten."
            },
            {
                "template": "In welchem Fall könnte die Liste `gerade_zahlen` leer sein?",
                "type": "multiple_choice",
                "correct_answer": ["b) {V2}", "d) {V4}"],
                "wrong_answers": [
                    "a) {V1}",
                    "c) {V3}"
                ],
                "variables": {
                    "V1": [
                        "Wenn `zahlen` nur eine gerade Zahl enthält.",
                        "Wenn alle Zahlen in `zahlen` gerade und größer als 10 sind.",
                        "Wenn alle Zahlen in `zahlen` die Primzahlen bis 10 sind."
                    ],
                    "V2": [
                        "Wenn `zahlen` leer ist.",
                        "Wenn alle Zahlen in `zahlen` ungerade sind.",
                        "Wenn `zahlen` nicht definiert ist."
                    ],
                    "V3": [
                        "Wenn alle Zahlen in `zahlen` gerade sind.",
                        "Wenn `zahlen` nur durch 3 teilbare Zahlen enthält.",
                        "Wenn `zahlen` nur durch 5 teilbare Zahlen enthält."
                    ],
                    "V4": [
                        "Wenn alle Zahlen in `zahlen` Primzahlen sind und keine dieser Primzahlen 2 ist.",
                        "Wenn alle Zahlen in `zahlen` durch 7 teilbar sind und keine davon gerade ist.",
                        "Wenn alle Zahlen in `zahlen` von einer anderen Liste stammen, die nur ungerade Zahlen enthält."
                    ]
                }
            },
            {
                "template": "Fülle die Lücken im folgenden Text aus: Der Code verwendet das Listen-Abstraktion, um nur die {V1} Zahlen aus der Liste `zahlen` zu filtern und sie in der Liste `gerade_zahlen` zu speichern. Dies wird erreicht, indem überprüft wird, ob eine Zahl durch {V2} teilbar ist.",
                "type": "cloze",
                "answers": {
                    "V1": ["geraden", "Geraden"],
                    "V2": ["2", "zwei", "Zwei"]
                }
            }
            # Weitere Feedbackfragen können hier hinzugefügt werden
        ]
    },
    "task3": {
        "questions": [
            {
                "template": "Was macht die `range` Funktion in Python?",
                "type": "single_choice",
                "correct_answer": "d) {V4}",
                "wrong_answers": [
                    "b) {V2}",
                    "c) {V3}",
                    "a) {V1}"
                ],
                "variables": {
                    "V4": [
                        "Generiert ein Iterable von Zahlen.",
                        "Generiert eine Sequenz von Zahlen.",
                        "Generiert eine Folge von Zahlen."
                    ],
                    "V2": [
                        "Generiert eine Liste von Zahlen.",
                        "Generiert einen String von Zahlen.",
                        "Generiert eine Liste von Zeichen."
                    ],
                    "V3": [
                        "Generiert einen String von Zahlen.",
                        "Generiert eine Verkettung von Zahlen.",
                        "Generiert eine Zeichenkette von Zahlen."
                    ],
                    "V1": [
                        "Generiert eine Tabelle von Zahlen.",
                        "Generiert ein Wörterbuch von Zahlen.",
                        "Generiert ein Array von Zahlen."
                    ]
                }
            },
            {
                "template": "Was passiert, wenn `range(1, 100)` anstelle von `range(1, 101)` verwendet wird?",
                "type": "single_choice",
                "correct_answer": "c) {V3}",
                "wrong_answers": [
                    "a) {V1}",
                    "b) {V2}",
                    "d) {V4}"
                ],
                "variables": {
                    "V1": [
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` die Zahlen von 1 bis 95 umfasst.",
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` die Zahlen von 1 bis 98 umfasst.",
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` die Zahlen von 1 bis 97 umfasst."
                    ],
                    "V2": [
                        "Der Code wird einen Fehler werfen, weil `range(1, 100)` eine ungültige Syntax ist.",
                        "Der Code wird einen Fehler werfen, weil `range(1, 100)` eine falsche Syntax ist.",
                        "Der Code wird einen Fehler werfen, weil `range(1, 100)` eine nicht erlaubte Syntax ist."
                    ],
                    "V3": [
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` die Zahlen von 1 bis einschließlich 99 umfasst.",
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` alle Zahlen von 1 bis 99 beinhaltet.",
                        "Es wird ein anderer Bereich abgedeckt, da `range(1, 100)` von 1 bis 99 geht."
                    ],
                    "V4": [
                        "Es wird derselbe Bereich abgedeckt, da `range(1, 101)` die Zahlen von 1 bis 100 umfasst.",
                        "Es wird derselbe Bereich abgedeckt, da `range(1, 101)` alle Zahlen von 1 bis 100 beinhaltet.",
                        "Es wird derselbe Bereich abgedeckt, da `range(1, 101)` von 1 bis 100 geht."
                    ]
                }
            },
            {
                "template": "In welchem Fall könnte die Variable `summe` 0 bleiben?",
                "type": "multiple_choice",
                "correct_answer": ["a) {V1}", "b) {V2}"],
                "wrong_answers": [
                    "c) {V3}",
                    "d) {V4}"
                ],
                "variables": {
                    "V1": [
                        "Wenn der Startwert der `range` Funktion größer ist als der Endwert.",
                        "Wenn die `range` Funktion falsch verwendet wird und keine Werte liefert.",
                        "Wenn der Bereich der range-Funktion keine Werte umfasst."
                    ],
                    "V2": [
                        "Wenn `range(0, 0)` verwendet wird.",
                        "Wenn die Schleife aufgrund eines leeren Bereichs der range-Funktion keine Werte verarbeitet.",
                        "Wenn die `range` Funktion keine Werte liefert."
                    ],
                    "V3": [
                        "Wenn die `range` Funktion negative Werte enthält.",
                        "Wenn die `range` Funktion nur einen Wert enthält.",
                        "Wenn die `range` Funktion positive Werte enthält."
                    ],
                    "V4": [
                        "Wenn die `range` Funktion eine große Anzahl von Werten enthält.",
                        "Wenn die `range` Funktion ungerade Werte enthält.",
                        "Wenn die `range` Funktion Werte im Dezimalbereich enthält."
                    ]
                }
            },
            {
                "template": "Fülle die Lücken im folgenden Text aus, um zu erklären, wie der Code die Summe der Zahlen berechnet: Der Code verwendet eine Schleife, die von {V1} bis {V2} läuft. Innerhalb der Schleife wird jede Zahl zur Variablen {V3} addiert. Am Ende enthält die Variable {V3} die Summe aller Zahlen von {V1} bis {V2} .",
                "type": "cloze",
                "answers": {
                    "V1": ["1", "eins", "Eins"],
                    "V2": ["100", "einhundert", "Einhundert"],
                    "V3": ["summe", "Summe"]
                }
            }
            # Weitere Feedbackfragen können hier hinzugefügt werden
        ]
    },
    "task4": {
        "questions": [
            {
                "template": "Was macht die `split` Funktion in Python?",
                "type": "single_choice",
                "correct_answer": "c) {V3}",
                "wrong_answers": [
                    "b) {V2}",
                    "a) {V1}",
                    "d) {V4}"
                ],
                "variables": {
                    "V3": [
                        "Trennt einen String in eine Liste von Teilstrings basierend auf einem Trennzeichen.",
                        "Teilt einen String in mehrere Teilstrings auf."
                    ],
                    "V2": [
                        "Fügt mehrere Strings zu einem zusammen.",
                        "Verbindet mehrere Strings zu einem.",
                        "Kombiniert mehrere Strings zu einem."
                    ],
                    "V1": [
                        "Sortiert die Wörter in einem String.",
                        "Ordnet die Wörter in einem String neu an.",
                        "Sortiert die Elemente in einem String."
                    ],
                    "V4": [
                        "Entfernt ein bestimmtes Zeichen aus einem String.",
                        "Löscht ein bestimmtes Zeichen aus einem String.",
                        "Entfernt alle Instanzen eines Zeichens aus einem String."
                    ]
                }
            },
            {
                "template": "Was passiert, wenn `text.split(' ')` anstelle von `text.split()` verwendet wird?",
                "type": "single_choice",
                "correct_answer": "d) {V4}",
                "wrong_answers": [
                    "a) {V1}",
                    "b) {V2}",
                    "c) {V3}"
                ],
                "variables": {
                    "V1": [
                        "Die Funktionalität bleibt gleich, da der Standardwert von `split` ein Leerzeichen ist.",
                        "Die Funktionalität bleibt gleich, da `split` standardmäßig nach Leerzeichen trennt.",
                        "Es gibt keinen Unterschied, da `split()` standardmäßig nach Leerzeichen trennt."
                    ],
                    "V2": [
                        "Der String wird in einzelne Zeichen aufgeteilt.",
                        "Der String wird in einzelne Buchstaben aufgeteilt.",
                        "Der String wird in einzelne Symbole aufgeteilt."
                    ],
                    "V3": [
                        "Der String wird in ganze Sätze aufgeteilt.",
                        "Der String wird in Absätze aufgeteilt.",
                        "Der String wird in Textblöcke aufgeteilt."
                    ],
                    "V4": [
                        "Der String wird in einzelne Wörter aufgeteilt.",
                        "Der String wird in Begriffe aufgeteilt.",
                        "Der String wird in Teile aufgeteilt."
                    ]
                }
            },
            {
                "template": "In welchem Fall könnte `anzahl_woerter` 1 sein, auch wenn der String mehrere Wörter enthält?",
                "type": "multiple_choice",
                "correct_answer": ["a) {V1}","d) {V4}"],
                "wrong_answers": [
                    "b) {V2}",
                    "c) {V3}"
                ],
                "variables": {
                    "V1": [
                        "Wenn der String keine Leerzeichen enthält.",
                        "Wenn der String durch Kommata getrennte Wörter enthält und keine Leerzeichen verwendet werden.",
                        "Wenn der String keine Leerzeichen enthält, sondern andere Trennzeichen verwendet."
                    ],
                    "V2": [
                        "Wenn der String nur Sonderzeichen enthält.",
                        "Wenn der String leer ist."
                    ],
                    "V3": [
                        "Wenn der String aus Zahlen besteht.",
                        "Wenn der String durch Leerzeichen getrennte Sonderzeichen enthält."
                    ],
                    "V4": [
                        "Wenn das Trennzeichen falsch gewählt ist.",
                        "Wenn der String durch Semikolons getrennte Wörter enthält.",
                        "Wenn der String durch Bindestriche getrennte Wörter enthält."
                    ]
                }
            },
            {
                "template": "Fülle die Lücken im folgenden Text aus, um zu erklären, wie der Code die Anzahl der Wörter berechnet: Der Code verwendet die `split`-Funktion, um den String in {V1} zu teilen. Anschließend wird die Länge der resultierenden Liste mit `len()` berechnet, um die {V2} zu ermitteln.",
                "type": "cloze",
                "answers": {
                    "V1": ["Wörter", "Teile", "wörter", "teile"],
                    "V2": ["Anzahl der Wörter", "Anzahl der Teile", "Anzahl Wörter", "anzahl wörter", "anzahl Wörter", "anzahl der Wörter"]
                }
            }
            # Weitere Feedbackfragen können hier hinzugefügt werden
        ]
    },
    "task5": {
        "questions": [
            {
                "template": "Was ist die Fibonacci-Folge?",
                "type": "single_choice",
                "correct_answer": "b) {V2}",
                "wrong_answers": [
                    "a) {V1}",
                    "c) {V3}",
                    "d) {V4}"
                ],
                "variables": {
                    "V2": [
                        "Eine Zahlenfolge, bei der jede Zahl die Summe der beiden vorhergehenden ist.",
                        "Eine Zahlenfolge, bei der jede Zahl die Summe der letzten zwei Zahlen ist."
                    ],
                    "V1": [
                        "Eine Zahlenfolge, bei der jede Zahl das Produkt der beiden vorhergehenden ist.",
                        "Eine Zahlenfolge, bei der jede Zahl das Produkt der letzten drei Zahlen ist.",
                        "Eine Zahlenfolge, bei der jede Zahl das Produkt der vorhergehenden und der nächsten Zahl ist."
                    ],
                    "V3": [
                        "Eine Zahlenfolge, bei der jede Zahl die Differenz der beiden vorhergehenden ist.",
                        "Eine Zahlenfolge, bei der jede Zahl die Differenz der letzten drei Zahlen ist.",
                        "Eine Zahlenfolge, bei der jede Zahl die Differenz der vorhergehenden und der nächsten Zahl ist."
                    ],
                    "V4": [
                        "Eine Zahlenfolge, bei der jede Zahl der Quotient der beiden vorhergehenden ist.",
                        "Eine Zahlenfolge, bei der jede Zahl der Quotient der letzten drei Zahlen ist.",
                        "Eine Zahlenfolge, bei der jede Zahl der Quotient der vorhergehenden und der nächsten Zahl ist."
                    ]
                }
            },
            {
                "template": "Was passiert, wenn `n = 1` gesetzt wird?",
                "type": "freitext",
                "answer": "Die Ausgabe wird `[0,1]` sein, da die for-Schleife nicht ausgeführt wird und die ursprüngliche Liste unverändert bleibt."
            },
            {
                "template": "In welchem Fall könnte die Fibonacci-Folge endlos weitergehen?",
                "type": "single_choice",
                "correct_answer": "a) {V1}",
                "wrong_answers": [
                    "b) {V2}",
                    "c) {V3}",
                    "d) {V4}"
                ],
                "variables": {
                    "V1": [
                        "Wenn keine Begrenzung für `n` gesetzt wird."
                        "Wenn `n` unendlich ist.",
                        "Wenn die Schleife bedingungslos weiterläuft."
                    ],
                    "V2": [
                        "Wenn `n` negativ ist.",
                        "Wenn `n` null ist.",
                        "Wenn `n` eins ist."
                    ],
                    "V3": [
                        "Wenn `n` auf einen sehr kleinen Wert gesetzt wird.",
                        "Wenn `n` auf null gesetzt wird."
                    ],
                    "V4": [
                        "Wenn `n` ein beliebiger Wert ist.",
                        "Wenn n eine gerade Zahl ist.",
                        "Wenn n eine Primzahl ist."
                    ]
                }
            },
            {
                "template": "Fülle die Lücken im folgenden Text aus, um zu erklären, wie der Code die Fibonacci-Folge berechnet: Der Code startet mit den Zahlen {V1} und {V2} . Für jedes weitere Element der Sequenz wird die Summe der beiden vorhergehenden Zahlen berechnet, was durch den Ausdruck {V3} + {V4} erreicht wird.",
                "type": "cloze",
                "answers": {
                    "V1": ["0", "null","Null"],
                    "V2": ["1", "eins","Eins"],
                    "V3": ["fibonacci[i-1]", "fibonacci [i-1]", "Fibonacci[i-1]","Fibonacci [i-1]"],
                    "V4": ["fibonacci[i-2]", "fibonacci [i-2]","Fibonacci[i-2]", "Fibonacci [i-2]"]
                }
            }
            # Weitere Feedbackfragen können hier hinzugefügt werden
        ]
    }
}
