### REST API для приложения yatube:

Предоставляет объекты в формате JSON и действия небходимые для работы с приложением yatube.
Полное описание доступно локально на localhost/redoc/

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexeyWer/yatube_api.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

Получение пяти публикаций начиная с шестой

```
Запрос:

GET http://127.0.0.1:8000/api/v1/posts/?offset=5&limit=5"

Ответ:

{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=10&limit=5",
  "previous": "http://api.example.org/accounts/?limit=5",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Создание публикации

```
Запрос:

POST http://127.0.0.1:8000/api/v1/posts/

Тело запроса:

{
"text": "string",
"image": "string",
"group": 0
}

Ответ:

{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
