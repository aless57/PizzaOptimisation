DEMANGE Alessi & NOEL Victor - Licence 3 Informatique

Projet Pizza Optimisation

Pour chacun des programmes, la documentation est précise pour comprendre notre fonctionnement.

DOSSIER basefile
Ce dossier comporte tous les fichier txt de test donnés au début.

DOSSIER resGenetique
Ce dossier comporte le resultat du programme genetique.py

DOSSIER resGlouton
Ce dossier comporte le resultat du programme glouton.py


SOLUTION ENUMERATION
Pour l'affichage de toutes les solutions (toutes les recettes), il faut lancer le programme appelé "enumeration.py"
-Dans le terminal : "python3 enumeration.py basefile/<fichier.txt>" où fichier.txt correspond au problème choisi en format .txt
Pour chaque problème, le résultat se trouve dans le fichier enumeration.txt (cela écrit automatiquement lors du lancement du programme)
et dans le terminal on voit l'enumeration de toutes les solutions.
PS : pour les problèmes D et E, le nombre de solutions est gigantesque donc la mémoire se sature trop vite mais cela peut être testé
pour les problèmes A B et C.

SOLUTION GENETIQUE
Avant de lancer le programme il faut installer la librairie pygad avec cette commande :
pip3 install pygad
-Le programme se lance avec cette commande : "python3 genetique.py"
Les resultats du programme se trouve dans le dossier resGenetique.
Le programme se lance sans aucun souci si les problèmes en ".txt" n'ont pas changé de nom, si vous avez changé les noms des problèmes,
il faut les mettre à jour aux lignes 95 à 99

SOLUTION GLOUTON
Pour trouver la solution optimale à chacun des problèmes, il suffit de lancer le programme qui se nomme "glouton.py" sans aucun argument.
-Dans le terminal : "python3 glouton.py"
Le programme se lance sans aucun souci si les problèmes en ".txt" n'ont pas changé de nom, si vous avez changé les noms des problèmes,
il faut les mettre à jour dans le tableau du fichier main.py ligne 2.
La solution est automatiquement générée. Par exemple pour le programme a_exemple.txt, la solution se nomme "exemple_solution_A.txt"
Le programme d'évaluation peut donc se lance de cette façon : python3 evaluation.py basefile/a_example.txt resGlouton/exemple_solution_A.txt

SCORE EVALUATION:
enumeration :
A : 2
B : 5
C : 5
D : impossible
E : impossible

genetique :
A : 2
B : 3
C : 2
D : 1303
E : 352

glouton :
A : 2
B : 5 
C : 5
D : 1706
E : 966