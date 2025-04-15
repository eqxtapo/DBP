from configparser import ConfigParser

from config import INI_DIR


def connect_params():
    """Функция возвращает параметры для подключения к БД"""

    parser = ConfigParser()
    parser.read(INI_DIR)

    db = {}
    params = parser.items("postgresql")
    for param in params:
        db[param[0]] = param[1]

    return db
