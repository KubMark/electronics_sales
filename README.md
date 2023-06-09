# Проект Electronics sales

## 

Проект использует следующие технологии:

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+
## Установка

## 1. Создаем виртуальное окружение.

```sh
# для первичной установки
poetry install
# активация окружения
poetry shell
```
## 2. Создайте свой .env файл в корне проекта.

## 3. Заполните .env файл следующими значениями
```sh
SECRET_KEY="esales"
DEBUG=True
POSTGRES_USER=esales
POSTGRES_PASSWORD=esales
POSTGRES_DB=esales
POSTGRES_HOST=localhost
```
## 4. Создать миграции.
```sh
./manage.py makemigrations
```
## 5. Применить миграции.
```sh
./manage.py migrate
```
## 5. Запустить проект.
```sh
./manage.py runserver
```

## Описание:
Реализована модель сети по продаже электроники.