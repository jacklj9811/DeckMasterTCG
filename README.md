# DeckMasterTCG
Your Ultimate Companion for Crafting Practically Perfect TCG Decks. This tool is designed to bring your deck-building strategy to life, ensuring your TCG decks perform precisely as envisioned in the game.

## Generating Decks

Decks can be automatically generated from a rulebook and card library stored as
JSON files:

```bash
python -m deckmaster.cli mydeck.json generate rules.json library.json
```

The rulebook file should define `max_size` and `max_copies` while the library
file contains a list of cards.
