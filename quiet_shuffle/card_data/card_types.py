from dataclasses import dataclass, field
from enum import Enum

class Creature(Enum):
    CAT = "cat"
    SQUIRREL = "squirrel"
    MONKEY = "monkey"
    ALPACA = "alpaca"

class Season(Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"

class CreatureSeason(Enum):
    cat = "winter"
    squirrel = "spring"
    monkey = "summer"
    alpaca = "fall"

@dataclass
class Card:
    creature: Creature = field(default_factory=Creature)
    spell = "Spell"
    artifact = "Artifact"
    enchantment = "Enchantment"
    season: Season = field(default_factory=Season)
    
    def __init__(self, creature: Creature, season: Season):
        self.creature = creature
        self.season = season

    def __str__(self):
        return f"{self.creature.name.capitalize()} {self.season.value.capitalize()}"
