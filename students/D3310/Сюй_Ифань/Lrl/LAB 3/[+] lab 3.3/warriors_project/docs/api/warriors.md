# Warriors API
# api-эндпоинты
## Получение Списка Всех Войн

- **URL**: `/api/warriors/`
- **Метод**: `GET`
- **Описание**: Возвращает список всех воинов с их деталями, включая профессию и навыки.

### Примеры Запросов и Ответов

```http
GET http://127.0.0.1:8000/api/warriors/

{
  "Warriors": [
    {
      "id": 1,
      "race": "d",
      "race_display": "developer",
      "name": "Artem",
      "level": 10,
      "profession": {
        "id": 1,
        "title": "Sword Master",
        "description": "Мастер владения мечом"
      },
      "profession_id": 1,
      "skill_details": [
        {
          "skill_id": 1,
          "skill": {
            "id": 1,
            "title": "Archery"
          },
          "level": 5
        },
        {
          "skill_id": 2,
          "skill": {
            "id": 2,
            "title": "Stealth"
          },
          "level": 3
        }
      ]
    },
    // Другие воины...
  ]
}

### Пример Запроса

```http

POST http://127.0.0.1:8000/api/warrior/create/
Content-Type: application/json

{
  "race": "d",
  "name": "Artem",
  "level": 10,
  "profession_id": 1,
  "skills": [
    {"skill_id": 1, "level": 5},
    {"skill_id": 2, "level": 3}
  ]
}

Пример Ответа

{
  "Success": "Warrior 'Artem' created successfully.",
  "Warrior": {
    "id": 2,
    "race": "d",
    "race_display": "developer",
    "name": "Artem",
    "level": 10,
    "profession": {
      "id": 1,
      "title": "Sword Master",
      "description": "Мастер владения мечом"
    },
    "profession_id": 1,
    "skill_details": [
      {
        "skill_id": 1,
        "skill": {
          "id": 1,
          "title": "Archery"
        },
        "level": 5
      },
      {
        "skill_id": 2,
        "skill": {
          "id": 2,
          "title": "Stealth"
        },
        "level": 3
      }
    ]
  }
}


