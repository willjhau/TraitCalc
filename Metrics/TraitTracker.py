from Structures.board import Board
from Structures.unit import Unit
from Structures.trait import Trait
from Structures.level import TraitLevel
from Structures.colours import Colour

def evaluate(board: Board, units: dict, traits: dict, critical = 8) -> int:
    """
    Evaluate the board and calculate the trait levels and unit counts.
    
    Args:
        board (Board): The Board object representing the team composition.
        units (dict): A dictionary of Unit objects.
        traits (dict): A dictionary of Trait objects.
    
    Returns:
        int: A number representing the fitness of the board.
    """

    # Initialize trait counts
    numberOfActiveTraits = 0

    activeTraits = board.getActiveTraits()
    for trait in activeTraits:
        if (activeTraits[trait][1] != Colour.DISABLED
            and activeTraits[trait][1] != Colour.UNIQUE_ACTIVE):
            numberOfActiveTraits += 1

    totalUnitCost = 0

    for unit in board.getUnits():
        totalUnitCost += units[unit].cost

    # Calculate the number of units
    numberOfUnits = len(board.getUnits())

    # Calculate a fitness score
    # Number of active traits is a positive trait
    # Total unit cost is a negative trait
    # Fewer units is a positive trait
    fitness = 0
    fitness += numberOfActiveTraits * 100
    if numberOfActiveTraits == critical:
        fitness += 10000
    fitness -= numberOfUnits * 5
    fitness -= totalUnitCost * 3

    return fitness
    
    