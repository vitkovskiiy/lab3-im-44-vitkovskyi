from tetris.field import Field, Point, step_down


def test_step_down_moves_piece_one_row_down_when_space_below_is_free():
    field = Field(
        height=3,
        width=3,
        piece=frozenset({Point(0, 1)}),
        landscape=frozenset(),
    )

    assert step_down(field) == Field(
        height=3,
        width=3,
        piece=frozenset({Point(1, 1)}),
        landscape=frozenset(),
    )
