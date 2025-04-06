import random
from Structures.board import Board
from Structures.unit import Unit
from typing import List, Dict

def crossover(parent1: Board, parent2: Board, teamSize: int, units: dict, traits: dict) -> Board:
    """
    Combines two parent Boards into a child Board using randomised half-and-fill crossover.
    Units are added to the new Board using board.addUnit().
    """
    p1_units = [unit for unit in parent1.units]
    p2_units = [unit for unit in parent2.units]

    # Random split point
    split = random.randint(1, teamSize - 1)

    # Start with a new, empty board
    child = Board()

    # Add first half from parent1
    added = set()
    for name in p1_units[:split]:
        child.addUnit(name, units, traits)
        added.add(name)

    # Add units from parent2, avoiding duplicates
    for name in p2_units:
        if name not in added and len(child.units) < teamSize:
            child.addUnit(name, units, traits)
            added.add(name)

    # Fill from global unit pool if needed
    all_unit_names = list(units.keys())
    remaining = list(set(all_unit_names) - added)
    while len(child.units) < teamSize:
        choice = random.choice(remaining)
        child.addUnit(choice, units, traits)
        remaining.remove(choice)

    return child
