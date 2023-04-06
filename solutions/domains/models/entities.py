from dataclasses import dataclass, field

from solutions.domains.models.values import Price, Symbol, Weight, Volume
from solutions.utils.numbers import get_id


@dataclass
class Entity:
    id: int = field(default_factory=get_id().__next__)

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.id == other.id


# Objets d'Entité
@dataclass
class Asset(Entity):
    symbol: Symbol = None
    weight: Weight = None


@dataclass
class MarketData(Entity):
    symbol: Symbol = None
    price: Price = None
    volume: Volume = None
