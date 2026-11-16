from dataclasses import dataclass
from typing import NamedTuple


class Point(NamedTuple):
    row: int
    col: int


@dataclass(frozen=True)
class Field:
    height: int
    width: int
    piece: frozenset[Point]
    landscape: frozenset[Point]


def step_down(field: Field) -> Field:
    moved = frozenset(Point(p.row + 1, p.col) for p in field.piece)
    return Field(field.height, field.width, moved, field.landscape)
