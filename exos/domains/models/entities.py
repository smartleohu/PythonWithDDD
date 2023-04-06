from dataclasses import dataclass, field

from .values import Price, Symbol, Weight, Volume
from ...utils.numbers import get_id


@dataclass
class Entity:
    id: int = field(default_factory=get_id().__next__)

    def __eq__(self, other):
        # to do


# Objets d'Entité
@dataclass
class Asset(Entity):
    symbol: Symbol = None
    weight: Weight = None


@dataclass
class MarketData(Entity):
    # to do
