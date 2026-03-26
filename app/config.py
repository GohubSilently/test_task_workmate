import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import DT_FORMAT, LOG_DIR, LOG_FILE, LOG_FORMAT, SIZE_LOG


def configure_parser(available_report_funtion):
    parser = argparse.ArgumentParser(
        allow_abbrev=False, description="Обработка csv-файлов"
    )
    parser.add_argument(
        "--files",
        "-f",
        nargs="+",
        required=True,
        help="Файлы, которые нужно обработать",
    )
    parser.add_argument(
        "--report",
        "-r",
        choices=available_report_funtion,
        required=True,
        help="Название режима",
    )
    return parser


def configure_logging():
    LOG_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(LOG_FILE, maxBytes=SIZE_LOG, backupCount=5)
    logging.basicConfig(
        level=logging.INFO,
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        encoding="utf-8",
        handlers=(rotating_handler, logging.StreamHandler()),
    )
