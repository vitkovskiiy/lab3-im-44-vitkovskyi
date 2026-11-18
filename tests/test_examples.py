import pytest

from tetris.codec import parse_field, render_field
from tetris.field import drop

# Input/output pairs copied from the assignment PDF.
PDF_EXAMPLES = [
    (
        "7 8\n"
        "..p.....\n"
        ".ppp....\n"
        "..p.....\n"
        "........\n"
        "...#....\n"
        "...#...#\n"
        "#..#####\n",
        "........\n"
        "........\n"
        "..p.....\n"
        ".ppp....\n"
        "..p#....\n"
        "...#...#\n"
        "#..#####\n",
    ),
    (
        "5 6\n"
        "..p...\n"
        "##p.##\n"
        "##pp##\n"
        "##..##\n"
        "##..##\n",
        "......\n"
        "##..##\n"
        "##p.##\n"
        "##p.##\n"
        "##pp##\n",
    ),
]


@pytest.mark.parametrize(
    "input_text, expected_output",
    PDF_EXAMPLES,
    ids=["cross stops on landscape", "piece falls into well"],
)
def test_dropped_field_matches_pdf_example(input_text, expected_output):
    assert render_field(drop(parse_field(input_text))) == expected_output
