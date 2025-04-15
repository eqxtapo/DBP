# Проект 3. Поиск вакансий с подключением БД

## Описание

В рамках проекта необходимо получить данные о компаниях и вакансиях с сайта hh.ru,
спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

## Установка:

1. Клонируйте репозиторий:

```
https://github.com/eqxtapo/BDP/
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
exclude = .git, __pycache__
```

Файл pyproject.toml

black, isort, mypy
```
[tool.black]
line_length = 119
exclude = '''
/(
  | \.git
)/
'''

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = '''
/(
  | \.venv
)/
'''
```

5. Установите библиотеку requests и dotenv.
 
```
poetry add requests
poetry add python-dotenv
```

6. Установите библиотеку psycopg2 для работы с БД
````
poetry add psycopg2
````

# Модули

## Модуль Main
В модуле реализована основная работа по взаимодействию с пользователем.

## Модуль db_manager
Содержит класс DBManager который подключается к БД PostgreSQL.

## Модуль db_connect
Обеспечивает подключение к БД

## Модуль vacancy
Подключается к hh.ru, и получает список работодателей

## Модуль utils
Содержит основной функционал для работы с БД.