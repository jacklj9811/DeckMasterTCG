"""Card model for DeckMasterTCG.

This module defines a simple data structure representing a card
in a trading card game. The attributes are intentionally generic
so the module can be used for a variety of games.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """Represents a trading card.

    Attributes
    ----------
    name: str
        The card name.
    type: str
        The card type (e.g. creature, spell).
    cost: int
        The resource cost required to play the card.
    """

    name: str
    type: str
    cost: int

    def __str__(self) -> str:
        return f"{self.name} ({self.type}) - cost: {self.cost}"
