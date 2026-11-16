import sys


class FileReader:
    def read(self, path: str) -> str:
        with open(path, encoding="utf-8-sig") as f:
            return f.read()


class ConsoleWriter:
    def write(self, text: str) -> None:
        sys.stdout.write(text)
