from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from os import getenv
from dotenv import load_dotenv
import stripe

from .models import Item


load_dotenv()
stripe.api_key = getenv('STRIPE_SECRET_KEY')


def get_buy_session_id(request, id):
    """
        Получение Stripe Session ID для покупки выбранного товара.

        Параметры:
        - request: Объект HTTP-запроса.
        - id: Идентификатор товара для покупки.

        Возвращает:
        - JsonResponse: JSON-ответ, содержащий Stripe Session ID.
        """

    # Получение товара из базы данных
    item = get_object_or_404(Item, pk=id)

    # Создание новой сессии Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(item.get_absolute_url()),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
    )
    return JsonResponse({'session_id': session.id})


def get_item_page(request, id):
    """
       Отображение страницы с информацией о выбранном товаре и кнопкой "Buy".

       Параметры:
       - request: Объект HTTP-запроса.
       - id: Идентификатор товара для отображения.

       Возвращает:
       - Rendered HTML page: HTML-страница с информацией о товаре.
       """
    # Получение товара из базы данных
    item = get_object_or_404(Item, pk=id)

    # Отображение HTML-страницы с информацией о товаре
    return render(request, 'item_page.html', {'item': item})
