from pydantic import BaseModel, Field

from typing import Optional, List, Dict, Any

class Unit(BaseModel):
    """
    Represents a unit with its properties.
    """

    name: str = Field(
        ...,
        description="The name of the unit."
    )

    cost: int = Field(
        ...,
        description="The cost of the unit."
    )

    traits: List[str] = Field(
        ...,
        description="List of traits associated with the unit."
    )

    frontline: bool = Field(
        False,
        description="Indicates if the unit is a frontline unit."
    )

    damageType: str = Field(
        ...,
        description="The type of damage the unit deals."
    )