import random
from icecream import ic

def tournamentSelection(population, fitness_fn, units, traits, k, num_parents=2, verbose=False):
    selected = []
    if verbose:
        for i in range(num_parents):
            print(f"Round {i+1}")
            contenders = random.sample(population, k)
            for j, ind in enumerate(contenders):
                fitness = fitness_fn(ind, traits, units)
                print(f"Contender {j+1}: {ind} - Fitness: {fitness}")

            best = max(contenders, key=lambda ind: fitness_fn(ind, units, traits))
            selected.append(best)
            print(f"Selected: {best}")
    else:
        for i in range(num_parents):
            contenders = random.sample(population, k)
            best = max(contenders, key=lambda ind: fitness_fn(ind, units, traits))
            selected.append(best)

    return selected

if __name__ == "__main__":
    # Example usage
    population = ["ind1", "ind2", "ind3", "ind4", "ind5"]
    fitness_fn = lambda ind, units, traits: random.random()  # Dummy fitness function
    traits = {}
    units = {}
    k = 3
    num_parents = 2

    parents = tournamentSelection(population, fitness_fn, units, traits, k, num_parents, verbose=True)
    print(parents)