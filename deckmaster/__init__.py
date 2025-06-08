"""DeckMasterTCG - Tools for building trading card game decks.

This package provides models and utilities to help build and manage
trading card game (TCG) decks. It includes a simple command line
interface for creating and modifying decks.
"""

__all__ = ["Card", "Deck", "generate_deck"]

from .card import Card
from .deck import Deck
from .generator import generate_deck
