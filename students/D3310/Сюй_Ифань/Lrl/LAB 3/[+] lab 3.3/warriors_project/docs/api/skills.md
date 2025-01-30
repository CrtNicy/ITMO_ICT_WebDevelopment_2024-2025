# Warriors API

## Получение Списка Всех Войн

- **URL**: `/api/skills/`
- **Метод**: `GET`
- **Описание**: Возвращает список всех навыков.

### Примеры Запросов и Ответов

```http
### Пример Запроса
GET http://127.0.0.1:8000/api/skills/

Пример Ответа
json
Копировать код
{
  "Skills": [
    {
      "id": 1,
      "title": "Archery"
    },
    {
      "id": 2,
      "title": "Stealth"
    },
    // Другие навыки...
  ]
}


Создание Нового Навыка
URL: /api/skill/create/
Метод: POST
Описание: Создаёт новый навык.
Пример Запроса
http
Копировать код
POST http://127.0.0.1:8000/api/skill/create/
Content-Type: application/json

{
  "title": "Alchemy"
}
Пример Ответа
json
Копировать код
{
  "Success": "Skill 'Alchemy' created successfully."
}