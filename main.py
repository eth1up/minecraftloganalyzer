# main file for a logging system analyzer using Python.

import os
import subprocess
import time
import sys

fertig = False
while fertig == False:
    try:
        pfad = input("Wo befindet sich die Datei? ")
        valid = open(pfad)
        valid.close()
        fertig = True
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden! Bitte kontrolliere deinen angegebenen Pfad!")



    with open(pfad, "r") as log_file:
        inhalt = log_file.read()

        if "" in inhalt:
            print("Es gibt einen Fehler!")
            print("Analyzing further...")
            fehlerexistiert = True
        else:
            print("Es gibt keinen Fehler! Alles passt!")
            sys.exit()

