from Structures.trait import Trait
from Structures.level import TraitLevel
from Structures.colours import Colour

def getTraitColourFromNumber(trait: Trait, number: int) -> str:
    """
    Get the trait colour based on the number of units.
    
    Args:
        trait (Trait): The Trait object.
        number (int): The number of units.
    
    Returns:
        str: The colour associated with the trait level.
    """
    # Iterate through the levels of the trait
    for level in trait.levels:
        # Check if the number of units is within the range defined by minUnits and maxUnits
        if level.minUnits <= number <= level.maxUnits:
            return level.colour
    
    # If no matching level is found, return an empty string or a default value
    return Colour.DISABLED