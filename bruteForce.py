import itertools
from Structures.board import Board

def bruteForceBestTeam(units: dict, traits: dict, teamSize: int, fitness_fn) -> Board:
    """
    Brute-force all combinations of units of a given team size and return the best board
    according to the provided fitness function.

    Args:
        units (dict): All available units, keyed by name.
        traits (dict): All traits.
        teamSize (int): Number of units per team.
        fitness_fn (function): Function to evaluate each Board's fitness.

    Returns:
        Board: The best Board found.
    """
    best_fitness = float('-inf')
    best_board = None
    unit_names = list(units.keys())

    count = 0
    for combo in itertools.combinations(unit_names, teamSize):
        count += 1
        if count % 1000000 == 0:
            print(f"Checked {count} combinations...")
        board = Board()
        for name in combo:
            board.addUnit(name, units, traits)

        fitness = fitness_fn(board, units, traits)

        if fitness > 10000:
            print(f"{" ".join(board.getUnits())} - {fitness}")
        if fitness > best_fitness:
            best_fitness = fitness
            best_board = board

    return best_board