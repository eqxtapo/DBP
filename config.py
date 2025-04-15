import os

# Получаем абсолютный путь до текущей директории
ROOT_DIR = os.path.dirname(__file__)

# Создаем путь до директории data
DATA_DIR = os.path.join(ROOT_DIR, "data")

# Создаем путь до файла vacancies.json относительно текущей директории.
REL_INI_DIR = os.path.join(DATA_DIR, "../data/database.ini")
INI_DIR = os.path.abspath(REL_INI_DIR)
