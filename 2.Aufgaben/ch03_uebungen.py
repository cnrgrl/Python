# Aufgabe 1: Hochzählen von 1 bis  n 
    # Schreiben Sie ein Programm, das die Zahlen von 1 bis n ausgibt.
"""
erstezahl=1
n = int(input('Gibt eine Zahl: '))

while erstezahl<=n:
    print(erstezahl, end=' ')
    erstezahl+=1
"""
# Aufgabe 2: Hochzählen von 1 bis n mit Schrittweite 2
    # Schreiben Sie ein Programm, das jede zweite Zahl zwischen 1 bis n ausgibt.
"""
erstezahl = 1
n = int(input('Gibt eine Zahl: '))

while (erstezahl<=n):
    print(erstezahl, end=',')
    erstezahl += 2
"""

# Aufgabe 3: Runterzählen von n bis 1
    # Schreiben Sie ein Programm, das von n bis 1 runterzählt.
"""
n = int(input('Gibt eine Zahl: '))

while (int(n)>=1):
    print(n, end=',')
    n -= 1
"""
# Aufgabe 4: Runterzählen von  n  bis 1 mit Schrittweite 2
    # Schreiben Sie ein Programm, das von (n bis k < n) in Schritten zu 2 runterzählt.
"""
erstezahl = int(input('Gibt Erstezahl: ')) #n
letztezahl = int(input('Gibt Letztezahl: ')) #k

while erstezahl >= letztezahl:
    print(erstezahl, end=',')
    erstezahl -= 2
"""