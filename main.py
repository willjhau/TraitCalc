"""
This is the entry point for the TraitCalc program.
The purpose of TraitCalc is to calculate the optimal team
composition for a given set of traits and units in the game TFT.

It optimises based on a custom-designed fitness function
"""

from loadData import loadData

def main(set: int):
    """
    Main function to load data and initialise optimisation.
    
    Args:
        set (int): The set number to load data for.
    """
    # Load data
    traits, units = loadData(set)
    
    # Initialize the game with the loaded data
    # (Game initialization code goes here)