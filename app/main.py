import logging

from config import configure_logging, configure_parser
from constants import COMMAND_LINE_ARGUMENTS, END_HANDLER, ERROR_PARSER, START_HANDLER
from reader import read_csv
from report_functions import median_report
from output import output_data


FUNCTION = {"median-coffee": median_report}


def main():
    configure_logging()
    logging.info(START_HANDLER)

    arg_parser = configure_parser(FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(COMMAND_LINE_ARGUMENTS.format(**vars(args)))

    try:
        raw_data = read_csv(args.files)
        result = FUNCTION[args.report](raw_data)
        if result is not None:
            output_data(result, args.report)
    except FileNotFoundError as error:
        logging.error(f"Файл не найден: {error}")
    except Exception as error:
        logging.info(ERROR_PARSER.format(report=args.report, error=error))

    logging.info(END_HANDLER)


if __name__ == "__main__":
    main()
