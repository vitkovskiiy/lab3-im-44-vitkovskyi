from fakes import FakeReader, RecordingWriter
from tetris.app import TetrisApp


def test_run_asks_reader_for_file_at_given_path_once():
    reader = FakeReader(text="1 1\np\n")
    app = TetrisApp(reader=reader, writer=RecordingWriter())

    app.run("input.txt")

    assert reader.requested_paths == ["input.txt"]
