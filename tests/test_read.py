import pytest

from app.read import read_csv


def test_read_single_csv(one_csv_file):
    result = read_csv([one_csv_file])
    assert result == {
        'Алексей Смирнов': [450, 550, 300],
        'Дарья Петрова': [200, 300],
        'Иван Кузнецов': [700],
        'Мария Соколова': [100]
    }
    assert isinstance(result, dict)
    assert all(isinstance(v, list) for v in result.values())
    assert all(isinstance(v, list) for v in result.values())


def test_read_lot_csv(multiple_csv_files):
    result = read_csv(multiple_csv_files)
    assert result == {
        'Алексей Смирнов': [450, 550, 200, 100, 300, 100],
        'Дарья Петрова': [200, 200, 200],
    }


def test_empty_file(empty_csv_file):
    result = read_csv([empty_csv_file])
    assert result == {}


def test_file_wrong_data(csv_files_wrong_data):
    with pytest.raises(KeyError):
        read_csv([csv_files_wrong_data])


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv(["none.csv"])
