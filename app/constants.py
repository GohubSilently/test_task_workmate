from pathlib import Path

BASE_DIR = Path(__file__).parent

# Логирование
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "parser.log"
SIZE_LOG = 10**6
DT_FORMAT = "%d.%m.%Y %H:%M:%S"
LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"

START_HANDLER = "Обработчик запущен!"
END_HANDLER = "Обработчик завершил работу!"
COMMAND_LINE_ARGUMENTS = "Передаваемые файлы {files}. Режим обработки {report}."
ERROR_PARSER = "Ошибка при работе парсера в режиме: {report} - {error}"
