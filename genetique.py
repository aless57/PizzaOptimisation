######################################
# Optimisation L3 - 2021/2022        #
# One Pizza is all you need          #
# genetique.py                       #
######################################

from dataclasses import dataclass, field
import pygad

# Classe des clients
@dataclass
class Client:
    aime: set[str]
    nonaime: set[str]

# Classe des probleme
@dataclass
class Probleme:
    client: list[Client] = field(default_factory=list)
    all_ingredients: set = field(default_factory=set)
    solution: set = field(default_factory=set)
    score: int = 0

    # Permet de mettre a jour un nouveau client
    def reset(instance):
        instance.client = []
        instance.all_ingredients = set()
        instance.solution = set()
        instance.score = 0

    # Permet d'ajouter un client
    def ajouterClient(instance, client):
        instance.client.append(client)
        instance.all_ingredients |= client.aime

    # Permet d'evaluer la pizza en fonction des clients 
    def evaluation(instance, pizza: set[str]) -> int:
        result = 0
        # Boucle sur la liste des clients 
        for c in instance.client:
            if (c.aime & pizza == c.aime and c.nonaime & pizza == set()):
                result += 1
        return result

    # Permet de résoudre via l'algorithme génétique pour obtenir le score d'une recette et cette recette
    def resoudre(instance, generations):
        ingr_list = sorted(list(instance.all_ingredients))

        # Fitness de l'algo
        def fitness(solution, solution_idx):
            pizza = set([ingr_list[k] for (k,v) in enumerate(solution) if v == 1])
            return instance.evaluation(pizza)

        ga_instance = pygad.GA(
            num_generations=generations,
            num_parents_mating=2,
            sol_per_pop=3,
            num_genes=len(ingr_list),
            fitness_func=fitness,
            init_range_low=0,
            init_range_high=2,
            mutation_num_genes=1,
            random_mutation_min_val=0,
            random_mutation_max_val=2,
            mutation_by_replacement=True,
            gene_type=int,
            stop_criteria="saturate_10")

        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        instance.solution = set([ingr_list[k] for (k,v) in enumerate(solution) if v == 1])
        instance.score = solution_fitness

    # Recuperation des données via ouverture de fichier et ecriture dans le dossier out
    def process(instance, filename, generations):
        instance.reset()
        with open(f"{filename}.txt") as f:
            n = int(f.readline())
            for i in range(n):
                client = Client(
                    set(f.readline().strip().split()[1:]),
                    set(f.readline().strip().split()[1:])
                )
                instance.ajouterClient(client)

            instance.resoudre(generations)

        with open(f"resGenetique/{filename}.out.txt", "w") as f:
            f.write(f"{len(instance.solution)} ")
            f.write(" ".join(instance.solution))

#Initialisation du probleme
p = Probleme()
p.process("a_exemple", 1000)
p.process("b_basique", 1000)
p.process("c_grossier", 1000)
p.process("d_difficile", 1000)
p.process("e_elabore", 1000)
print("Resultat dans resGenetique")