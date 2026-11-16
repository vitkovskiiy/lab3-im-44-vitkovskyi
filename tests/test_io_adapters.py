from tetris.io_adapters import FileReader


def test_file_reader_returns_whole_text_of_file(tmp_path):
    path = tmp_path / "input.txt"
    path.write_bytes(b"2 2\n.p\n#.\n")

    assert FileReader().read(str(path)) == "2 2\n.p\n#.\n"
