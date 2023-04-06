from dataclasses import dataclass
from typing import List

from solutions.domains.models.entities import Asset, Entity


@dataclass
class Portfolio(Entity):
    assets: List[Asset] = None

    def total_weight(self):
        return sum(asset.weight.value for asset in self.assets)
