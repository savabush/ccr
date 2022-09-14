# Test Case CCR

Сервис разработан на django rest framework, с использованием swagger, pytest, mypy, flake8, django-debug-toolbar, pre-commit


## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone git@github.com:savabush/ccr.git
````
2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение: 

````
source \venv\bin\activate
````
5. Файл .env.example переименовать в .env и изменить данные в нем на подходящие вам 
6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver
```
***
### Запуск тестов
``` 
pytest
```
***
## Установка проекта с помощью docker-compose


1. Склонировать репозиторий с Github
```
git clone git@github.com:savabush/ccr.git
```
2. Перейти в директорию проекта
3. Файл .env.example переименовать в .env и изменить данные в нем на подходящие вам 
4. Запустить контейнеры 
``` 
sudo docker-compose up -d
 ```
5. Остановка работы контейнеров 
```
sudo docker-compose stop
```
***
```http://0.0.0.0:8000/api/v1/``` - api проекта

```http://0.0.0.0:8000/api/v1/news/``` - новости

```http://0.0.0.0:8000/api/v1/news/<pk>/``` - детальная информация о новости

```http://0.0.0.0:8000/api/v1/types/``` - типы новостей

```http://0.0.0.0:8000/api/v1/types/<pk>/``` - детальная информация о типе

```http://0.0.0.0:8000/docs/``` - docs проекта, оформленный через swagger
