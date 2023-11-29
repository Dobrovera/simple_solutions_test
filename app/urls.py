from django.urls import path
from .views import get_buy_session_id, get_item_page


urlpatterns = [
    path('buy/<int:id>', get_buy_session_id, name='get_buy_session_id'),
    path('item/<int:id>', get_item_page, name='get_item_page'),
]
