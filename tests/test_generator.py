import json
from deckmaster.generator import generate_deck


def test_generate_deck_respects_rulebook(tmp_path):
    rulebook = {"max_size": 5, "max_copies": 2}
    library = {
        "cards": [
            {"name": "Fireball", "type": "Spell", "cost": 2},
            {"name": "Goblin", "type": "Creature", "cost": 1},
        ]
    }
    rule_path = tmp_path / "rules.json"
    lib_path = tmp_path / "library.json"
    rule_path.write_text(json.dumps(rulebook))
    lib_path.write_text(json.dumps(library))

    deck = generate_deck(rule_path, lib_path)

    assert len(deck.cards) == 4
    assert deck.count_card("Fireball") <= 2
    assert deck.count_card("Goblin") <= 2
