import json
import sys

ascii_art = """"

██████████████████████████████████████████████████████████████████████
███▄─▄█▄─▄▄─█▄─██─▄███▄─▄▄▀█▄─██─▄███▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█▄─██─▄█
█─▄█─███─▄█▀██─██─█████─██─██─██─█████─▄▄▄██─▄█▀██─█▄▀─███─██─██─██─██
█▄▄▄███▄▄▄▄▄██▄▄▄▄████▄▄▄▄███▄▄▄▄████▄▄▄███▄▄▄▄▄█▄▄▄██▄▄█▄▄▄▄███▄▄▄▄██
"""

tentatives = 7
lettres_utilisees = []
affichage = ""
lettres_trouvees = ""
search = 0
number_string = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear() :
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def pendu() :
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|/ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:
        print("/||           ")
    if tentatives<=6:
        print("==============")
    if tentatives==0:
        print("perdu le mot etait " , solution)

for lettre in solution:
    affichage += "_ "

while tentatives > 0:
    if search == 0 :
        print(ascii_art)
    print("Mot a deviner : ", affichage)
    print("Lettre deja utilisee : " , lettres_utilisees)
    print("Proposez une lettre : ")
    proposition = input("$:").lower().strip()
    search += 1


    if proposition in lettres_utilisees:
        clear()
        print(ascii_art)
        print("Lettre deja utilisee")

    elif proposition in number_string:
        clear()
        print(ascii_art)
        print("On utilise des lettres pas des nombres")

    elif proposition == "" :
        clear()
        print(ascii_art)
        print("' ' nest pas une lettre")

    elif len(proposition) > 1 :
        clear()
        print(ascii_art)
        print("une seul lettre à la fois")

    else:
        if proposition in solution:
            lettres_utilisees.append(proposition)
            lettres_trouvees += proposition
            clear()
            print(ascii_art)
            print("C'est juste !")
        else:
            lettres_utilisees.append(proposition)
            tentatives -= 1
            clear()
            print(ascii_art)
            print("Faux, il vous reste", tentatives, "tentatives")

    pendu()
    if tentatives==0:
        break

    affichage = ""
    for lettre in solution:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "

    if "_" not in affichage:
            print("Gagne ! Le mot etait :", solution)
            break