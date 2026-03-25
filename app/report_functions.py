import statistics


def median_report(raw_data: dict[str, list[int]]) -> dict[str, float]:
    result = {student: statistics.median(money) for student, money in raw_data.items()}
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
