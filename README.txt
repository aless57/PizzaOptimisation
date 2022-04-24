DEMANGE Alessi & NOEL Victor - Licence 3 Informatique

Projet Pizza Optimisation

Pour chacun des programmes, la documentation est précise pour comprendre notre fonctionnement.

SOLUTION ENUMERATION
Pour l'affichage de toutes les solutions (toutes les recettes), il faut lancer le programme appelé "enumeration.py"
Dans le terminal : "python3 enumeration.py <fichier.txt>" où fichier.txt correspond au problème choisi en format .txt
Pour chaque problème, le résultat se trouve dans le fichier enumeration.txt (cela écrit automatiquement lors du lancement du programme)
et dans le terminal on voit l'enumeration de toutes les solutions.
PS : pour les problèmes D et E, le nombre de solutions est gigantesque donc la mémoire se sature trop vite mais cela peut être testé
pour les problèmes A B et C.

SOLUTION GENETIQUE
pip3 install pygad

SOLUTION OPTIMALE
Pour trouver la solution optimale à chacun des problèmes, il suffit de lancer le programme qui se nomme "main.py" sans aucun argument.
Dans le terminal : "python3 main.py"
Le programme se lance sans aucun souci si les problèmes en ".txt" n'ont pas changé de nom, si vous avez changé les noms des problèmes,
il faut les mettre à jour dans le tableau du fichier main.py ligne 2.
La solution est automatiquement générée. Par exemple pour le programme a_exemple.txt, la solution se nomme "exemple_solution_A.txt"
Le programme d'évaluation peut donc se lance de cette façon : python3 evaluation.py a_example.txt exemple_solution_A.txt