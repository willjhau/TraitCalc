from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from Structures.colours import Colour
from Structures.level import TraitLevel

class Trait(BaseModel):
    """
    Represents a trait with its properties and effects.
    """
    name: str = Field(
        ...,
        description="The name of the trait."
        )
    
    unique: bool = Field(
        False,
        description="Indicates if the trait is unique (only one instance can exist)."
    )

    levels: List[TraitLevel] = Field(
        ...,
        description="List of levels for the trait."
    )

    emblem: bool = Field(
        False,
        description="Indicates if the trait has an emblem."
    )

    units: List[str] = Field(
        ...,
        description="List of units associated with the trait."
    )

if __name__ == "__main__":
    # Example usage
    enforcer_trait = {
        "name": "Enforcer",
        "unique": False,
        "emblem": True,
        "units": ["Maddie", "Steb", "Camille", "Loris", "Twisted Fate", "Vi", "Caitlyn"],
        "levels": [
            {
                "minUnits": 2,
                "maxUnits": 3,
                "colour": "BRONZE"
            },
            {
                "minUnits": 4,
                "maxUnits": 5,
                "colour": "SILVER"
            },
            {
                "minUnits": 6,
                "maxUnits": 7,
                "colour": "GOLD"
            },
            {
                "minUnits": 8,
                "maxUnits": 9,
                "colour": "GOLD"
            },
            {
                "minUnits": 10,
                "maxUnits": 30,
                "colour": "PRISMATIC"
            },

        ]
    }

    enforcer = Trait(**enforcer_trait)
    print(enforcer)

