# Warriors API

## Получение Списка Всех Войн

- **URL**: `/api/profession/create/`
- **Метод**: `POST`
- **Описание**: Создание новой специализации.

### Примеры Запросов и Ответов

```http
Пример Запроса

POST http://127.0.0.1:8000/api/profession/create/
Content-Type: application/json

{
  "title": "Shield Bearer",
  "description": "Специалист по использованию щита"
}

Пример Ответа
json
Копировать код
{
  "Success": "Profession 'Shield Bearer' created successfully."
}
