"""Utilities to generate decks based on a rulebook and card library."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict

from .card import Card
from .deck import Deck


def load_rulebook(path: Path) -> Dict[str, int]:
    """Load rulebook JSON and return as a dict."""
    data = json.loads(path.read_text())
    return data


def load_library(path: Path) -> List[Card]:
    """Load card library JSON and return list of :class:`Card`."""
    data = json.loads(path.read_text())
    return [Card(**c) for c in data.get("cards", [])]


def generate_deck(rulebook_path: Path, library_path: Path) -> Deck:
    """Generate a deck using the provided rulebook and library.

    Parameters
    ----------
    rulebook_path:
        Path to a JSON file containing ``max_size`` and ``max_copies``.
    library_path:
        Path to a JSON file with a ``cards`` list describing available cards.
    """
    rules = load_rulebook(rulebook_path)
    library = load_library(library_path)

    max_size = int(rules.get("max_size", 60))
    max_copies = int(rules.get("max_copies", 3))

    deck = Deck(max_size=max_size, max_copies=max_copies)

    if not library:
        return deck

    idx = 0
    attempts = 0
    # Try adding cards until deck is filled or attempts exceed a safe limit
    limit = len(library) * max_copies * 2
    while len(deck.cards) < deck.max_size and attempts < limit:
        card = library[idx % len(library)]
        if deck.count_card(card.name) < deck.max_copies:
            deck.add_card(card)
        idx += 1
        attempts += 1
    return deck
