import random
from typing import List

from quiet_shuffle.card_data.card_types import Card, Creature, Season, CreatureSeason


def create_deck() -> List[Card]:
    return [Card(creature=Creature(cs.name), season=Season(cs.value)) for cs in CreatureSeason]

def shuffle_deck(deck: List[Card]) -> List[Card]:
    random.shuffle(deck)
    return deck

def draw_card(deck: List[Card]) -> Card:
    card_i = random.randint(0, len(deck) - 1)
    card = deck[card_i]
    return card
    