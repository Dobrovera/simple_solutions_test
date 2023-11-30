## Django Stripe Checkout Проект

Django и Stripe API для обработки онлайн-платежей через Stripe Checkout


### Как это работает?
Проект задеплоен на Railway, ниже указаны ссылки для теста
1. Пример страницы товара 1: 

[/buy/1](https://simplesolutionstest-production.up.railway.app/buy/1) эндпоинт для получения Stripe Session Id товара
2. Пример страницы покупки товара 1:

[/item/1](https://simplesolutionstest-production.up.railway.app/item/1) эндпоинт c информацией по товару 1 и кнопкой Buy для перехода к оплате


### Для локального запуска
1. Клонируйте репозиторий

```
git clone https://github.com/Dobrovera/simple_solutions_test
```

2. Создайте в корне проекта файл .env и добавьте переменные

SECRET_KEY = 'your_secret_key'

STRIPE_SECRET_KEY = 'your_stripe_secret_key'

STRIPE_PUBLIC_KEY = 'your_stripe_public_key'


3. Установите зависимости
```
pip install -r requirements.txt
```
4. Настройка бд
```
python manage.py makemigrations app
python manage.py migrate
```
5. Запуск сервера Django
```
python manage.py runserver
```

### Используемый стек
Python3, Django, Stripe, HTML, JS, SQlite