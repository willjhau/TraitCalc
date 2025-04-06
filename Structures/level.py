from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from Structures.colours import Colour

class TraitLevel(BaseModel):
    """
    Represents a trait level with its colour
    """

    minUnits: int = Field(
        ...,
        description="The minimum number of units required for the trait level."
    )
    maxUnits: int = Field(
        ...,
        description="The maximum number of units allowed for the trait level."
    )
    colour: Colour = Field(
        ...,
        description="The colour associated with the trait level."
    )