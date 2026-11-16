from .field import Field, Point


def parse_field(text: str) -> Field:
    lines = text.splitlines()
    height, width = (int(n) for n in lines[0].split())
    piece = set()
    landscape = set()
    for row, line in enumerate(lines[1 : 1 + height]):
        for col, char in enumerate(line):
            if char == "p":
                piece.add(Point(row, col))
            elif char == "#":
                landscape.add(Point(row, col))
    return Field(height, width, frozenset(piece), frozenset(landscape))


def render_field(field: Field) -> str:
    lines = []
    for row in range(field.height):
        line = ""
        for col in range(field.width):
            point = Point(row, col)
            if point in field.piece:
                line += "p"
            elif point in field.landscape:
                line += "#"
            else:
                line += "."
        lines.append(line + "\n")
    return "".join(lines)
