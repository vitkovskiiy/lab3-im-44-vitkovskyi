from tetris.io_adapters import FileReader


def test_file_reader_returns_whole_text_of_file(tmp_path):
    path = tmp_path / "input.txt"
    path.write_bytes(b"2 2\n.p\n#.\n")

    assert FileReader().read(str(path)) == "2 2\n.p\n#.\n"


def test_file_reader_drops_utf8_byte_order_mark(tmp_path):
    # Notepad and PowerShell's "Set-Content -Encoding UTF8" add a BOM.
    path = tmp_path / "input.txt"
    path.write_bytes(b"\xef\xbb\xbf2 2\n.p\n#.\n")

    assert FileReader().read(str(path)) == "2 2\n.p\n#.\n"
