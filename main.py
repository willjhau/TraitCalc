"""
This is the entry point for the TraitCalc program.
The purpose of TraitCalc is to calculate the optimal team
composition for a given set of traits and units in the game TFT.

It optimises based on a custom-designed fitness function
"""

from Processing.loadData import loadData
from Processing.generateIndividual import generateIndividual
from Structures.board import Board
import config as cfg
from Selection.tournament import tournamentSelection
from Crossover.randomSplit import crossover
from Mutation.mutate import mutate
from math import floor
from Outputs.hotStorage import Store
from bruteForce import bruteForceBestTeam

from Metrics.TraitTracker import evaluate


def main(set: int, teamSize: int, fitnessFunction = evaluate, verbose = False, storeOutputs: Store = None):
    """
    Main function to load data and initialise optimisation.
    
    Args:
        set (int): The set number to load data for.
    """
    # Load data
    if verbose:
        print(f"Loading data for set {set}...")
    units, traits = loadData(set)
    
    # Generate initial population
    if verbose:
        print(f"Generating initial population of size {cfg.POPULATION_SIZE}...")
    population = []
    population_size = cfg.POPULATION_SIZE
    for _ in range(population_size):
        individual = generateIndividual(units, traits, teamSize)
        population.append(individual)

    prev_best_fitness = None
    stale_generations = 0
    patience = cfg.CONVERGENCE_PATIENCE  # Number of generations to wait before stopping
    threshold = cfg.CONVERGENCE_THRESHOLD  # Minimum improvement to consider progress

    hasConverged = False
    generationNumber = 0
    maxGenerations = cfg.MAX_GENERATIONS
    while (generationNumber <= maxGenerations):
        generationNumber += 1
        if verbose:
            print(f"Generation {generationNumber}...")
            print(f"Evaluating fitness of population...")
        # Evaluate the fitness of each individual in the population
        
        fitnessScores = [evaluate(individual, units, traits) for individual in population]
        
        if storeOutputs is not None:
            for i, score in enumerate(fitnessScores):
                if score > 10000:
                    board = population[i].getUnits()
                    # Check if the board is already stored
                    if not storeOutputs.checkMatch(board):
                        storeOutputs.add(board, score)
        

        if verbose:
            print(f"Fitness scores: {fitnessScores}")
        # Check for convergence
        # Check if the best fitness has improved significantly
        best_fitness = max(fitnessScores)

        if verbose:
            print(f"Best fitness in generation {generationNumber}: {best_fitness}")

        # if prev_best_fitness is not None and abs(best_fitness - prev_best_fitness) < threshold:
        #     if verbose:
        #         print(f"Stale generation detected. No significant improvement.")
        #     stale_generations += 1
        # else:
        #     stale_generations = 0
        #     prev_best_fitness = best_fitness

        # if stale_generations >= patience:
        #     if verbose:
        #         print(f"Convergence reached. No significant improvement for {stale_generations} generations.")
        #     hasConverged = True
        #     print(f"Converged after {generationNumber} generations with best fitness: {best_fitness}")
        #     break

        if verbose:
            print(f"Generating next generation...")
        # Generate the next generation
        # Select the best individuals for reproduction
        nextGeneration = []

        # Elitism

        if verbose:
            print(f"Applying elitism...")
        elitism_count = floor(cfg.ELITISM_RATE * population_size)
        best_individuals = sorted(zip(population, fitnessScores), key=lambda x: x[1], reverse=True)[:elitism_count]
        nextGeneration.extend([ind[0] for ind in best_individuals])
        # Remove the best individuals from the population
        population = [ind for ind in population if ind not in nextGeneration]

        if verbose:
            print(f"Populating next generation with elitism...")
        # Populate the rest of the next generation
        while len(nextGeneration) < population_size:
            # Tournament selection
            parents = tournamentSelection(population, fitnessFunction, units, traits, cfg.TOURNAMENT_SIZE)

            # Crossover
            offspring = crossover(parents[0], parents[1], teamSize, units, traits)

            # Mutation
            offspring = mutate(offspring, teamSize, units, traits)

            # Add the offspring to the next generation
            nextGeneration.append(offspring)
        
        population = nextGeneration

    # Final evaluation of the best individual
    best_individual = max(population, key=lambda ind: fitnessFunction(ind, units, traits))
    best_fitness = fitnessFunction(best_individual, units, traits)

    # Return the best individual and its fitness
    return best_individual, best_fitness



    


if __name__ == "__main__":
    # Example usage
    # set_number = 14  # Example set number
    # team_size = 7  # Example team size
    # trials = 20  # Number of trials to run

    # store = Store()

    # boards =[]
    # for _ in range(trials):
    #     sol, fitness = main(set_number, team_size, fitnessFunction=evaluate, verbose=True, storeOutputs=store)
    #     boards.append((sol, fitness))
    
    # for i, board in enumerate(boards):
    #     print(f"{board[0].getUnits()} - {board[1]}")

    # for board in store.getBoards():
    #     print(f"{" ".join(board[0])} - {board[1]}")
    units, traits = loadData(14)

    best = bruteForceBestTeam(units, traits, 6, fitness_fn=evaluate)

    print(f"Best team: {best.getUnits()} - {evaluate(best, units, traits)}")



