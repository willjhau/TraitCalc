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


from Metrics.TraitTracker import evaluate


def main(set: int, teamSize: int):
    """
    Main function to load data and initialise optimisation.
    
    Args:
        set (int): The set number to load data for.
    """
    # Load data
    traits, units = loadData(set)
    
    # Generate initial population
    initial_population = []
    population_size = cfg.POPULATION_SIZE
    for _ in range(population_size):
        individual = generateIndividual(traits, units, teamSize)
        initial_population.append(individual)

    for i, individual in enumerate(initial_population):
        # Evaluate the fitness of the individual
        fitness = evaluate(individual, units, traits)
        print(f"Individual {i}: Fitness = {fitness}")
    


if __name__ == "__main__":
    # Example usage
    set_number = 14  # Example set number
    team_size = 8  # Example team size
    main(set_number, team_size)
