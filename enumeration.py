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
            else:
                listeIngredient[data[next]] += 1
            
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
                    listeIngredient[data[next]] += -1
            else:
                break
    next+=1
out=""
n=0
# Table de vérité des aliments
table = list(product([False, True], repeat=len(listeIngredient)))
# Noms des aliments dans key
key = [k for k, v in listeIngredient.items()]
allRes = []
res = ""
# Boucle sur les possibilité des solution (2 puissance N)
for t in table:
    # Incrementeur
    num =0
    # Boucle sur le nombre d'aliment
    for i in t:
        if i:
            n+=1
    out+=str(n) + " "
    for i in t:
        if i:
            out+=str(key[num])+" "
        num+=1  
    n=0  
    out+="\n"
print("Liste de toutes les solutions")
print(out)
tabOut = out.splitlines()
tabOut.remove('0 ')
#------------------------------- TEST du score pour chaque solution (copie de evaluation.py)
data = []
with open(instance_file, "r") as f:
        data = f.readlines()
data = [l.strip().split() for l in data]
Nclients = int(data[0][0]) 
data.pop(0)
ingredients = dict()
noms_ingredients = []
Ningredients = 0
L = [set() for _ in range(Nclients)] 
D = [set() for _ in range(Nclients)] 
for client in range(Nclients):
    Lc,Dc = data[2*client][1:], data[2*client+1][1:] 
    for nom_ingr in Lc + Dc:
        if nom_ingr not in ingredients: 
            ingredients[nom_ingr] = Ningredients 
            noms_ingredients.append(nom_ingr)
            Ningredients += 1 
    L[client] = {ingredients[i] for i in Lc}
    D[client] = {ingredients[i] for i in Dc}
    
solutionOptimale = ""
meilleureScore = 0
for i in tabOut:
    data_soluce = [i]
    data_soluce = data_soluce[0].split(" ")
    data_soluce.remove('')
    n_ingredients_soluce, data_soluce = int(data_soluce[0]), data_soluce[1:] 
    solution_set = {ingredients[nom_ingr] for nom_ingr in data_soluce} 
    score = 0
    for c in range(Nclients):
        if L[c].issubset(solution_set) and len(D[c].intersection(solution_set))==0:
            score += 1  
    #Mettre à jour la solution optimale
    if meilleureScore<score:
        solutionOptimale=str(i)
        meilleureScore=score
#-------------------------------- FIN du test de score

# Ouverture et écriture de la meilleure solution dans le fichier evaluation.txt
fileout = open("resEnumeration/enumeration.txt","w")
fileout.write(solutionOptimale)
fileout.close()
file.close()
print("Resultat dans enumeration.txt (meilleure solution)")