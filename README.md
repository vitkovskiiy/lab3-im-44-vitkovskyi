# Лабораторна робота №3 — Tetris (Test doubles)

- Студент: Іван Вітковський
- Група: ІМ-44
- Pull request: [PR URL]
- Демо-відео (необов'язково): [DEMO VIDEO URL]

Програма читає початковий стан екрана гри, схожої на Тетріс (одна «підвішена»
фігура `p` і «ландшафт» `#`), і виводить стан після того, як фігура впала.
Якщо вхідний файл некоректний або його не вдалося прочитати, програма виводить
`Error: invalid input` без подробиць.

## Встановлення

```bash
pip install -r requirements.txt
```

## Тести

```bash
pytest
```

## Шари програми

| Шар | Модуль | Що робить |
|---|---|---|
| Логічний | `src/tetris/field.py` | `Point`, `Field`, `step_down` (зсув на 1 рядок), `drop` (падіння до упору) |
| Логічний | `src/tetris/codec.py` | `parse_field` (текст → поле, перевірка коректності), `render_field` (поле → текст) |
| Введення/виведення | `src/tetris/io_adapters.py` | `FileReader` (файл), `ConsoleWriter` (стандартний вивід) |
| Комунікаційний | `src/tetris/app.py` | `TetrisApp(reader, writer)` — DI через конструктор: читає, рахує, виводить |
| Точка входу | `src/tetris/cli.py` | збирає `TetrisApp` зі справжніми `FileReader` і `ConsoleWriter` |

Комунікаційний шар тестується з власноруч написаними test doubles
(`tests/fakes.py`: `FakeReader`, `RecordingWriter`), без бібліотек для mock'ів.
Property-based тести (`tests/test_properties.py`) теж написані без бібліотек:
власний генератор полів, 6 властивостей, 1000 полів з фіксованим seed.

## Приклад запуску

Вхідний файл `examples/example1.txt`:

```
7 8
..p.....
.ppp....
..p.....
........
...#....
...#...#
#..#####
```

Запуск:

```bash
python -m src.tetris examples/example1.txt
```

Вивід:

```
........
........
..p.....
.ppp....
..p#....
...#...#
#..#####
```
