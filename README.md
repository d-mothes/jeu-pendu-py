# 🎮 Jeu du Pendu (Python)

Petit jeu du **pendu** en **Python** jouable dans le terminal, avec **3 modes de difficulté** (Facile / Normal / Difficile) et possibilité d’enchaîner plusieurs parties.

---

## ✅ Fonctionnalités

- Affichage ASCII du titre + du pendu
- 3 difficultés (listes de mots différentes)
- Vérification des entrées :
  - empêche les chiffres
  - empêche les entrées vides
  - empêche de saisir plusieurs lettres
  - empêche de rejouer une lettre déjà utilisée
- Rejouer une partie à la fin
- Option pour changer la difficulté entre deux parties

---

## 📦 Prérequis

- **Python 3.x**
- Un terminal (Windows / Linux / macOS)

---

## 🗂️ Structure du projet

> Le code charge des fichiers via `./lib/...`, donc garde cette structure :

```text
.
├── main.py
└── lib
    ├── game.py
    └── liste
        ├── liste_facile.txt
        ├── liste_normal.txt
        └── liste_difficile.txt
