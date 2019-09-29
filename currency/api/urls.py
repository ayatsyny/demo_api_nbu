from django.urls import path
from .views import ListCurrencies


urlpatterns = [
    path('currencies/', ListCurrencies.as_view())
]
