```markdown
# Настройки Учетной Записи Пользователя

## Обновление Учетных Данных

- **URL**: `/api/users/<int:pk>/update/`
- **Метод**: `PUT` или `PATCH`
- **Описание**: Позволяет пользователям обновлять свои учетные данные.

### Пример Запроса

```http
PATCH http://127.0.0.1:8000/api/users/1/update/
Content-Type: application/json
Authorization: Token your_auth_token

{
  "email": "new_email@example.com",
  "password": "new_secure_password"
}
Пример Ответа
json
Копировать код
{
  "Success": "User updated successfully.",
  "User": {
    "id": 1,
    "username": "existing_user",
    "email": "new_email@example.com"
  }
}
Изменение Пароля
URL: /api/users/<int:pk>/change_password/
Метод: POST
Описание: Позволяет пользователям изменить свой пароль.
Пример Запроса
http
Копировать код
POST http://127.0.0.1:8000/api/users/1/change_password/
Content-Type: application/json
Authorization: Token your_auth_token

{
  "old_password": "old_password",
  "new_password": "new_secure_password"
}
Пример Ответа
json
Копировать код
{
  "Success": "Password changed successfully."
}