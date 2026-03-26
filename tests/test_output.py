from app.output import output_data


def test_output(capsys):
    data = {
        'Иван Кузнецов': 700,
        'Алексей Смирнов': 450,
        'Дарья Петрова': 250.0,
        'Мария Соколова': 100
    }
    output_data(data, 'median-coffee')
    output = capsys.readouterr().out

    assert 'Иван Кузнецов' in output
    assert 'Алексей Смирнов' in output
    assert 'median-coffee' in output
