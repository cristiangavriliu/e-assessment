# Aufgaben und Lösung
tasks = {
    "task1": {
        "description": "Passen Sie den Code an den Stellen mit einem Stern (*) an, sodass eine eingegebene Zahl bei *DeineTestzahl* nach mathematischem Verständnis in gerade und ungerade Zahlen eindeutig zugewiesen wird.\nHinweis: Es wird davon ausgegangen, dass *DeineTestzahl* eine positive ganze Zahl ist.",
        "code": "Zahl = *DeineTestzahl*\nif (****):\n    print(\"Deine Zahl ist gerade:\", Zahl)\nelse:\n    print(\"Deine Zahl ist ungerade:\", Zahl)",
        "solution": "Zahl = *DeineTestzahl*\nif (Zahl % 2 == 0):\n    print(\"Deine Zahl ist gerade:\", Zahl)\nelse:\n    print(\"Deine Zahl ist ungerade:\", Zahl)"
    },
    "task2": {
        "description": "Passe den Code so an, dass er nur die geraden Zahlen aus der Liste zahlen filtert und in gerade_zahlen speichert.",
        "code": "zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ngerade_zahlen = [x for x in zahlen if *BEDINGUNG*]\nprint(gerade_zahlen)",
        "solution": "zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ngerade_zahlen = [x for x in zahlen if x % 2 == 0]\nprint(gerade_zahlen)"
    },
    "task3": {
        "description": "Passen den Code so an, dass er die Summe der Zahlen von 1 bis 100 berechnet.",
        "code": "summe = 0\nfor i in range(*START*, *ENDE*):\n    summe += i\n\nprint(summe)",
        "solution": "summe = 0\nfor i in range(1, 101):\n    summe += i\n\nprint(summe)"
    },
    "task4": {
        "description": "Passe den Code so an, dass er die Anzahl der Wörter in einem gegebenen String text zählt.",
        "code": "text = \"Dies ist ein Beispieltext mit mehreren Wörtern.\"\nworter = text.split(*TRENNZEICHEN*)\nanzahl_woerter = len(worter)\n\nprint(anzahl_woerter)",
        "solution": "text = \"Dies ist ein Beispieltext mit mehreren Wörtern.\"\nworter = text.split()\nanzahl_woerter = len(worter)\n\nprint(anzahl_woerter)"
    },
    "task5": {
        "description": "Passe den Code so an, dass er die ersten n Zahlen der Fibonacci-Folge berechnet und ausgibt.",
        "code": "n = 10\nfibonacci = [0, 1]\nfor i in range(2, n):\n    fib = fibonacci[i-1] + fibonacci[i-2]\n    fibonacci.append(*NEUE_ZAHL*)\n\nprint(fibonacci)",
        "solution": "n = 10\nfibonacci = [0, 1]\nfor i in range(2, n):\n    fib = fibonacci[i-1] + fibonacci[i-2]\n    fibonacci.append(fib)\n\nprint(fibonacci)"
    },
    # Weitere Aufgaben
}