import pytest


@pytest.fixture
def one_csv_file(tmp_path):
    algebra_csv = tmp_path / 'algebra.csv'
    algebra_csv.write_text(
        'student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n'
        'Алексей Смирнов,2024-06-01,450,4.5,12,норм,Алгебра\n'
        'Алексей Смирнов,2024-06-03,550,3.5,16,зомби,Алгебра\n'
        'Дарья Петрова,2024-06-01,200,7.0,6,отл,Алгебра\n'
        'Дарья Петрова,2024-06-03,300,6.0,9,норм,Алгебра\n'
        'Иван Кузнецов,2024-06-03,700,2.0,18,не выжил,Алгебра\n'
        'Мария Соколова,2024-06-01,100,8.0,3,отл,Алгебра\n'
        'Алексей Смирнов,2024-06-03,300,3.5,16,зомби,Алгебра\n',
        encoding='utf-8'
    )
    return algebra_csv

@pytest.fixture
def multiple_csv_files(tmp_path):
    algebra_csv = tmp_path / 'algebra.csv'
    physic_csv = tmp_path / 'physic.csv'
    russian_csv = tmp_path / 'russian.csv'
    algebra_csv.write_text(
        'student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n'
        'Алексей Смирнов,2024-06-01,450,4.5,12,норм,Алгебра\n'
        'Алексей Смирнов,2024-06-03,550,3.5,16,зомби,Алгебра\n'
        'Дарья Петрова,2024-06-01,200,7.0,6,отл,Алгебра\n'
    )
    physic_csv.write_text(
        'student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n'
        'Алексей Смирнов,2024-06-01,200,4.5,12,норм,Физика\n'
        'Алексей Смирнов,2024-06-03,100,3.5,16,зомби,Физика\n'
        'Дарья Петрова,2024-06-01,200,7.0,6,отл,Физика\n'
    )
    russian_csv.write_text(
        'student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n'
        'Алексей Смирнов,2024-06-01,300,4.5,12,норм,Русский язык\n'
        'Алексей Смирнов,2024-06-03,100,3.5,16,зомби,Русский язык\n'
        'Дарья Петрова,2024-06-01,200,7.0,6,отл,Русский язык\n'
    )

    return [algebra_csv, physic_csv, russian_csv]

@pytest.fixture
def empty_csv_file(tmp_path):
    empty_csv = tmp_path / 'empty.csv'
    empty_csv.write_text(
        'student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n',
        encoding="utf-8"
    )
    return empty_csv

@pytest.fixture
def csv_files_wrong_data(tmp_path):
    wrong_csv = tmp_path / 'wrong.csv'
    wrong_csv.write_text(
        'date,sleep_hours,study_hours,mood,exam\n'
        '2024-06-01,4.5,12,норм,Русский язык\n'
        '2024-06-01,7.0,6,отл,Физика\n'
    )
    return wrong_csv

@pytest.fixture
def median_report_files():
    raw_data = {
        'Алексей Смирнов': [450, 550, 300],
        'Дарья Петрова': [200, 300],
        'Иван Кузнецов': [700],
        'Мария Соколова': [100]
    }
    return raw_data
