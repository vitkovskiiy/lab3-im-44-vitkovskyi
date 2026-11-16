from fakes import FakeReader, RecordingWriter
from tetris.app import TetrisApp


def test_run_asks_reader_for_file_at_given_path_once():
    reader = FakeReader(text="1 1\np\n")
    app = TetrisApp(reader=reader, writer=RecordingWriter())

    app.run("input.txt")

    assert reader.requested_paths == ["input.txt"]


def test_run_writes_dropped_field_to_writer_exactly_once():
    reader = FakeReader(text="3 2\np.\n..\n.#\n")
    writer = RecordingWriter()
    app = TetrisApp(reader=reader, writer=writer)

    app.run("input.txt")

    assert writer.written == ["..\n..\np#\n"]
