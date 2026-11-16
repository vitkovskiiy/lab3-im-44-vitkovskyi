from tetris.cli import main


def test_main_prints_dropped_field_for_input_file_path(tmp_path, capsys):
    path = tmp_path / "input.txt"
    path.write_text("3 3\n.p.\n...\n#.#\n", encoding="utf-8")

    main([str(path)])

    assert capsys.readouterr().out == "...\n.p.\n#.#\n"
