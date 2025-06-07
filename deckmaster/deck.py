"""Deck model with basic utility methods."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Iterable, List

from .card import Card


@dataclass
class Deck:
    """Represents a collection of cards used in a TCG match."""

    max_size: int = 60
    max_copies: int = 3
    cards: List[Card] = field(default_factory=list)

    def add_card(self, card: Card) -> None:
        if len(self.cards) >= self.max_size:
            raise ValueError("Deck is already at maximum size")
        if self.count_card(card.name) >= self.max_copies:
            raise ValueError(f"Cannot have more than {self.max_copies} copies of {card.name}")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> None:
        for i, c in enumerate(self.cards):
            if c.name == card_name:
                del self.cards[i]
                return
        raise ValueError(f"Card {card_name} not found in deck")

    def count_card(self, card_name: str) -> int:
        return sum(1 for c in self.cards if c.name == card_name)

    def as_counter(self) -> Counter:
        return Counter(c.name for c in self.cards)

    @classmethod
    def from_iterable(cls, items: Iterable[Card]) -> "Deck":
        deck = cls()
        for card in items:
            deck.add_card(card)
        return deck

    def __str__(self) -> str:
        counts = self.as_counter()
        lines = [f"{cnt}x {name}" for name, cnt in sorted(counts.items())]
        return "\n".join(lines)
