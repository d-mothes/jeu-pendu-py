import sys
import random
import threading
import time

ascii_art = """"

██████████████████████████████████████████████████████████████████████
███▄─▄█▄─▄▄─█▄─██─▄███▄─▄▄▀█▄─██─▄███▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█▄─██─▄█
█─▄█─███─▄█▀██─██─█████─██─██─██─█████─▄▄▄██─▄█▀██─█▄▀─███─██─██─██─██
█▄▄▄███▄▄▄▄▄██▄▄▄▄████▄▄▄▄███▄▄▄▄████▄▄▄███▄▄▄▄▄█▄▄▄██▄▄█▄▄▄▄███▄▄▄▄██
"""


niveaudi = ""
mot_random = []

def clear() :
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

with open('./lib/game.py') as fichier:
    code = fichier.read()

def selection_liste(mode):
    if mode == "1":
        with open("./lib/liste/liste_facile.txt", "r") as fichier:
            mot = fichier.read().splitlines()
        return mot

    elif mode == "2":
        with open("./lib/liste/liste_normal.txt", "r") as fichier:
            mot = fichier.read().splitlines()
        return mot

    elif mode == "3":
        with open("./lib/liste/liste_difficile.txt", "r") as fichier:
            mot = fichier.read().splitlines()
        return mot

    else:
        print("Mode invalide")
        return []

clear()
print(ascii_art , """
Selectionnez un mode de jeu : (1) Facile, (2) Normal, (3) Difficile""")
choix_mode = str(input("$:")).strip()
while choix_mode not in  ["1", "2", "3"] :
    clear()
    print(ascii_art, """
Choix invalide veuillez reselectionner :
Selectionnez un mode de jeu : (1) Facile, (2) Normal, (3) Difficile""")
    choix_mode = str(input("$:")).strip()

clear()
while True :
    if choix_mode == "1" :
        niveaudi = "Facile"
    if choix_mode == "2" :
        niveaudi = "Normal"
    if choix_mode == "3" :
        niveaudi = "Difficile"

    mots = selection_liste(choix_mode)

    if not mots:
        print(ascii_art)
        print("Erreur : liste de mots vide ou mode invalide")
        break
    solution = random.choice(mots)
    while solution in mot_random :
        solution = random.choice(mots)
    mot_random.append(solution)
    exec(code)
    choix = str(input("Voulez-vous continuer de jouer ? (o/n) : ")).strip().upper()
    while choix not in ["O", "N"]:
        clear()
        print(ascii_art)
        print("Choix invalide, veuillez re selectionner")
        choix = str(input("Voulez-vous continuer de jouer ? (o/n) : ")).strip().upper()
    if choix != "O" :
        exit()
    clear()
    print(ascii_art)
    cnt = str(input("voulez vous changer de mode de difficulte ? (o/n) : ")).strip().upper()
    while cnt not in ["O", "N"]:
        clear()
        print(ascii_art)
        print("Choix invalide, veuillez re selectionner")
        cnt = str(input("voulez vous changer de mode de difficulte ? (o/n) : ")).strip().upper()
    if cnt == "O" :
        clear()
        print(ascii_art)
        print("Selectionnez un mode de jeu : (1) Facile, (2) Normal, (3) Difficile")
        mode = str(input("$:")).strip()
        while mode not in ["1", "2", "3"]:
            clear()
            print(ascii_art, """
Choix invalide veuillez reselectionner :
Selectionnez un mode de jeu : (1) Facile, (2) Normal, (3) Difficile""")
            mode = str(input("$:")).strip()
        clear()

    elif cnt == "N" :
        clear()