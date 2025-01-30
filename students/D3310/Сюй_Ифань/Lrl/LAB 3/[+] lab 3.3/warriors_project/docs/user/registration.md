```markdown
# Управление Пользователями

## Регистрация Пользователя

- **URL**: `/api/users/register/`
- **Метод**: `POST`
- **Описание**: Позволяет новым пользователям зарегистрироваться в системе.

### Пример Запроса

```http
POST http://127.0.0.1:8000/api/users/register/
Content-Type: application/json

{
  "username": "new_user",
  "password": "secure_password",
  "email": "new_user@example.com"
}

Пример Ответа
json
Копировать код
{
  "Success": "User 'new_user' registered successfully."
}

Вход Пользователя (Аутентификация)
URL: /api/users/login/
Метод: POST
Описание: Позволяет пользователям войти в систему и получить токен аутентификации.
Пример Запроса
http
Копировать код
POST http://127.0.0.1:8000/api/users/login/
Content-Type: application/json

{
  "username": "new_user",
  "password": "secure_password"
}
Пример Ответа
json
Копировать код
{
  "token": "your_auth_token"
}

Изменение Учетных Данных Пользователя
URL: /api/users/<int:pk>/update/
Метод: PUT или PATCH
Описание: Позволяет пользователям обновлять свои учетные данные.
Пример Запроса
http
Копировать код
PATCH http://127.0.0.1:8000/api/users/1/update/
Content-Type: application/json
Authorization: Token your_auth_token

{
  "email": "updated_email@example.com"
}
Пример Ответа
json
Копировать код
{
  "Success": "User updated successfully.",
  "User": {
    "id": 1,
    "username": "new_user",
    "email": "updated_email@example.com"
  }
}