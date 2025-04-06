import random
from Structures.board import Board
import config as cfg

def mutate(individual: Board, teamSize: int, units: dict, traits: dict):
    """
    Mutates the given board in-place with a chance of replacing each unit.
    Ensures no duplicate units.
    """
    OUTER_MUTATION_RATE = cfg.OUTER_MUTATION_RATE
    INNER_MUTATION_RATE = cfg.INNER_MUTATION_RATE

    if random.random() > OUTER_MUTATION_RATE:
        return individual

    current_unit_names = [unit for unit in individual.units]
    available_unit_names = list(set(units.keys()) - set(current_unit_names))

    for i in range(len(current_unit_names)):
        if random.random() < INNER_MUTATION_RATE and available_unit_names:
            # Remove the unit
            removed_unit = random.choice(list(individual.units))
            individual.removeUnit(removed_unit, units, traits)

            # Choose a new unique unit
            new_unit_name = random.choice(available_unit_names)
            available_unit_names.remove(new_unit_name)

            # Add the new unit
            individual.addUnit(new_unit_name, units, traits)

    # If there are still available units, add them to the board
    while len(individual.units) < teamSize and available_unit_names:
        new_unit_name = random.choice(available_unit_names)
        individual.addUnit(new_unit_name, units, traits)
        available_unit_names.remove(new_unit_name)

    # If the board has more than teamSize units, remove excess
    while len(individual.units) > teamSize:
        removed_unit = random.choice(list(individual.units))
        individual.removeUnit(removed_unit, units, traits)

    return individual