from typing import List
from Structures.trait import Trait
from Structures.unit import Unit
from Processing.getTraitColourFromNumber import getTraitColourFromNumber
from Structures.colours import Colour

class Board:
    """
    Class representing a team in the game.
    """

    def __init__(self):
        self.units = set()
        self.activeTraits = {}

    def addUnit(self, unit, units: List[Unit], traits: List[Trait]):
        """
        Add a unit to the team.
        
        Args:
            unit: The unit to add.
        """
        self.units.add(unit)

        for trait in units[unit].traits:
            if trait in self.activeTraits:
                newVal = self.activeTraits[trait][0] + 1
                newColour = getTraitColourFromNumber(traits[trait], newVal)
                self.activeTraits[trait] = (newVal, newColour)
            else:
                newColour = getTraitColourFromNumber(traits[trait], 1)
                self.activeTraits[trait] = (1, newColour)

    def removeUnit(self, unit, units, traits):
        """
        Remove a unit from the team.
        
        Args:
            unit: The unit to remove.
        """
        if unit not in self.units:
            raise ValueError(f"Unit {unit} not in team.")

        self.units.discard(unit)

        for trait in units[unit].traits:
            if trait in self.activeTraits:
                newVal = self.activeTraits[trait][0] - 1
                if newVal == 0:
                    del self.activeTraits[trait]
                else:
                    newColour = getTraitColourFromNumber(traits[trait], newVal)
                    self.activeTraits[trait] = (newVal, newColour) 
            else:
                raise ValueError(f"Trait {trait} not in active traits.")


    def getUnits(self):
        """
        Get the list of units in the team.
        
        Returns:
            List of units in the team.
        """
        return list(self.units)
    
    def getActiveTraits(self):
        """
        Get the active traits of the team.
        
        Returns:
            Dictionary of active traits.
        """
        return self.activeTraits
    
    
    def clear(self):
        """
        Clear the team.
        """
        self.units.clear()
        self.activeTraits.clear()

    def __contains__(self, unit):
        """
        Check if a unit is in the team.
        
        Args:
            unit: The unit to check.
        
        Returns:
            bool: True if the unit is in the team, False otherwise.
        """
        return unit in self.units
    
    def __len__(self):
        """
        Get the number of units in the team.
        
        Returns:
            int: The number of units in the team.
        """
        return len(self.units)
    
    def __iter__(self):
        """
        Iterate over the units in the team.
        
        Returns:
            Iterator over the units in the team.
        """
        return iter(self.units)



    def __repr__(self):
        return f"Board(units={self.units})"
    
    def __str__(self):
        retVal = ""
        for unit in self.units:
            retVal += f"{unit} "
        if not retVal:
            return "No units in board."
        retVal += "\n"
        for trait in self.activeTraits:
            if self.activeTraits[trait][1] != Colour.DISABLED:
                retVal += f"{trait}: {self.activeTraits[trait][0]} {self.activeTraits[trait][1]} units\n"
        return retVal.strip()
