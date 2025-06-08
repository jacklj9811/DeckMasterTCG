"""Command line interface for DeckMasterTCG."""

import argparse
import json
from pathlib import Path

from .card import Card
from .deck import Deck
from .generator import generate_deck


def load_deck(path: Path) -> Deck:
    if not path.exists():
        return Deck()
    data = json.loads(path.read_text())
    cards = [Card(**c) for c in data.get("cards", [])]
    return Deck.from_iterable(cards)


def save_deck(deck: Deck, path: Path) -> None:
    data = {"cards": [c.__dict__ for c in deck.cards]}
    path.write_text(json.dumps(data, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="DeckMasterTCG CLI")
    parser.add_argument("deck_file", type=Path, help="Path to deck JSON file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add = subparsers.add_parser("add", help="Add a card to the deck")
    add.add_argument("name")
    add.add_argument("type")
    add.add_argument("cost", type=int)

    remove = subparsers.add_parser("remove", help="Remove a card by name")
    remove.add_argument("name")

    generate = subparsers.add_parser("generate", help="Generate deck from rulebook and library")
    generate.add_argument("rulebook", type=Path)
    generate.add_argument("library", type=Path)

    subparsers.add_parser("show", help="Display deck contents")

    args = parser.parse_args(argv)
    deck = load_deck(args.deck_file)

    if args.command == "add":
        deck.add_card(Card(name=args.name, type=args.type, cost=args.cost))
        save_deck(deck, args.deck_file)
    elif args.command == "remove":
        deck.remove_card(args.name)
        save_deck(deck, args.deck_file)
    elif args.command == "show":
        print(deck)
    elif args.command == "generate":
        deck = generate_deck(args.rulebook, args.library)
        save_deck(deck, args.deck_file)
        print(deck)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
