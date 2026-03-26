from tabulate import tabulate


def output_data(data: dict[str, int], report_name: str) -> None:
    columns = ["student", report_name]
    print(tabulate(data.items(), headers=columns, tablefmt="grid"))
