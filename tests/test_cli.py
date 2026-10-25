import pytest

from fibonacci_kata.cli import build_parser, main


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["10"])
    assert args.n == 10


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "0", "--end", "7"])
    assert args.start == 0
    assert args.end == 7


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "10"])
    main()
    assert capsys.readouterr().out.strip() == "55"


def test_main_prints_range(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "0", "--end", "7"],
    )
    main()
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["0", "1", "1", "2", "3", "5", "8", "13"]


def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata"])
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_negative_number(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "-1"])
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_negative_range(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "-1", "--end", "5"],
    )
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_invalid_range(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "5", "--end", "2"],
    )
    with pytest.raises(SystemExit):
        main()


def test_main_requires_both_range_arguments(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "0"],
    )
    with pytest.raises(SystemExit):
        main()
