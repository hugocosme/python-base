#!/usr/bin/env python3
"""Imprime a tabuada
"""

__version__ = "0.1.0"
__author__ = "Hugo Cosme <hugocr@msn.com>"
__license__ = "Unlicense"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

print(numeros)

# iterable (percorriveis)
for numero in numeros:
    print("tabuada do", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-----------------")