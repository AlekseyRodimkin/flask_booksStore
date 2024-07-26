# Books Store

### Онлайн библиотека с возможностью покупки или аренды книг.
### Предусмотрена панель администратора. (/admin)
### У администратора есть возможность изменения списка и характеристик книг, пользователей и заказов.
### cloudipsp - Библиотека для проведения платежей через платформу  [Fondy](https://fondy.ua/ru/). Из-за некоторых ограничений, для работы из России необходим VPN для регистрации и проведение платежей (при нажатии купить/аренда). Но платформа предоставляет возможность использовать тестовые транзакции, что и использовано в проекте.
___
### 
- Клонировать репозиторий
- Установить виртуальное окружение
- Создать .env по .env.template
- Установить библиотеки
  ```python
  (.venv) booksStore>>> pip install -r requirements.txt
  ```
- Запустить файл start
