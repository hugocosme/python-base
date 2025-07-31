#!/usr/bin/env python3
"""
Hello World multilinguage example.

USAGE:
tenha a variavel LANG setada para o idioma desejado.
Exemplo: export LANG=pt_BR

execution:
python3 hello.py
"""
__version__ = "1.0.0"
__author__ = "Hugo Cosme <hugocr@msn.com>"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "es_ES":
    msg = "¡Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, le monde!"

print(msg)