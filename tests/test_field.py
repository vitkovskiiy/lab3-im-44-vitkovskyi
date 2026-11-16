from tetris.field import Field, Point, drop, step_down


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


def test_step_down_leaves_field_unchanged_when_piece_is_on_bottom_row():
    field = Field(
        height=2,
        width=3,
        piece=frozenset({Point(1, 0), Point(1, 1)}),
        landscape=frozenset(),
    )

    assert step_down(field) == field


def test_step_down_leaves_field_unchanged_when_landscape_is_directly_below_piece():
    field = Field(
        height=4,
        width=3,
        piece=frozenset({Point(0, 1), Point(1, 1)}),
        landscape=frozenset({Point(2, 1), Point(3, 0), Point(3, 1)}),
    )

    assert step_down(field) == field


def test_drop_moves_piece_down_until_it_rests_on_landscape():
    field = Field(
        height=5,
        width=2,
        piece=frozenset({Point(0, 0), Point(0, 1)}),
        landscape=frozenset({Point(4, 1)}),
    )

    assert drop(field) == Field(
        height=5,
        width=2,
        piece=frozenset({Point(3, 0), Point(3, 1)}),
        landscape=frozenset({Point(4, 1)}),
    )
