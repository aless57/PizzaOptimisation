######################################
# Optimisation L3 - 2021/2022        #
# One Pizza is all you need          #
# glouton.py                         #
######################################

#Nom des fichiers à ouvrir et à traiter
filesIN=["basefile/a_exemple.txt","basefile/b_basique.txt","basefile/c_grossier.txt","basefile/d_difficile.txt","basefile/e_elabore.txt"]
# Boucle sur les problèmes
for f in filesIN:
    # list out pour la réécriture
    listeIngredientIN = {}
    # Ouverture et lecture dans les fichiers (nom dans 'filesIN')
    with open(f) as file:
        #On sépare chaque élement dans le fichier
        data = file.read().split()
        #On se place sur la ligne de ce que le client 1 aime
        next = 1
        #On boucle sur le nombre de clients
        for i in range(int(data[0])):
            #Nombre d'ingredient qu'aime le client i
            aime = int(data[next])
            if aime != 0:
                for i in range(aime):
                    # On se place sur la ligne de ce que n'aime pas le client i
                    next +=1
                    # INGREDIENT AIME : Si l'ingredient est dans la list out alors on incremente de 1 sinon on le rejoute dedans 
                    if data[next] in listeIngredientIN:
                        listeIngredientIN[data[next]] += 1
                    else:
                        listeIngredientIN[data[next]] = 1
            # On se place sur la ligne de ce que n'aime pas le client i
            next+=1
            # Nombre d'ingredient que n'aime pas le client i
            aimepas = int(data[next])
            if aimepas !=0:
                for i in range(aimepas):
                    # On se place sur la ligne de ce qu'aime le client i+1
                    next +=1
                    # INGREDIENT NON AIME : Si l'ingredient est dans la list out alors on incremente de 1 sinon on le rejoute dedans 
                    if len(data) != next:
                        if data[next] in listeIngredientIN:
                            listeIngredientIN[data[next]] -= 1
                        else:
                            listeIngredientIN[data[next]] = 0
                    else:
                        break
            # On se place sur la ligne de ce qu'aime le client i+1
            next+=1
    
    #Variable pour la reecriture du fichier
    listeIngredientOUT = []
    # On boucle sur chaque element de la list out
    for i in listeIngredientIN:
        # Si l'ingredient est supperieur a 0 alors on l'ajoute dans la reecriture du fichier (<=0 : ingredient detesté de N clients )
        if listeIngredientIN[i] > 0:
            listeIngredientOUT.append(i)
    listeIngredientOUT.insert(0,len(listeIngredientOUT))
    #Split du nom des ficher pour récupérer la lettre du test
    fn = f.split("_")
    fn = fn[0].split("/")
    #Création du fichier et écriture dedans pour la solution des problèmes
    file=open("resGlouton/exemple_solution_"+fn[1]+".txt",'w')
    for tof in listeIngredientOUT:
        file.write(str(tof)+" ")
    file.close()