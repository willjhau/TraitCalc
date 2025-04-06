from Structures.trait import Trait
from Structures.unit import Unit
from typing import List, Dict, Tuple
import json
import os

def loadData(setNumber: int) -> Tuple[Dict[str, Unit], Dict[str, Trait]]:
    """
    Load data from JSON files and create Trait and Unit objects.
    
    Args:
        setNumber (int): The set number to load data for.
    Returns:
        Tuple[Dict[str, Trait], Dict[str, Unit]]: A tuple containing dictionaries of Trait and Unit objects.
    """
    # Load all files in Sets/{setNumber}/Traits/

    traits_data = []
    for file in os.listdir(f"Sets/{setNumber}/Traits/"):
        if file.endswith(".json"):
            with open(f"Sets/{setNumber}/Traits/{file}", "r") as f:
                traits_data.append(json.load(f))
    # Create a dictionary to store the traits
    traits_dict = {}
    for trait in traits_data:
        # Create a Trait object
        trait_obj = Trait(**trait)
        # Add the Trait object to the dictionary
        traits_dict[trait_obj.name] = trait_obj
    
    # Load all files in Sets/{setNumber}/Units/
    units_data = []
    for file in os.listdir(f"Sets/{setNumber}/Units/"):
        if file.endswith(".json"):
            with open(f"Sets/{setNumber}/Units/{file}", "r") as f:
                units_data.append(json.load(f))
    # Create a dictionary to store the units
    units_dict = {}
    for unit in units_data:
        # Create a Unit object
        unit_obj = Unit(**unit)
        # Add the Unit object to the dictionary
        units_dict[unit_obj.name] = unit_obj

    # toRemove = []
    # for unit in units_dict.values():
    #     if unit.cost == 4 or unit.cost == 5:
    #         toRemove.append(unit.name)
    # for unit in toRemove:
    #     del units_dict[unit]

    # Return the dictionaries of traits and units
    return units_dict, traits_dict
    
if __name__ == "__main__":
    # Example usage
    set_number = 14
    units, traits = loadData(set_number)
    print("Traits:")
    for trait_name, trait in traits.items():
        print(f" - {trait_name}: {trait}")
    print("Units:")
    for unit_name, unit in units.items():
        print(f" - {unit_name}: {unit}")

