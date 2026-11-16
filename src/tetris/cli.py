import sys

from .app import TetrisApp
from .io_adapters import ConsoleWriter, FileReader


def main(argv: list[str] | None = None) -> None:
    args = sys.argv[1:] if argv is None else argv
    TetrisApp(reader=FileReader(), writer=ConsoleWriter()).run(args[0])
