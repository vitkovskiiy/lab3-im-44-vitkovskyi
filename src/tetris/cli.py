import sys

from .app import ERROR_MESSAGE, TetrisApp
from .io_adapters import ConsoleWriter, FileReader


def main(argv: list[str] | None = None) -> None:
    args = sys.argv[1:] if argv is None else argv
    writer = ConsoleWriter()
    if len(args) != 1:
        writer.write(ERROR_MESSAGE)
        return
    TetrisApp(reader=FileReader(), writer=writer).run(args[0])
