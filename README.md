# README #

# Установка виртуального окружения и зависимостей #

* Установка виртуальной среды: python3 -m venv venv
* Активация виртуальный среды: source venv/bin/activate
* Обновить pip: pip3 install --upgrade pip
* Утановка зависимостий из файла requirments.txt: pip3 install -r requirements.txt
* Отключение виртуальной среды: deactivate

# Обновление файла requirements.txt #

Если в момент работы с проектом вы добавляете новую библиотеку, необходимо обновить файл requirements.txt

* Команда для обновления файла: pip freeze > requirements.txt

# Структура проекта #

* pages - папка для хранения page object объектов страниц
* tests - папка для хранения автотестов и вспомогательных материалов

# Запуск тестов для отладки #

## HEADED mode ##

### Запуск тестов по одному ###

* python -m pytest tests/test_case_0.py::test_pizzas_list_and_city --headed --slowmo 1000
* python -m pytest tests/test_case_1.py::test_add_pizza --headed --slowmo 1000
* python -m pytest tests/test_case_2.py::test_add_two_pizzas --headed --slowmo 1000

### Запуск всех тестов ###

* python -m pytest tests --headed --slowmo 1000

## HEADLESS mode ###

### Запуск тестов по одному ###

* python -m pytest tests/test_case_0.py::test_pizzas_list_and_city
* python -m pytest tests/test_case_1.py::test_add_pizza
* python -m pytest tests/test_case_2.py::test_add_two_pizzas

### Запуск всех тестов ###

* python -m pytest tests 
