from app.report_functions import median_report

def test_sorted(median_report_files):
    result = median_report(median_report_files)
    assert result == {
        'Иван Кузнецов': 700,
        'Алексей Смирнов': 450,
        'Дарья Петрова': 250.0,
        'Мария Соколова': 100
    }

def test_empty_raw_data():
    assert median_report({}) == {}
