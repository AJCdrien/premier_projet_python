"""
Created on Wed Jul 24 10:12:32 2019

@author: utilisateur
"""

from random import randint
entier = randint(1,1000)
print ("Bienvenue au Juste Prix !")

for nb_essais in range(1,11):
    print("Il vous reste",11 - nb_essais, "essai(s).")
    entree = int(input("Entrez un prix : \n"))
    if nb_essais != 10:
        if entree < entier:
            print("C'est plus !")
        elif entree > entier:
            print("C'est moins !")
    else:
        print("C'est gagné !")
        break

if entree != entier:
    print("C'est perdu ! Le juste prix était", entier, "!")
print ("Merci d'avoir participé !")
