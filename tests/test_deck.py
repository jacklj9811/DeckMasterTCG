import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from deckmaster.card import Card
from deckmaster.deck import Deck


def test_add_card_increases_count():
    deck = Deck(max_size=10, max_copies=3)
    card = Card("Fireball", "Spell", 2)
    deck.add_card(card)
    assert deck.count_card("Fireball") == 1


def test_cannot_exceed_max_copies():
    deck = Deck(max_size=10, max_copies=2)
    card = Card("Goblin", "Creature", 1)
    deck.add_card(card)
    deck.add_card(card)
    try:
        deck.add_card(card)
    except ValueError as e:
        assert "more than" in str(e)
    else:
        raise AssertionError("Expected ValueError")


def test_remove_card():
    deck = Deck(max_size=10)
    card = Card("Elf", "Creature", 1)
    deck.add_card(card)
    deck.remove_card("Elf")
    assert deck.count_card("Elf") == 0
