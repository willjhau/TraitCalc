from Structures.board import Board
from Structures.unit import Unit
from Structures.trait import Trait
from Structures.level import TraitLevel
import random

def generateIndividual(traits: dict, units: dict, size: int) -> Board:
    """
    Generate a random individual for the team composition.
    
    Args:
        traits (dict): A dictionary of Trait objects.
        units (dict): A dictionary of Unit objects.
        size (int): The size of the team.
    
    Returns:
        Board: A Board object representing the generated team composition.
    """

    if size < 1 or size > 15:
        raise ValueError("Size must be between 1 and 15.")
    if size > len(units):
        raise ValueError("Size must not exceed the number of available units.")

    # Create a new board
    board = Board()
    
    # Randomly select {size} units from the unit pool
    selected_units = random.sample(list(units.keys()), size)

    # Add the selected units to the board
    for unit_name in selected_units:
        unit = units[unit_name]
        board.addUnit(unit)

    
    return board