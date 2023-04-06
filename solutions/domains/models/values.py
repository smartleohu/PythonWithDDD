from dataclasses import dataclass


@dataclass(frozen=True)
class Symbol:
    name: str


@dataclass(frozen=True)
class Price:
    value: float


@dataclass(frozen=True)
class Volume:
    value: float


@dataclass(frozen=True)
class Weight:
    value: float

