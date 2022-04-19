######################################
# Optimisation L3 - 2021/2022        #
# One Pizza is all you need          #
# enumeration.py                     #
######################################

#python enumeration.py a_exemple.txt

import sys
from itertools import product

try:
    instance_file = sys.argv[1]
except:
    raise Exception("Erreur à la lecture des arguments. Syntaxe de la commande :\n\
        python3 enumeration.py <chemin_vers_fichier_d_entree>" )
listeIngredient = {}
file = open(instance_file)
data = file.read().split()
next =1
for i in range(int(data[0])):
    aime = int(data[next])
    if aime != 0:
        for i in range(aime):
            next +=1
            if not data[next] in listeIngredient:
                listeIngredient[data[next]] = 1
            
    next +=1
    aimepas = int(data[next])     
    if aimepas !=0:
        for i in range(aimepas):
            next+=1
            if len(data)!=next: 
                if not data[next] in listeIngredient:
                    listeIngredient[data[next]] = 0
            else:
                break
    next+=1
print("Liste de tous les ingrédients :")
print(listeIngredient)
n=0
out=""
table = list(product([False, True], repeat=len(listeIngredient)))
key = [k for k, v in listeIngredient.items()]
for t in table:
    num =0
    n+=1
    out+=str(n) + " "
    for i in t:
        if i:
            out+=str(key[num])+" "
        num+=1
    out+="\n"
print(out)

file.close()