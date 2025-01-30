```markdown
# Аутентификация Пользователей

## Вход Пользователя

- **URL**: `/api/users/login/`
- **Метод**: `POST`
- **Описание**: Позволяет пользователям войти в систему и получить токен аутентификации.

### Пример Запроса

```http
POST http://127.0.0.1:8000/api/users/login/
Content-Type: application/json

{
  "username": "existing_user",
  "password": "user_password"
}
Пример Ответа
json
Копировать код
{
  "token": "your_auth_token"
}

Выход Пользователя
URL: /api/users/logout/
Метод: POST
Описание: Позволяет пользователям выйти из системы и аннулировать токен аутентификации.
Пример Запроса
http
Копировать код
POST http://127.0.0.1:8000/api/users/logout/
Content-Type: application/json
Authorization: Token your_auth_token
Пример Ответа
json
Копировать код
{
  "Success": "User logged out successfully."
}