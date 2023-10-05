#! /usr/bin/env python3
# coding:utf8
import random
import time
import string


# On saisit le mot de passe qu'on doit trouver
mot_de_passe = input("Saisir le mot de passe a trouver :")

# On définit le fonction
def pwd_aleatoire():
    lettres = string.ascii_letters + '"!@#$%^&*()"' #
    chiffres = [str(i) for i in range(1, 11)]
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv: # boucle tant que le caractère suivant ne correspond pas au caractère du mot de passe
            print(resultat + suiv)
            time.sleep(0.05) 
            suiv = random.choice(lettres + "".join(chiffres))
        resultat += suiv
    return resultat


debut = time.time()
print(pwd_aleatoire())
print("Durée : " + str(time.time() - debut) + " secondes")
