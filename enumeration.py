######################################
# Optimisation L3 - 2021/2022        #
# One Pizza is all you need          #
# enumeration.py                     #
######################################

#python enumeration.py a_exemple.txt

import sys
from itertools import product

# Recuperation du probleme dans le fichier txt correspondant
try:
    instance_file = sys.argv[1]
except:
    raise Exception("Erreur à la lecture des arguments. Syntaxe de la commande :\n\
        python3 enumeration.py <chemin_vers_fichier_d_entree>" )
# Liste des ingrédients
listeIngredient = {}
# Ouverture et lecture dans le fichier
file = open(instance_file)
data = file.read().split()
# Incrémenteur dans les aliments du client (deux lignes par clients)
next =1
# Boucle sur le nombre de clients
for i in range(int(data[0])):
    # Nombre d'aliments aimés par le client
    aime = int(data[next])
    if aime != 0:
        # Boucle sur les aliments aimé par le client
        for i in range(aime):
            next +=1
            # Si l'aliment n'est pas dans la liste alors on le rajoute
            if not data[next] in listeIngredient:
                listeIngredient[data[next]] = 1
            
    next +=1
    # Nombre d'aliments détestés par le client
    aimepas = int(data[next])     
    if aimepas !=0:
        # Boucle sur les aliments détestés par le client
        for i in range(aimepas):
            next+=1
            if len(data)!=next:
                # Si l'aliment n'est pas dans la liste alors on le rajoute 
                if not data[next] in listeIngredient:
                    listeIngredient[data[next]] = 0
            else:
                break
    next+=1
print("Liste de tous les ingrédients :")
print(listeIngredient)
n=0
out=""
# Table de vérité des aliments
table = list(product([False, True], repeat=len(listeIngredient)))
# Noms des aliments dans key
key = [k for k, v in listeIngredient.items()]

# Boucle sur les possibilité des solution (2 puissance N)
for t in table:
    # Incrementeur
    num =0
    n+=1
    out+=str(n) + " "
    # Boucle sur le nombre d'aliment
    for i in t:
        if i:
            out+=str(key[num])+" "
        num+=1
    out+="\n"
print(out)

file.close()