from typing import Protocol


class Reader(Protocol):
    def read(self, path: str) -> str: ...


class Writer(Protocol):
    def write(self, text: str) -> None: ...


class TetrisApp:
    """Connects the game logic with input/output; both are injected."""

    def __init__(self, reader: Reader, writer: Writer):
        self._reader = reader
        self._writer = writer

    def run(self, path: str) -> None:
        self._reader.read(path)
