from collections import defaultdict
import csv


def read_csv(files: list[str]) -> dict[str, list[int]]:
    raw_data: dict[str, list[int]] = defaultdict(list)
    for file in files:
        with open(file, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_data[row["student"]].append(int(row["coffee_spent"]))
    return raw_data
