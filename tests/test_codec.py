from tetris.codec import parse_field
from tetris.field import Field, Point


def test_parse_field_reads_size_and_splits_pixels_into_piece_and_landscape():
    text = "3 4\n.pp.\n....\n#..#\n"

    assert parse_field(text) == Field(
        height=3,
        width=4,
        piece=frozenset({Point(0, 1), Point(0, 2)}),
        landscape=frozenset({Point(2, 0), Point(2, 3)}),
    )
