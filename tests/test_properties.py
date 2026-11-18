"""Hand-written property-based tests (no property-testing libraries).

A generator builds random valid fields, each property compares the initial
and the final field, and the loop checks every property on many fields.
Each case uses its own seed, so a failure can be reproduced from the message.
"""

import random

import pytest

from tetris.codec import render_field
from tetris.field import Field, Point, drop

BASE_SEED = 20261116
CASES = 1000


def generate_field(rng: random.Random) -> Field:
    """Random size, random landscape at the bottom, one piece above it."""
    height = rng.randint(2, 10)
    width = rng.randint(1, 10)
    piece_rows = rng.randint(1, max(1, height // 2))
    landscape = frozenset(
        Point(row, col)
        for row in range(piece_rows, height)
        for col in range(width)
        if rng.random() < 0.35
    )
    candidates = [Point(row, col) for row in range(piece_rows) for col in range(width)]
    piece = frozenset(rng.sample(candidates, rng.randint(1, min(4, len(candidates)))))
    return Field(height, width, piece, landscape)


def size_is_unchanged(initial: Field, final: Field) -> None:
    assert (final.height, final.width) == (initial.height, initial.width), "size changed"


def landscape_is_unchanged(initial: Field, final: Field) -> None:
    assert final.landscape == initial.landscape, "landscape changed"


def piece_pixel_count_is_unchanged(initial: Field, final: Field) -> None:
    assert len(final.piece) == len(initial.piece), "piece pixel count changed"


def piece_keeps_shape_and_only_moves_down(initial: Field, final: Field) -> None:
    shift = min(p.row for p in final.piece) - min(p.row for p in initial.piece)
    moved = frozenset(Point(p.row + shift, p.col) for p in initial.piece)
    assert shift >= 0 and final.piece == moved, "piece changed shape or moved sideways/up"


def piece_is_inside_field_and_off_landscape(initial: Field, final: Field) -> None:
    for p in final.piece:
        assert 0 <= p.row < final.height and 0 <= p.col < final.width, f"{p} is outside the field"
        assert p not in final.landscape, f"{p} overlaps the landscape"


def final_field_is_stable(initial: Field, final: Field) -> None:
    assert drop(final) == final, "dropping the final field again changes it"


PROPERTIES = [
    size_is_unchanged,
    landscape_is_unchanged,
    piece_pixel_count_is_unchanged,
    piece_keeps_shape_and_only_moves_down,
    piece_is_inside_field_and_off_landscape,
    final_field_is_stable,
]


def test_generator_builds_valid_fields():
    for case in range(CASES):
        seed = BASE_SEED + case
        field = generate_field(random.Random(seed))
        assert field.piece, f"seed={seed}: empty piece"
        assert not field.piece & field.landscape, f"seed={seed}: piece overlaps landscape"


@pytest.mark.parametrize("prop", PROPERTIES, ids=lambda prop: prop.__name__)
def test_property_holds_for_random_fields(prop):
    for case in range(CASES):
        seed = BASE_SEED + case
        initial = generate_field(random.Random(seed))
        final = drop(initial)
        try:
            prop(initial, final)
        except AssertionError as error:
            pytest.fail(
                f"{prop.__name__} failed for seed={seed}: {error}\n"
                f"initial field ({initial.height}x{initial.width}):\n{render_field(initial)}"
                f"final field:\n{render_field(final)}"
            )
