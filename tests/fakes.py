"""Hand-written test doubles for the communication layer (no mock libraries)."""


class FakeReader:
    """Returns prepared text (or raises a prepared error) and records requested paths."""

    def __init__(self, text: str = "", error: Exception | None = None):
        self._text = text
        self._error = error
        self.requested_paths: list[str] = []

    def read(self, path: str) -> str:
        self.requested_paths.append(path)
        if self._error is not None:
            raise self._error
        return self._text


class RecordingWriter:
    """Remembers every text it was asked to write, in order."""

    def __init__(self):
        self.written: list[str] = []

    def write(self, text: str) -> None:
        self.written.append(text)
